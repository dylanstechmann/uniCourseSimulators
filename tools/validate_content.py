#!/usr/bin/env python3
"""Validate authored inventory without equating schema validity with university quality."""

from __future__ import annotations

import argparse
import json
import re
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


def validate_graph(courses: dict[str, dict[str, Any]], report: Report) -> None:
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
        check_refs(edges, set(courses), "prerequisite course", course_id, report)
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
            if source["reuse_mode"] == "link-only-comparator" and any(
                source["permissions"][key]
                for key in ("quotation", "adaptation", "redistribution")
            ):
                report.error(
                    "source-permissions",
                    registry_path,
                    f"Comparator-only source {source['id']} must not claim content reuse permissions.",
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
    validate_graph(courses, report)
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
                    headers={"User-Agent": "Lattice-CourseLab-content-validation/1.0"},
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
