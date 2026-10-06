#!/usr/bin/env python3
"""Validate authored inventory without equating schema validity with university quality."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from hashlib import sha256
from pathlib import Path, PureWindowsPath
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError
from referencing import Registry, Resource

for import_path in (
    Path(__file__).resolve().parent,
    Path(__file__).resolve().parents[1] / "backend",
):
    if import_path.is_dir():
        sys.path.insert(0, str(import_path))
from courselab.assessment import validate_assessment_configuration  # noqa: E402

MATURE = {"complete", "externally reviewed"}
GATE_CHECKS = {
    "broken_links",
    "numerical_recalculation",
    "unit_tolerance",
    "grader_mutation",
    "accessibility",
    "frontend_tests",
    "backend_tests",
}
PLACEHOLDER = re.compile(
    r"\b(?:TODO|TBD)\b|lorem ipsum|coming soon|\bplaceholder(?: material| content| text)?\b|"
    r"insert (?:lesson|content|text) here",
    re.IGNORECASE,
)


@dataclass
class Report:
    errors: list[dict[str, str]] = field(default_factory=list)
    warnings: list[dict[str, str]] = field(default_factory=list)
    inventory: dict[str, int] = field(
        default_factory=lambda: {
            "courses": 0,
            "lessons": 0,
            "questions": 0,
            "cards": 0,
            "cases": 0,
        }
    )

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, code: str, path: Path | str, message: str) -> None:
        self.errors.append({"code": code, "path": str(path), "message": message})

    def warn(self, code: str, path: Path | str, message: str) -> None:
        self.warnings.append({"code": code, "path": str(path), "message": message})

    def as_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "inventory": self.inventory,
            "errors": self.errors,
            "warnings": self.warnings,
        }


def load_json(path: Path, report: Report) -> Any | None:
    def reject_nonfinite(value: str) -> None:
        raise ValueError(f"Non-finite JSON number {value} is forbidden.")

    try:
        return json.loads(
            path.read_text(encoding="utf-8"), parse_constant=reject_nonfinite
        )
    except (OSError, UnicodeError, ValueError) as exc:
        report.error("json", path, f"Cannot read valid UTF-8 JSON: {exc}")
        return None


def safe_file(course_root: Path, reference: str, report: Report) -> Path | None:
    """Resolve an authoring reference without permitting host paths or symlink escape."""
    if not isinstance(reference, str) or not reference or "\\" in reference:
        report.error(
            "path",
            course_root,
            "Content reference must be a nonempty relative POSIX path.",
        )
        return None
    relative = Path(reference)
    if (
        relative.is_absolute()
        or PureWindowsPath(reference).is_absolute()
        or re.match(r"^[a-zA-Z]:", reference)
    ):
        report.error(
            "path",
            reference,
            "Absolute paths and URI references are forbidden in course files.",
        )
        return None
    resolved = (course_root / relative).resolve()
    try:
        resolved.relative_to(course_root.resolve())
    except ValueError:
        report.error(
            "path",
            reference,
            "Reference escapes its course directory, including through a symlink.",
        )
        return None
    if not resolved.is_file():
        report.error(
            "missing-file", resolved, "Referenced content file does not exist."
        )
        return None
    return resolved


def normalize(text: str) -> str:
    return " ".join(re.findall(r"\w+", text.casefold()))


def prose_only(markdown: str) -> str:
    return "\n".join(
        line for line in markdown.splitlines() if not line.lstrip().startswith("#")
    )


def check_text(
    text: str, path: Path | str, report: Report, minimum_words: int = 1
) -> None:
    normalized = normalize(text)
    words = normalized.split()
    if not words:
        report.error("empty-content", path, "Material has no explanatory content.")
    elif len(words) < minimum_words:
        report.error(
            "depth",
            path,
            f"Authored material has {len(words)} words; minimum substantial reading threshold is {minimum_words}.",
        )
    if PLACEHOLDER.search(text):
        report.error(
            "placeholder", path, "Placeholder or unfinished authoring marker found."
        )
    if len(words) >= 100 and len(set(words)) / len(words) < 0.15:
        report.error(
            "repetitive-content",
            path,
            "Repeated low-information vocabulary cannot satisfy instructional depth.",
        )
    paragraphs = [
        normalize(p)
        for p in re.split(r"\n\s*\n", text)
        if len(normalize(p).split()) >= 35
    ]
    if len(paragraphs) != len(set(paragraphs)):
        report.error(
            "duplicate-paragraph",
            path,
            "A substantial paragraph is repeated within this reading.",
        )


def schema_validators(root: Path, report: Report) -> dict[str, Draft202012Validator]:
    documents = {}
    for path in sorted((root / "content/schemas").glob("*.schema.json")):
        schema = load_json(path, report)
        if not schema:
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as exc:
            report.error("invalid-schema", path, str(exc))
            continue
        documents[path.name] = schema
    registry = Registry().with_resources(
        (schema["$id"], Resource.from_contents(schema)) for schema in documents.values()
    )
    return {
        name: Draft202012Validator(
            schema, registry=registry, format_checker=FormatChecker()
        )
        for name, schema in documents.items()
    }


def apply_schema(
    document: Any,
    name: str,
    path: Path,
    validators: dict[str, Draft202012Validator],
    report: Report,
) -> bool:
    validator = validators.get(name)
    if not validator:
        report.error("missing-schema", path, f"Required schema {name} is unavailable.")
        return False
    failures = sorted(validator.iter_errors(document), key=lambda e: str(e.json_path))
    for error in failures:
        report.error("schema", path, f"{error.json_path}: {error.message}")
    return not failures


def unique_ids(
    items: list[dict[str, Any]], kind: str, path: Path, report: Report
) -> set[str]:
    ids = [item.get("id") for item in items if isinstance(item, dict)]
    if len(ids) != len(items) or any(
        not isinstance(value, str) or not value for value in ids
    ):
        report.error("id", path, f"Every {kind} needs a nonempty string ID.")
    valid = [value for value in ids if isinstance(value, str)]
    for value, count in Counter(valid).items():
        if count > 1:
            report.error("duplicate-id", path, f"Duplicate {kind} ID: {value}")
    return set(valid)


def check_refs(
    refs: list[str], valid: set[str], kind: str, path: Path, report: Report
) -> None:
    for reference in refs:
        if reference not in valid:
            report.error("reference", path, f"Unknown {kind} reference: {reference}")


def validate_graph(
    courses: dict[str, dict[str, Any]],
    report: Report,
    extra_node_ids: set[str] | None = None,
) -> None:
    graph = {}
    for course_id, course in courses.items():
        prerequisites = course["prerequisites"]
        # All dependency relations are checked; concurrent edges can be symmetric only
        # when represented outside the dependency graph in a future contract version.
        edges = (
            prerequisites["course_ids"]
            + prerequisites.get("recommended_course_ids", [])
            + prerequisites.get("concurrent_course_ids", [])
        )
        check_refs(
            edges,
            set(courses) | (extra_node_ids or set()),
            "prerequisite course",
            course_id,
            report,
        )
        graph[course_id] = [edge for edge in edges if edge in courses]
    visited, active = set(), set()

    def visit(node: str, chain: list[str]) -> None:
        if node in active:
            report.error("prerequisite-cycle", node, " -> ".join(chain + [node]))
            return
        if node in visited:
            return
        active.add(node)
        for dependency in graph[node]:
            visit(dependency, chain + [node])
        active.remove(node)
        visited.add(node)

    for course_id in graph:
        visit(course_id, [])


def validate_curriculum_map(
    root: Path,
    courses: dict[str, dict[str, Any]],
    source_ids: set[str],
    validators: dict[str, Draft202012Validator],
    report: Report,
) -> set[str]:
    """Validate planning nodes and pathways without treating catalog entries as courses."""
    path = root / "content/curriculum-map.json"
    document = load_json(path, report)
    if document is None or not apply_schema(
        document, "curriculum-map.schema.json", path, validators, report
    ):
        return set()

    catalog_nodes = document["catalog_only"]
    catalog_ids = unique_ids(catalog_nodes, "catalog node", path, report)
    duplicates = catalog_ids & set(courses)
    for course_id in sorted(duplicates):
        report.error(
            "duplicate-curriculum-node",
            path,
            f"Catalog-only node {course_id} duplicates a course package ID.",
        )
    all_ids = set(courses) | catalog_ids
    graph: dict[str, list[str]] = {}
    for course_id, course in courses.items():
        prerequisites = course["prerequisites"]
        edges = (
            prerequisites["course_ids"]
            + prerequisites.get("recommended_course_ids", [])
            + prerequisites.get("concurrent_course_ids", [])
        )
        check_refs(edges, all_ids, "curriculum prerequisite", course_id, report)
        graph[course_id] = [edge for edge in edges if edge in all_ids]
    description_signatures: dict[str, str] = {}
    for node in catalog_nodes:
        node_id = node["id"]
        prerequisites = node["prerequisites"]
        edges = (
            prerequisites["course_ids"]
            + prerequisites["recommended_course_ids"]
            + prerequisites["concurrent_course_ids"]
        )
        check_refs(edges, all_ids, "curriculum prerequisite", node_id, report)
        check_refs(
            node["related_package_ids"],
            set(courses),
            "related partial package",
            node_id,
            report,
        )
        graph[node_id] = [edge for edge in edges if edge in all_ids]
        signature = normalize(node["description"])
        if signature in description_signatures:
            report.error(
                "duplicate-curriculum-description",
                path,
                f"Catalog entries {description_signatures[signature]} and {node_id} repeat the same description.",
            )
        description_signatures[signature] = node_id
        if PLACEHOLDER.search(node["description"]):
            report.error(
                "placeholder-curriculum-entry",
                path,
                f"Catalog entry {node_id} contains placeholder text.",
            )

    visited, active = set(), set()

    def visit(node_id: str, chain: list[str]) -> None:
        if node_id in active:
            report.error(
                "curriculum-prerequisite-cycle",
                path,
                " -> ".join(chain + [node_id]),
            )
            return
        if node_id in visited:
            return
        active.add(node_id)
        for dependency in graph.get(node_id, []):
            visit(dependency, chain + [node_id])
        active.remove(node_id)
        visited.add(node_id)

    for node_id in graph:
        visit(node_id, [])

    pathways = document["pathways"]
    pathway_ids = unique_ids(pathways, "pathway", path, report)
    pathways_by_id = {item["id"]: item for item in pathways}
    required_pathways = {
        "science-mathematics-foundation",
        "electrical-computer-engineering",
        "mechanical-engineering-robotics",
        "biomedical-engineering",
        "tissue-regenerative-medicine",
        "geroscience-aging",
        "drug-discovery-translational-science",
        "jhu-regenerative-stem-cell-prerequisites",
    }
    for missing in sorted(required_pathways - pathway_ids):
        report.error("required-pathway", path, f"Required pathway is missing: {missing}.")

    required_topics = {
        "calculus-1", "calculus-2", "calculus-3", "linear-algebra", "differential-equations",
        "statistics", "numerical-methods", "physics-mechanics", "physics-em", "statics", "dynamics",
        "mechanics-of-materials", "thermodynamics", "fluid-mechanics", "heat-mass-transfer",
        "materials-science", "circuits-1", "circuits-2", "analog-electronics", "digital-electronics",
        "signals-and-systems", "feedback-control", "instrumentation-and-sensors", "embedded-systems",
        "mechanical-design", "robotics-mechatronics", "engineering-design-experimental-methods",
    }
    for missing in sorted(required_topics - all_ids):
        report.error("required-curriculum-topic", path, f"Required subject node is missing: {missing}.")
    for pathway in pathways:
        check_refs(pathway["course_ids"], all_ids, "pathway node", pathway["id"], report)
        check_refs(pathway["source_ids"], source_ids, "pathway source", pathway["id"], report)

    alignments = document["alignment_maps"]
    alignment_ids = unique_ids(alignments, "curriculum alignment", path, report)
    if "jhu-regenerative-stem-cell-technologies" not in alignment_ids:
        report.error("required-curriculum-alignment", path, "The JHU regenerative/stem-cell topic map is missing.")
    for alignment in alignments:
        check_refs(alignment["source_ids"], source_ids, "alignment source", alignment["id"], report)
        check_refs(
            alignment["foundational_nodes"] + alignment["advanced_nodes"],
            all_ids,
            "alignment node",
            alignment["id"],
            report,
        )
        if alignment["id"] == "jhu-regenerative-stem-cell-technologies":
            required_foundations = {
                "organic-chemistry",
                "biochemistry",
                "molecular-biology",
                "cell-biology",
            }
            required_advanced = {
                "developmental-biology",
                "gene-therapy",
                "regenerative-medicine",
                "bioethics",
                "stem-cell-biology",
                "tissue-engineered-drug-discovery",
                "biotherapeutic-manufacturing",
                "cell-culture-stem-cell-lab",
            }
            if not required_foundations <= set(alignment["foundational_nodes"]):
                report.error("jhu-curriculum-map", path, "JHU foundational topics are incomplete.")
            if not required_advanced <= set(alignment["advanced_nodes"]):
                report.error("jhu-curriculum-map", path, "JHU advanced topic mapping is incomplete.")
            jhu_pathway = pathways_by_id.get("jhu-regenerative-stem-cell-prerequisites")
            required_map_nodes = required_foundations | required_advanced
            if jhu_pathway and not required_map_nodes <= set(jhu_pathway["course_ids"]):
                report.error(
                    "jhu-curriculum-map",
                    path,
                    "The JHU pathway sequence must include all foundational and advanced mapped topics.",
                )
            if any(term in alignment["disclaimer"].casefold() for term in ("equivalent", "transfer credit")) is False:
                report.error(
                    "jhu-curriculum-disclaimer",
                    path,
                    "The JHU map must explicitly disclaim equivalency and transfer credit.",
                )
    return catalog_ids


def legacy_reading_allowed(
    manifest: dict[str, Any],
    lesson: dict[str, Any],
    text: str,
    baseline: dict[str, Any],
) -> bool:
    origin = manifest["content_origin"]
    expected = next(
        (
            item
            for item in baseline.get("readings", [])
            if item.get("course_id") == manifest["id"]
            and item.get("lesson_id") == lesson["id"]
            and item.get("reading") == lesson["reading"]
        ),
        None,
    )
    return bool(
        manifest["maturity"] == "partial"
        and origin["kind"] == "legacy-prototype"
        and origin["source_path"]
        == baseline.get("source_path")
        == "src/data/courses.js"
        and origin["source_sha256"] == baseline.get("source_sha256")
        and origin["migration_version"] == baseline.get("migration_version") == "1.0"
        and expected
        and expected.get("sha256") == sha256(text.encode("utf-8")).hexdigest()
    )


def complete_gate(
    manifest: dict[str, Any],
    course_root: Path,
    lessons: list[dict[str, Any]],
    questions: list[dict[str, Any]],
    covered: set[str],
    report: Report,
) -> None:
    if manifest["maturity"] not in MATURE:
        return

    def require(condition: bool, message: str) -> None:
        if not condition:
            report.error("complete-gate", course_root, message)

    duration = manifest["duration"]
    weeks = duration["weeks"]
    conventional = (
        duration["instructional_weeks"] is not None
        and 12 <= duration["instructional_weeks"] <= 15
    )
    equivalent = (
        isinstance(duration["equivalent_structure"], str)
        and len(duration["equivalent_structure"].split()) >= 40
    )
    require(
        conventional or equivalent,
        "Complete courses require 12–15 instructional weeks or a substantial equivalent-structure rationale.",
    )
    require(
        len(weeks) >= 12 and all(week["lesson_ids"] for week in weeks),
        "At least 12 populated instructional periods are required.",
    )
    require(
        len(lessons) >= 24,
        "At least 24 substantial lessons are required; counts alone do not establish depth.",
    )
    require(
        manifest["workload"]["estimated_total_hours"] is not None,
        "A justified total workload estimate is required.",
    )
    require(
        manifest["workload"]["estimated_hours_per_week"] is not None,
        "A justified weekly workload estimate is required.",
    )
    all_objectives = {
        item["id"] for item in manifest["outcomes"] + manifest["lesson_objectives"]
    }
    require(
        bool(all_objectives) and all_objectives <= covered,
        "Every outcome and lesson objective must map to a graded or formative assessment.",
    )
    assessments = manifest["assessments"]
    graded = [item for item in assessments if item["mode"] == "graded"]
    kinds = Counter(item["type"] for item in assessments if item["mode"] == "graded")
    require(
        kinds["homework"] >= 8,
        "At least eight substantive graded homework sets are required.",
    )
    require(
        sum(kinds[kind] for kind in ("lab", "simulation", "data-analysis", "design"))
        >= 3,
        "At least three substantive lab, simulation, data-analysis, or design activities are required.",
    )
    for kind in ("midterm", "final", "project"):
        require(kinds[kind] >= 1, f"A graded {kind} is required.")
    homework_signatures = []
    for assessment in graded:
        require(
            bool(assessment["objective_ids"]) and assessment["points"] > 0,
            f"Graded assessment {assessment['id']} requires objectives and positive points.",
        )
        if assessment["type"] == "homework":
            require(
                len(assessment["question_ids"]) >= 5,
                f"Homework {assessment['id']} must contain at least five substantive items.",
            )
            homework_signatures.append(tuple(sorted(assessment["question_ids"])))
        if assessment["type"] in {"midterm", "final"}:
            require(
                len(assessment["question_ids"]) >= 15,
                f"Exam {assessment['id']} must contain at least fifteen substantive items.",
            )
        if assessment["type"] in {
            "lab",
            "simulation",
            "data-analysis",
            "design",
            "project",
        }:
            activity_path = safe_file(course_root, assessment["path"], report)
            require(
                activity_path is not None
                and activity_path.suffix.lower() in {".md", ".mdx"},
                f"Activity {assessment['id']} requires its own substantial instructional brief and rubric references.",
            )
            if activity_path and activity_path.suffix.lower() in {".md", ".mdx"}:
                check_text(
                    prose_only(activity_path.read_text(encoding="utf-8")),
                    activity_path,
                    report,
                    minimum_words=250,
                )
    require(
        len(homework_signatures) == len(set(homework_signatures)),
        "Repeated homework inventories cannot satisfy the homework sequence.",
    )
    require(
        len(questions) >= 80,
        "A bank of at least 80 distinct substantive items is required for full-course coverage.",
    )
    require(
        len({question["type"] for question in questions}) >= 3,
        "At least three assessment response types are required.",
    )
    require(
        any(question.get("randomization", {}).get("seeded") for question in questions),
        "Seeded randomized item specifications are required.",
    )
    require(
        manifest["grading_policy"]["mode"] == "graded-course",
        "A complete course must define a course grade policy.",
    )
    weights = manifest["grading_policy"]["categories"]
    require(
        bool(weights)
        and abs(sum(category["weight"] for category in weights) - 1) < 1e-8,
        "Course grade category weights must sum to one.",
    )
    require(
        manifest["accessibility"]["review_status"] == "reviewed",
        "Content accessibility review is required.",
    )
    review = manifest["review"]
    require(
        review["status"] in {"internal", "external"}
        and review["reviewed_version"] == manifest["version"]
        and bool(review["reviewers"]),
        "A real named human review with evidence for this version is required.",
    )
    if manifest["maturity"] == "externally reviewed":
        require(
            review["status"] == "external",
            "Externally reviewed requires an actual external review of this version.",
        )
    evidence = manifest.get("validation_evidence", {})
    checks = evidence.get("checks", {})
    require(
        all(checks.get(check) is True for check in GATE_CHECKS),
        "All independent validation checks must have recorded passing evidence.",
    )
    if not evidence.get("report"):
        require(
            False, "A machine-readable validation report with executions is required."
        )
    else:
        evidence_path = safe_file(course_root, evidence["report"], report)
        if evidence_path:
            record = load_json(evidence_path, report)
            require(
                isinstance(record, dict)
                and record.get("course_id") == manifest["id"]
                and record.get("version") == manifest["version"]
                and bool(record.get("executed_at"))
                and bool(record.get("executions"))
                and all(
                    record.get("checks", {}).get(check) is True for check in GATE_CHECKS
                ),
                "Validation report must identify this course version, executed checks, and actual recorded results.",
            )
    require(
        not manifest["limitations"],
        "Complete-course blockers must be resolved rather than retained as package limitations.",
    )


def validate_course(
    manifest: dict[str, Any],
    course_root: Path,
    sources: set[str],
    validators: dict[str, Draft202012Validator],
    baseline: dict[str, Any],
    seen_readings: dict[str, str],
    seen_questions: dict[str, str],
    report: Report,
) -> None:
    report.inventory["courses"] += 1
    course_path = course_root / "course.json"
    objective_records = manifest["outcomes"] + manifest["lesson_objectives"]
    objective_ids = unique_ids(
        objective_records, "learning objective", course_path, report
    )
    outcome_ids = {outcome["id"] for outcome in manifest["outcomes"]}
    for objective in manifest["lesson_objectives"]:
        check_refs(
            objective.get("course_outcome_ids", []),
            outcome_ids,
            "course outcome",
            course_path,
            report,
        )
    modules = manifest["modules"]
    module_ids = unique_ids(modules, "module", course_path, report)
    lessons = [lesson for module in modules for lesson in module["lessons"]]
    lesson_ids = unique_ids(lessons, "lesson", course_path, report)
    assessment_ids = unique_ids(
        manifest["assessments"], "assessment", course_path, report
    )
    try:
        validate_assessment_configuration(
            manifest.get("assessments", []), manifest.get("grading_policy", {})
        )
    except (AttributeError, TypeError, ValueError) as exc:
        report.error("assessment-policy", course_path, str(exc))
    report.inventory["lessons"] += len(lessons)
    questions = []
    # Repeated references to a bank share one authoring source, not duplicate items.
    bank_paths = {
        assessment["path"]
        for assessment in manifest["assessments"]
        if assessment["question_ids"]
    }
    for reference in sorted(bank_paths):
        bank_path = safe_file(course_root, reference, report)
        if not bank_path:
            continue
        bank = load_json(bank_path, report)
        if bank is None or not apply_schema(
            bank, "question-bank.schema.json", bank_path, validators, report
        ):
            continue
        if bank["course_id"] != manifest["id"]:
            report.error(
                "bank-course",
                bank_path,
                "Question bank course_id does not match its manifest.",
            )
        questions.extend(bank["questions"])
    question_ids = unique_ids(questions, "question", course_path, report)
    report.inventory["questions"] += len(questions)
    covered = set()
    for question in questions:
        check_refs(
            question["objective_ids"], objective_ids, "objective", course_path, report
        )
        covered.update(question["objective_ids"])
        check_text(question["prompt"], question["id"], report, minimum_words=5)
        question_key = normalize(question["prompt"])
        if question_key in seen_questions:
            report.error(
                "duplicate-question",
                question["id"],
                f"Prompt duplicates {seen_questions[question_key]}.",
            )
        else:
            seen_questions[question_key] = question["id"]
        solution = question["solution_spec"]
        if question["type"] == "symbolic":
            variables = solution.get("variables", [])
            assumptions = solution.get("assumptions", {})
            if (
                isinstance(variables, list)
                and isinstance(assumptions, dict)
                and set(assumptions) - set(variables)
            ):
                report.error(
                    "answer-spec",
                    question["id"],
                    "Symbolic assumptions may only name declared variables.",
                )
        if question["type"] in {"data_interpretation", "structured"}:
            fields = question.get("response_fields", [])
            field_specs = solution.get("field_specs", [])
            field_ids = [field.get("id") for field in fields if isinstance(field, dict)]
            spec_ids = [field.get("id") for field in field_specs if isinstance(field, dict)]
            if (
                len(field_ids) != len(fields)
                or len(spec_ids) != len(field_specs)
                or len(field_ids) != len(set(field_ids))
                or len(spec_ids) != len(set(spec_ids))
                or set(field_ids) != set(spec_ids)
            ):
                report.error(
                    "answer-spec",
                    question["id"],
                    "Data-interpretation response fields and answer specifications must have unique matching IDs.",
                )
            else:
                specifications = {field["id"]: field for field in field_specs}
                for field in fields:
                    spec = specifications[field["id"]]
                    if field.get("type") != spec.get("type"):
                        report.error(
                            "answer-spec",
                            question["id"],
                            f"Data-interpretation field {field['id']} has mismatched response and answer types.",
                        )
                    if field.get("type") == "single_choice":
                        options = field.get("options", [])
                        answer = spec.get("answer")
                        if type(answer) is not int or answer < 0 or answer >= len(options):
                            report.error(
                                "answer-spec",
                                question["id"],
                                f"Data-interpretation choice field {field['id']} has an answer outside its option array.",
                            )
                    if field.get("type") == "numeric":
                        check_text(field.get("prompt", ""), f"{question['id']}/{field['id']}", report, minimum_words=5)
                field_points = sum(
                    field.get("points", 0)
                    for field in fields
                    if isinstance(field.get("points"), (int, float))
                    and not isinstance(field.get("points"), bool)
                )
                if not math.isclose(field_points, question.get("points", 0), rel_tol=0, abs_tol=1e-8):
                    report.error(
                        "answer-spec",
                        question["id"],
                        "Data-interpretation field points must sum to the parent question points.",
                    )
                if any(
                    field.get("type") == "single_choice"
                    and (not isinstance(field.get("options"), list) or len(field["options"]) < 2)
                    for field in fields
                ):
                    report.error(
                        "answer-spec",
                        question["id"],
                        "Each data-interpretation choice field requires at least two public options.",
                    )
                if question["type"] == "structured":
                    rubric = solution.get("rubric", [])
                    rubric_ids = [item.get("id") for item in rubric if isinstance(item, dict)]
                    if (
                        len(rubric_ids) != len(rubric)
                        or len(rubric_ids) != len(set(rubric_ids))
                        or set(rubric_ids) != set(field_ids)
                    ):
                        report.error(
                            "answer-spec",
                            question["id"],
                            "Structured rubric criteria must have unique IDs matching each response field.",
                        )
                    else:
                        criteria = {item["id"]: item for item in rubric}
                        if any(
                            not math.isclose(
                                criteria[field["id"]].get("points", 0),
                                field.get("points", 0),
                                rel_tol=0,
                                abs_tol=1e-8,
                            )
                            for field in fields
                        ):
                            report.error(
                                "answer-spec",
                                question["id"],
                                "Structured rubric criterion points must match response-field points.",
                            )
        if question["type"] == "graph":
            graph = question.get("graph_spec", {})
            axes = {}
            valid_axes = isinstance(graph, dict)
            if valid_axes:
                for axis_id in ("x_axis", "y_axis"):
                    axis = graph.get(axis_id)
                    if (
                        not isinstance(axis, dict)
                        or not isinstance(axis.get("label"), str)
                        or len(axis["label"].strip()) < 3
                        or isinstance(axis.get("minimum"), bool)
                        or not isinstance(axis.get("minimum"), (int, float))
                        or not math.isfinite(axis["minimum"])
                        or abs(axis["minimum"]) > 1e12
                        or isinstance(axis.get("maximum"), bool)
                        or not isinstance(axis.get("maximum"), (int, float))
                        or not math.isfinite(axis["maximum"])
                        or abs(axis["maximum"]) > 1e12
                        or axis["minimum"] >= axis["maximum"]
                    ):
                        valid_axes = False
                        break
                    axes[axis_id] = (axis["minimum"], axis["maximum"])
            public_points = graph.get("points", []) if isinstance(graph, dict) else []
            if not isinstance(public_points, list):
                public_points = []
            observations = graph.get("observations", []) if isinstance(graph, dict) else []
            if not isinstance(observations, list):
                observations = []
            expected_points = solution.get("points", [])
            if not isinstance(expected_points, list):
                expected_points = []
            rubric = solution.get("rubric", [])
            if not isinstance(rubric, list):
                rubric = []
            point_ids = [
                item.get("id") for item in public_points
                if isinstance(item, dict) and isinstance(item.get("id"), str)
            ]
            answer_ids = [
                item.get("id") for item in expected_points
                if isinstance(item, dict) and isinstance(item.get("id"), str)
            ]
            criterion_ids = [
                item.get("id") for item in rubric
                if isinstance(item, dict) and isinstance(item.get("id"), str)
            ] if isinstance(rubric, list) else []
            expected_criteria = {
                f"{point_id}_{coordinate}"
                for point_id in point_ids
                for coordinate in ("x", "y")
            }
            if (
                not valid_axes
                or not 2 <= len(public_points) <= 20
                or len(point_ids) != len(public_points)
                or len(point_ids) != len(set(point_ids))
                or len(observations) != len(public_points)
                or len(answer_ids) != len(expected_points)
                or len(answer_ids) != len(set(answer_ids))
                or set(point_ids) != set(answer_ids)
                or len(criterion_ids) != len(rubric)
                or len(criterion_ids) != len(set(criterion_ids))
                or set(criterion_ids) != expected_criteria
            ):
                report.error(
                    "answer-spec",
                    question["id"],
                    "Graph points, axis bounds, answer coordinates, and rubric criteria must map uniquely.",
                )
            else:
                answers = {item["id"]: item for item in expected_points}
                criteria = {item["id"]: item for item in rubric}
                graph_points_valid = True
                observation_ids = [
                    item.get("id") for item in observations
                    if isinstance(item, dict) and isinstance(item.get("id"), str)
                ]
                if (
                    len(observation_ids) != len(observations)
                    or len(observation_ids) != len(set(observation_ids))
                    or set(observation_ids) != set(point_ids)
                ):
                    graph_points_valid = False
                observation_by_id = {
                    item["id"]: item for item in observations
                    if isinstance(item, dict) and isinstance(item.get("id"), str)
                }
                for point_id, answer in answers.items():
                    for coordinate, axis_id in (("x", "x_axis"), ("y", "y_axis")):
                        criterion = criteria[f"{point_id}_{coordinate}"]
                        if (
                            not isinstance(criterion.get("criterion"), str)
                            or len(criterion["criterion"].strip()) < 10
                            or not isinstance(criterion.get("evidence"), list)
                            or not criterion["evidence"]
                            or any(
                                not isinstance(item, str) or len(item.strip()) < 3
                                for item in criterion["evidence"]
                            )
                        ):
                            graph_points_valid = False
                        value = answer.get(coordinate)
                        tolerance = answer.get(f"{coordinate}_tolerance")
                        minimum, maximum = axes[axis_id]
                        if (
                            isinstance(value, bool)
                            or not isinstance(value, (int, float))
                            or not math.isfinite(value)
                            or not minimum <= value <= maximum
                            or isinstance(tolerance, bool)
                            or not isinstance(tolerance, (int, float))
                            or not math.isfinite(tolerance)
                            or not 0 <= tolerance <= maximum - minimum
                        ):
                            graph_points_valid = False
                    if any(
                        isinstance(answer.get(key), bool)
                        or not isinstance(answer.get(key), (int, float))
                        or not math.isfinite(answer[key])
                        for key in ("x", "y", "x_tolerance", "y_tolerance")
                    ) or answer.get("x_tolerance", -1) < 0 or answer.get("y_tolerance", -1) < 0:
                        graph_points_valid = False
                        continue
                    observation = observation_by_id.get(point_id)
                    if (
                        not isinstance(observation, dict)
                        or isinstance(observation.get("x"), bool)
                        or not isinstance(observation.get("x"), (int, float))
                        or not math.isfinite(observation["x"])
                        or not isinstance(observation.get("values"), list)
                        or not 1 <= len(observation["values"]) <= 100
                        or any(
                            isinstance(value, bool)
                            or not isinstance(value, (int, float))
                            or not math.isfinite(value)
                            for value in observation["values"]
                        )
                    ):
                        graph_points_valid = False
                        continue
                    x_tolerance = answer.get("x_tolerance", -1)
                    y_tolerance = answer.get("y_tolerance", -1)
                    recalculated_y = math.fsum(observation["values"]) / len(observation["values"])
                    if (
                        not axes["x_axis"][0] <= observation["x"] <= axes["x_axis"][1]
                        or any(
                            not axes["y_axis"][0] <= value <= axes["y_axis"][1]
                            for value in observation["values"]
                        )
                        or abs(answer.get("x", math.inf) - observation["x"]) > x_tolerance
                        or abs(answer.get("y", math.inf) - recalculated_y) > y_tolerance
                    ):
                        report.error(
                            "numerical-recalculation",
                            f"{question['id']}/{point_id}",
                            "Graph answer coordinates do not match the supplied x value and independently recalculated sample mean within their tolerances.",
                        )
                rubric_points = sum(
                    item.get("points", 0)
                    for item in rubric
                    if isinstance(item.get("points"), (int, float))
                    and not isinstance(item.get("points"), bool)
                )
                if not graph_points_valid or not math.isclose(
                    rubric_points, question.get("points", 0), rel_tol=0, abs_tol=1e-8
                ):
                    report.error(
                        "answer-spec",
                        question["id"],
                        "Graph coordinates must fit the public axes, use bounded tolerances, and map to a complete point-sum rubric.",
                    )
        if question["type"] == "file_upload":
            validation = solution.get("validation_spec", {})
            checks = (
                validation.get("checks", [])
                if isinstance(validation, dict) and isinstance(validation.get("checks", []), list)
                else []
            )
            rubric = solution.get("rubric", [])
            if not isinstance(rubric, list):
                rubric = []
            check_ids = [
                item.get("id") for item in checks
                if isinstance(item, dict) and isinstance(item.get("id"), str)
            ]
            rubric_ids = [
                item.get("id") for item in rubric
                if isinstance(item, dict) and isinstance(item.get("id"), str)
            ]
            target_cells = [
                (item.get("row_id"), item.get("column"))
                for item in checks
                if isinstance(item, dict)
                and isinstance(item.get("row_id"), str)
                and isinstance(item.get("column"), str)
            ]
            columns = (
                validation.get("columns", [])
                if isinstance(validation, dict) and isinstance(validation.get("columns", []), list)
                else []
            )
            key_column = validation.get("key_column") if isinstance(validation, dict) else None
            if (
                len(check_ids) != len(checks)
                or len(check_ids) != len(set(check_ids))
                or len(rubric_ids) != len(rubric)
                or len(rubric_ids) != len(set(rubric_ids))
                or set(check_ids) != set(rubric_ids)
                or len(target_cells) != len(checks)
                or len(target_cells) != len(set(target_cells))
                or any(column not in columns or column == key_column for _, column in target_cells)
            ):
                report.error(
                    "answer-spec",
                    question["id"],
                    "CSV numeric checks must map uniquely to rubric criteria and non-key output columns.",
                )
            else:
                rubric_points = sum(
                    item.get("points", 0)
                    for item in rubric
                    if isinstance(item, dict)
                    and isinstance(item.get("points"), (int, float))
                    and not isinstance(item.get("points"), bool)
                )
                if not math.isclose(
                    rubric_points, question.get("points", 0), rel_tol=0, abs_tol=1e-8
                ):
                    report.error(
                        "answer-spec",
                        question["id"],
                        "CSV rubric points must sum to the parent question points.",
                    )
                for check in checks:
                    calculation = check.get("calculation") if isinstance(check, dict) else None
                    values = calculation.get("values") if isinstance(calculation, dict) else None
                    operation = calculation.get("operation") if isinstance(calculation, dict) else None
                    if (
                        operation not in {"count", "mean"}
                        or not isinstance(values, list)
                        or not values
                        or any(
                            isinstance(value, bool)
                            or not isinstance(value, (int, float))
                            or not math.isfinite(value)
                            for value in values
                        )
                        or not isinstance(check, dict)
                        or not isinstance(check.get("answer"), (int, float))
                        or isinstance(check.get("answer"), bool)
                        or not math.isfinite(check["answer"])
                        or not isinstance(check.get("unit"), str)
                        or not isinstance(check.get("unit_required", False), bool)
                        or (check.get("unit_required", False) and not check.get("unit"))
                        or isinstance(check.get("tolerance"), bool)
                        or not isinstance(check.get("tolerance"), (int, float))
                        or not math.isfinite(check.get("tolerance", 0))
                        or check.get("tolerance", 0) < 0
                        or isinstance(check.get("relative_tolerance", 0), bool)
                        or not isinstance(check.get("relative_tolerance", 0), (int, float))
                        or not math.isfinite(check.get("relative_tolerance", 0))
                        or not 0 <= check.get("relative_tolerance", 0) <= 1
                    ):
                        report.error(
                            "answer-spec",
                            f"{question['id']}/{check.get('id', '<invalid>') if isinstance(check, dict) else '<invalid>'}",
                            "CSV numeric checks require finite, independently recalculable source values.",
                        )
                        continue
                    recalculated = len(values) if operation == "count" else math.fsum(values) / len(values)
                    allowed_error = check.get("tolerance", 0) + check.get("relative_tolerance", 0) * abs(check["answer"])
                    if abs(recalculated - check["answer"]) > allowed_error:
                        report.error(
                            "numerical-recalculation",
                            f"{question['id']}/{check['id']}",
                            f"Authored answer {check['answer']} does not match independently recalculated {operation} {recalculated} within tolerance.",
                        )
        if question["type"] in {"single_choice", "multiple_select"}:
            answers = (
                [solution["answer"]]
                if question["type"] == "single_choice"
                else solution["answer"]
            )
            if any(answer >= len(question["options"]) for answer in answers):
                report.error(
                    "answer-spec",
                    question["id"],
                    "Correct choice index is outside the option array.",
                )
        if (
            question["type"] == "numeric"
            and manifest["maturity"] in MATURE
            and (
                not isinstance(solution.get("unit_required"), bool)
                or solution.get("dimensions") is None
                or solution.get("significant_figures") is None
            )
        ):
            report.error(
                "answer-spec",
                question["id"],
                "Complete-course numerical items require explicit dimensions, significant figures, and unit-entry policy.",
            )
        randomization = question.get("randomization")
        if randomization:
            seen_variant_ids = {"base"}
            variant_schema = validators.get("question.schema.json")
            for variant in randomization.get("variants", []):
                variant_id = variant.get("id", "<missing-id>")
                if variant_id in seen_variant_ids:
                    report.error(
                        "variant-id", course_path,
                        f"Question {question['id']} repeats variant identifier {variant_id}.",
                    )
                seen_variant_ids.add(variant_id)
                resolved = {key: value for key, value in question.items() if key != "randomization"}
                resolved.update({key: value for key, value in variant.items() if key != "id"})
                if variant_schema:
                    for error in variant_schema.iter_errors(resolved):
                        report.error(
                            "variant-schema", course_path,
                            f"Question {question['id']} variant {variant_id}: {error.message}",
                        )
                check_text(variant["prompt"], f"{question['id']}/{variant_id}", report, minimum_words=5)
                variant_key = normalize(variant["prompt"])
                if variant_key in seen_questions:
                    report.error(
                        "duplicate-question", question["id"],
                        f"Variant prompt duplicates {seen_questions[variant_key]}.",
                    )
                else:
                    seen_questions[variant_key] = f"{question['id']}/{variant_id}"
                variant_solution = variant["solution_spec"]
                if question["type"] in {"single_choice", "multiple_select"}:
                    answer = variant_solution["answer"]
                    if question["type"] == "single_choice":
                        answers = [answer]
                    else:
                        answers = answer if isinstance(answer, list) else []
                    if not answers or any(
                        type(index) is not int or index < 0 or index >= len(resolved["options"])
                        for index in answers
                    ):
                        report.error(
                            "answer-spec", question["id"],
                            f"Variant {variant_id} has a choice answer outside its option array.",
                        )
        if question["visibility"] == "restricted-server-assessment":
            report.error(
                "restricted-key",
                question["id"],
                "Production restricted answer keys must not be committed in public course packages.",
            )
    for assessment in manifest["assessments"]:
        check_refs(
            assessment["objective_ids"], objective_ids, "objective", course_path, report
        )
        check_refs(
            assessment["question_ids"], question_ids, "question", course_path, report
        )
        covered.update(assessment["objective_ids"])
        safe_file(course_root, assessment["path"], report)
    uncovered = sorted(objective_ids - covered)
    if uncovered and manifest["maturity"] not in MATURE:
        report.warn(
            "objective-coverage",
            course_path,
            f"{len(uncovered)} objective(s) have no authored assessment mapping; this is not demonstrated comprehensive coverage.",
        )
    for week in manifest["duration"]["weeks"]:
        check_refs(week["lesson_ids"], lesson_ids, "lesson", course_path, report)
        check_refs(
            week["assessment_ids"], assessment_ids, "assessment", course_path, report
        )
    week_numbers = [week["week"] for week in manifest["duration"]["weeks"]]
    if len(week_numbers) != len(set(week_numbers)):
        report.error(
            "duplicate-week", course_path, "Instructional week numbers must be unique."
        )
    cards_path = safe_file(course_root, manifest["retrieval_cards"], report)
    cards = []
    if cards_path:
        record = load_json(cards_path, report)
        if (
            not isinstance(record, dict)
            or record.get("course_id") != manifest["id"]
            or not isinstance(record.get("cards"), list)
        ):
            report.error(
                "cards",
                cards_path,
                "Retrieval inventory requires matching course_id and cards array.",
            )
        else:
            cards = record["cards"]
    card_ids = unique_ids(cards, "card", course_path, report)
    report.inventory["cards"] += len(cards)
    for card in cards:
        if not isinstance(card, dict):
            report.error(
                "cards", course_path, "Retrieval card records must be objects."
            )
            continue
        if not isinstance(card.get("front"), str) or not isinstance(
            card.get("back"), str
        ):
            report.error(
                "cards",
                course_path,
                "Each retrieval card requires front and back text.",
            )
            continue
        check_text(card["front"], card["id"], report)
        check_text(card["back"], card["id"], report, minimum_words=3)
        check_refs(
            [card.get("lesson_id", "")], lesson_ids, "card lesson", course_path, report
        )
        check_refs(
            card.get("objective_ids", []),
            objective_ids,
            "card objective",
            course_path,
            report,
        )
    case_path = safe_file(course_root, manifest["case_rubrics"], report)
    if case_path:
        record = load_json(case_path, report)
        if (
            not isinstance(record, dict)
            or record.get("course_id") != manifest["id"]
            or not isinstance(record.get("cases"), list)
        ):
            report.error(
                "cases",
                case_path,
                "Case inventory requires matching course_id and cases array.",
            )
        else:
            cases = record["cases"]
            unique_ids(cases, "case", case_path, report)
            report.inventory["cases"] += len(cases)
            for case in cases:
                if not isinstance(case, dict):
                    report.error("cases", case_path, "Case records must be objects.")
                    continue
                check_text(case.get("prompt", ""), case_path, report, minimum_words=10)
                check_refs(
                    case.get("objective_ids", []),
                    objective_ids,
                    "case objective",
                    case_path,
                    report,
                )
                if not isinstance(case.get("rubric"), list) or not case["rubric"]:
                    report.error(
                        "rubric", case_path, "A case requires explicit rubric criteria."
                    )
    for module in modules:
        check_refs(module["source_ids"], sources, "source", course_path, report)
        if not module["source_ids"]:
            report.error(
                "source-metadata",
                course_path,
                "Every instructional module requires provenance sources.",
            )
        for lesson in module["lessons"]:
            check_refs(
                lesson["objectives"], objective_ids, "objective", course_path, report
            )
            check_refs(
                lesson["question_ids"], question_ids, "question", course_path, report
            )
            check_refs(lesson["card_ids"], card_ids, "card", course_path, report)
            reading_path = safe_file(course_root, lesson["reading"], report)
            if not reading_path:
                continue
            if reading_path.suffix.lower() not in {".md", ".mdx"}:
                report.error(
                    "reading-format", reading_path, "Readings must be Markdown or MDX."
                )
                continue
            try:
                text = reading_path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                report.error("reading", reading_path, str(exc))
                continue
            legacy = legacy_reading_allowed(manifest, lesson, text, baseline)
            if legacy:
                report.warn(
                    "legacy-depth",
                    reading_path,
                    "Preserved short prototype reading; accepted only as verified partial legacy material.",
                )
            check_text(
                prose_only(text),
                reading_path,
                report,
                minimum_words=1 if legacy else 250,
            )
            check_text(
                lesson["worked_example"],
                lesson["id"],
                report,
                minimum_words=1 if legacy else 35,
            )
            reading_key = normalize(prose_only(text))
            if reading_key in seen_readings:
                report.error(
                    "duplicate-reading",
                    reading_path,
                    f"Reading duplicates {seen_readings[reading_key]}.",
                )
            else:
                seen_readings[reading_key] = str(reading_path)
    source_map_path = safe_file(course_root, manifest["source_map"], report)
    if source_map_path:
        mapping = load_json(source_map_path, report)
        if (
            not isinstance(mapping, dict)
            or mapping.get("course_id") != manifest["id"]
            or not mapping.get("license")
            or not isinstance(mapping.get("modules"), list)
        ):
            report.error(
                "source-map",
                source_map_path,
                "Source map needs matching course_id, license, and module records.",
            )
        else:
            mapped = set()
            map_ids = []
            for entry in mapping["modules"]:
                if not isinstance(entry, dict):
                    report.error(
                        "source-map",
                        source_map_path,
                        "Module source-map records must be objects.",
                    )
                    continue
                mapped.add(entry.get("module_id"))
                map_ids.append(entry.get("module_id"))
                check_refs(
                    entry.get("source_ids", []),
                    sources,
                    "source",
                    source_map_path,
                    report,
                )
                if (
                    not entry.get("license")
                    or not entry.get("relationship")
                    or "modifications" not in entry
                ):
                    report.error(
                        "source-map",
                        source_map_path,
                        "Each module mapping requires license, relationship, and modifications.",
                    )
            if mapped != module_ids or len(map_ids) != len(set(map_ids)):
                report.error(
                    "source-map",
                    source_map_path,
                    "Every authored module must have exactly one source-map identity.",
                )
    syllabus_path = safe_file(course_root, manifest["syllabus"], report)
    if syllabus_path:
        check_text(
            syllabus_path.read_text(encoding="utf-8"),
            syllabus_path,
            report,
            minimum_words=100 if modules else 10,
        )
    for reviewer in manifest["review"]["reviewers"]:
        evidence_path = safe_file(course_root, reviewer["evidence"], report)
        if evidence_path:
            check_text(
                evidence_path.read_text(encoding="utf-8"),
                evidence_path,
                report,
                minimum_words=30,
            )
    if manifest["review"]["status"] == "unreviewed" and manifest["review"]["reviewers"]:
        report.error(
            "review", course_path, "An unreviewed course cannot claim reviewers."
        )
    if not modules and manifest["maturity"] not in {"catalog-only", "outlined"}:
        report.error(
            "maturity",
            course_path,
            "A course without authored lessons must be catalog-only or outlined.",
        )
    if (
        manifest["maturity"] in {"catalog-only", "outlined", "partial"}
        and not manifest["limitations"]
    ):
        report.error(
            "maturity",
            course_path,
            "Incomplete courses must explicitly disclose their limitations.",
        )
    complete_gate(manifest, course_root, lessons, questions, covered, report)


def validate_repository(
    root: Path, *, check_links: bool = False, source_registry: Path | None = None
) -> Report:
    root = root.resolve()
    report = Report()
    validators = schema_validators(root, report)
    registry_path = source_registry or root / "content/sources/registry.json"
    source_document = load_json(registry_path, report)
    sources = set()
    if source_document is not None and apply_schema(
        source_document, "source.schema.json", registry_path, validators, report
    ):
        sources = unique_ids(
            source_document["sources"], "source", registry_path, report
        )
        for source in source_document["sources"]:
            if source["reuse_mode"] in {"link-only-comparator", "link-only-reference"} and any(
                source["permissions"][key]
                for key in ("quotation", "adaptation", "redistribution")
            ):
                report.error(
                    "source-permissions",
                    registry_path,
                    f"Link-only source {source['id']} must not claim content reuse permissions.",
                )
    baseline_path = root / "content/courses/legacy-inventory.json"
    baseline = load_json(baseline_path, report) if baseline_path.exists() else {}
    courses = {}
    seen_readings, seen_questions = {}, {}
    for path in sorted((root / "content/courses").glob("*/course.json")):
        manifest = load_json(path, report)
        if manifest is None or not apply_schema(
            manifest, "course.schema.json", path, validators, report
        ):
            continue
        if manifest["id"] in courses:
            report.error(
                "duplicate-course", path, f"Duplicate course ID {manifest['id']}."
            )
        if manifest["id"] != path.parent.name:
            report.error(
                "course-directory",
                path,
                "Course directory name must match its stable ID.",
            )
        courses[manifest["id"]] = manifest
        validate_course(
            manifest,
            path.parent,
            sources,
            validators,
            baseline or {},
            seen_readings,
            seen_questions,
            report,
        )
    if not courses:
        report.error(
            "empty-catalog",
            root / "content/courses",
            "No valid course manifests were found.",
        )
    catalog_ids = validate_curriculum_map(root, courses, sources, validators, report)
    validate_graph(courses, report, catalog_ids)
    if source_document and isinstance(source_document, dict):
        for source in source_document.get("sources", []):
            if isinstance(source, dict):
                check_refs(
                    source.get("mapped_courses", []),
                    set(courses),
                    "mapped course",
                    registry_path,
                    report,
                )
    if check_links and source_document and sources:
        for source in source_document["sources"]:
            try:
                request = Request(
                    source["url"],
                    headers={"User-Agent": "uniStemCourseSimulators-content-validation/1.0"},
                )
                with urlopen(request, timeout=12) as response:
                    if response.status >= 400:
                        report.error(
                            "broken-link", source["url"], f"HTTP {response.status}"
                        )
            except (HTTPError, URLError, TimeoutError, OSError) as exc:
                report.error("broken-link", source["url"], str(exc))
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument(
        "--source-registry",
        type=Path,
        help="Read-only source registry override for isolated worktree validation.",
    )
    parser.add_argument("--check-links", action="store_true")
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()
    report = validate_repository(
        args.root, check_links=args.check_links, source_registry=args.source_registry
    )
    if args.json_output:
        print(json.dumps(report.as_dict(), indent=2))
    else:
        print(
            f"Content validation {'PASS' if report.ok else 'FAIL'}: {report.inventory}"
        )
        print(
            f"{len(report.errors)} error(s), {len(report.warnings)} explicit limitation/depth warning(s)."
        )
        for error in report.errors:
            print(f"ERROR [{error['code']}] {error['path']}: {error['message']}")
        counts = Counter(warning["code"] for warning in report.warnings)
        for code, count in sorted(counts.items()):
            print(f"WARNING [{code}]: {count} occurrence(s); use --json for details.")
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
