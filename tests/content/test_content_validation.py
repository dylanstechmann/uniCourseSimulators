#!/usr/bin/env python3
"""Authoring adversaries: a valid inventory must not become a fabricated full course."""

from __future__ import annotations

import json
import math
import shutil
from copy import deepcopy
from pathlib import Path

import pytest

from tools.validate_content import validate_repository

ROOT = Path(__file__).resolve().parents[2]


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


@pytest.fixture
def repository(tmp_path: Path):
    for name in ("courses", "schemas"):
        shutil.copytree(ROOT / "content" / name, tmp_path / "content" / name)
    shutil.copy2(ROOT / "content/curriculum-map.json", tmp_path / "content/curriculum-map.json")
    source_ids = sorted(
        {
            source
            for path in (tmp_path / "content/courses").glob("*/course.json")
            for module in read(path)["modules"]
            for source in module["source_ids"]
        }
    )
    curriculum = read(tmp_path / "content/curriculum-map.json")
    source_ids = sorted(
        set(source_ids)
        | {
            source_id
            for item in curriculum["pathways"] + curriculum["alignment_maps"]
            for source_id in item["source_ids"]
        }
    )
    registry = {
        "schema_version": "1.0",
        "sources": [
            {
                "id": source_id,
                "title": "Synthetic source registry test fixture",
                "institution": "Test fixture",
                "url": f"https://example.edu/{source_id}",
                "accessed_at": "2026-10-05",
                "license": "fixture-only",
                "reuse_mode": "link-only-comparator",
                "permissions": {
                    "linking": True,
                    "quotation": False,
                    "adaptation": False,
                    "redistribution": False,
                },
                "attribution_requirements": [
                    "This is a synthetic validator fixture, not a real source."
                ],
                "third_party_notes": "No material is imported in this synthetic fixture.",
                "mapped_courses": [],
                "version": None,
                "checksum": None,
                "imported_assets": [],
            }
            for source_id in source_ids
        ],
    }
    registry_path = tmp_path / "content/sources/registry.json"
    registry_path.parent.mkdir()
    write(registry_path, registry)
    return tmp_path


@pytest.fixture
def course(repository):
    path = repository / "content/courses/cell-biology/course.json"
    return path, read(path)


def codes(report):
    return {error["code"] for error in report.errors}


def test_preserved_inventory_is_honest_partial(repository):
    result = validate_repository(repository)
    assert result.ok, result.errors
    assert result.inventory == {
        "courses": 25,
        "lessons": 119,
        "questions": 162,
        "cards": 239,
        "cases": 25,
    }
    assert sum(warning["code"] == "legacy-depth" for warning in result.warnings) == 98
    assert (
        sum(warning["code"] == "objective-coverage" for warning in result.warnings)
        == 25
    )
    assert all(
        read(path)["maturity"] == "partial"
        and read(path)["review"]["status"] == "unreviewed"
        for path in (repository / "content/courses").glob("*/course.json")
    )


def test_curriculum_map_has_eight_pathways_and_separated_engineering_subjects(repository):
    result = validate_repository(repository)
    assert result.ok, result.errors
    curriculum = read(repository / "content/curriculum-map.json")
    assert len(curriculum["pathways"]) == 8
    by_id = {item["id"]: item for item in curriculum["catalog_only"]}
    for node_id in (
        "numerical-methods",
        "statics",
        "dynamics",
        "mechanics-of-materials",
        "thermodynamics",
        "fluid-mechanics",
        "heat-mass-transfer",
        "materials-science",
        "circuits-1",
        "circuits-2",
        "analog-electronics",
        "digital-electronics",
        "signals-and-systems",
        "feedback-control",
        "instrumentation-and-sensors",
        "embedded-systems",
        "mechanical-design",
        "robotics-mechatronics",
        "engineering-design-experimental-methods",
    ):
        assert by_id[node_id]["maturity"] == "catalog-only"
        assert len(by_id[node_id]["description"]) >= 100


def test_curriculum_graph_rejects_cycles_across_packages_and_catalog(repository):
    curriculum_path = repository / "content/curriculum-map.json"
    curriculum = read(curriculum_path)
    next(node for node in curriculum["catalog_only"] if node["id"] == "precalculus")[
        "prerequisites"
    ]["course_ids"] = ["calculus-1"]
    write(curriculum_path, curriculum)

    course_path = repository / "content/courses/calculus-1/course.json"
    course = read(course_path)
    course["prerequisites"]["course_ids"] = ["precalculus"]
    write(course_path, course)

    assert "curriculum-prerequisite-cycle" in codes(validate_repository(repository))


def test_unknown_catalog_prerequisite_is_rejected(repository):
    curriculum_path = repository / "content/curriculum-map.json"
    curriculum = read(curriculum_path)
    next(node for node in curriculum["catalog_only"] if node["id"] == "precalculus")[
        "prerequisites"
    ]["course_ids"] = ["unlisted-subject"]
    write(curriculum_path, curriculum)

    assert "reference" in codes(validate_repository(repository))


@pytest.mark.parametrize("maturity", ["complete", "externally reviewed"])
def test_four_lessons_cannot_be_promoted(repository, course, maturity):
    path, manifest = course
    manifest["maturity"] = maturity
    write(path, manifest)
    result = validate_repository(repository)
    assert not result.ok
    assert {"complete-gate", "depth"} <= codes(result)
    assert any(
        "review" in error["message"].lower()
        for error in result.errors
        if error["code"] == "complete-gate"
    )


def test_missing_or_invalid_maturity_fails_schema(repository, course):
    path, manifest = course
    manifest["maturity"] = "semester-equivalent"
    write(path, manifest)
    assert "schema" in codes(validate_repository(repository))


def test_new_short_material_cannot_claim_legacy_exception(repository, course):
    path, manifest = course
    manifest["content_origin"]["kind"] = "original"
    write(path, manifest)
    assert "depth" in codes(validate_repository(repository))


def test_changed_legacy_reading_must_meet_new_depth(repository, course):
    path, manifest = course
    reading = path.parent / manifest["modules"][0]["lessons"][0]["reading"]
    reading.write_text(
        "# A replacement reading\n\nA short sentence about cells.\n", encoding="utf-8"
    )
    assert "depth" in codes(validate_repository(repository))


@pytest.mark.parametrize(
    "text,code",
    [
        ("# Heading only\n", "empty-content"),
        ("# Reading\n\nTODO write a substantial lesson.", "placeholder"),
        ("# Reading\n\n" + "cells molecules energy " * 120, "repetitive-content"),
    ],
)
def test_empty_placeholder_and_repeated_filler_fail(repository, course, text, code):
    path, manifest = course
    reading = path.parent / manifest["modules"][0]["lessons"][0]["reading"]
    reading.write_text(text, encoding="utf-8")
    assert code in codes(validate_repository(repository))


def test_duplicate_readings_are_not_more_depth(repository, course):
    path, manifest = course
    first = path.parent / manifest["modules"][0]["lessons"][0]["reading"]
    second = path.parent / manifest["modules"][1]["lessons"][0]["reading"]
    second.write_text(first.read_text(encoding="utf-8"), encoding="utf-8")
    assert "duplicate-reading" in codes(validate_repository(repository))


def test_duplicate_question_prompts_fail(repository, course):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    bank["questions"][1]["prompt"] = bank["questions"][0]["prompt"]
    write(bank_path, bank)
    assert "duplicate-question" in codes(validate_repository(repository))


def test_duplicate_question_ids_fail(repository, course):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    bank["questions"][1]["id"] = bank["questions"][0]["id"]
    write(bank_path, bank)
    assert "duplicate-id" in codes(validate_repository(repository))


def test_duplicate_variant_ids_fail(repository):
    path = repository / "content/courses/cell-biology/question-banks/practice.json"
    bank = read(path)
    variants = bank["questions"][0]["randomization"]["variants"]
    variants[1]["id"] = variants[0]["id"]
    write(path, bank)
    assert "variant-id" in codes(validate_repository(repository))


def test_variant_override_must_be_a_valid_standalone_question(repository):
    path = repository / "content/courses/cell-biology/question-banks/practice.json"
    bank = read(path)
    bank["questions"][0]["randomization"]["variants"][0]["solution_spec"]["answer"] = 99
    write(path, bank)
    result = validate_repository(repository)
    assert not result.ok
    assert "answer-spec" in codes(result)


@pytest.mark.parametrize(
    "change", ["missing-answer", "negative-tolerance", "out-of-range-choice"]
)
def test_incomplete_or_invalid_answer_specifications_fail(repository, course, change):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    if change == "missing-answer":
        del bank["questions"][2]["solution_spec"]["answer"]
    elif change == "negative-tolerance":
        bank["questions"][2]["solution_spec"]["tolerance"] = -1
    else:
        bank["questions"][0]["solution_spec"]["answer"] = 999
    write(bank_path, bank)
    assert codes(validate_repository(repository)) & {"schema", "answer-spec"}


def test_significant_figure_policy_is_bounded_by_schema(repository, course):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    numeric = next(question for question in bank["questions"] if question["type"] == "numeric")
    numeric["solution_spec"]["significant_figures"] = 13
    write(bank_path, bank)
    assert "schema" in codes(validate_repository(repository))


def test_structured_rubric_item_is_counted_while_course_remains_partial(repository, course):
    result = validate_repository(repository)
    assert result.ok, result.errors
    manifest = read(course[0])
    assert manifest["version"] == "0.12.0"
    assert manifest["maturity"] == "partial"
    assert result.inventory["questions"] == 162
    question = next(
        item
        for item in read(course[0].parent / "question-banks/practice.json")["questions"]
        if item["type"] == "structured"
    )
    assert len(question["solution_spec"]["rubric"]) == 4
    assert all(field["points"] == 1 for field in question["response_fields"])


def test_graph_plot_item_is_counted_while_statistics_course_remains_partial(repository):
    result = validate_repository(repository)
    assert result.ok, result.errors
    course_path = repository / "content/courses/statistics/course.json"
    manifest = read(course_path)
    bank = read(course_path.parent / "question-banks/practice.json")
    graph = next(item for item in bank["questions"] if item["type"] == "graph")
    assert manifest["version"] == "0.1.2"
    assert manifest["maturity"] == "partial"
    assert graph["id"] == "statistics-5:concentration-graph"
    assert len(graph["graph_spec"]["points"]) == 3
    assert result.inventory["questions"] == 162


def test_cell_biology_scope_does_not_claim_unwritten_weeks(repository):
    result = validate_repository(repository)
    assert result.ok, result.errors
    course_root = repository / "content/courses/cell-biology"
    manifest = read(course_root / "course.json")
    weeks = manifest["duration"]["weeks"]
    assert manifest["version"] == "0.12.0"
    assert manifest["maturity"] == "partial"
    assert len(weeks) == 14
    assert [week["week"] for week in weeks if week["lesson_ids"]] == [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
    assert len(weeks[0]["lesson_ids"]) == len(weeks[1]["lesson_ids"]) == 2
    assert len(weeks[2]["lesson_ids"]) == 2
    assert len(weeks[3]["lesson_ids"]) == 3
    assert len(weeks[4]["lesson_ids"]) == 2
    assert len(weeks[5]["lesson_ids"]) == 2
    assert len(weeks[6]["lesson_ids"]) == 3
    assert weeks[7]["week"] == 8
    assert "no midterm" in weeks[7]["title"].lower()
    assert weeks[7]["assessment_ids"] == ["cell-biology-week8-cumulative-practice"]
    practice_set = next(
        item for item in manifest["assessments"]
        if item["id"] == "cell-biology-week8-cumulative-practice"
    )
    assert practice_set["mode"] == "practice"
    assert len(practice_set["question_ids"]) == 12
    assert practice_set["points"] == 31
    assert weeks[8]["lesson_ids"] == ["cell-biology-17", "cell-biology-18"]
    assert weeks[8]["assessment_ids"] == ["cell-biology-week9-practice"]
    week9_practice = next(item for item in manifest["assessments"] if item["id"] == weeks[8]["assessment_ids"][0])
    assert week9_practice["mode"] == "practice"
    assert len(week9_practice["question_ids"]) == 8
    assert week9_practice["points"] == 14
    assert weeks[9]["lesson_ids"] == ["cell-biology-19", "cell-biology-20"]
    assert weeks[9]["assessment_ids"] == ["cell-biology-week10-practice"]
    week10_practice = next(item for item in manifest["assessments"] if item["id"] == weeks[9]["assessment_ids"][0])
    assert week10_practice["mode"] == "practice"
    assert len(week10_practice["question_ids"]) == 7
    assert week10_practice["points"] == 13
    assert weeks[10]["lesson_ids"] == ["cell-biology-21", "cell-biology-22"]
    assert weeks[10]["assessment_ids"] == ["cell-biology-week11-practice"]
    week11_practice = next(item for item in manifest["assessments"] if item["id"] == weeks[10]["assessment_ids"][0])
    assert week11_practice["mode"] == "practice"
    assert len(week11_practice["question_ids"]) == 7
    assert week11_practice["points"] == 13
    assert all(not week["lesson_ids"] for week in weeks[11:])
    assert all(not week["assessment_ids"] for week in weeks[11:])
    assert manifest["grading_policy"]["mode"] == "formative-only"

    source_map = read(course_root / "source-map.json")
    mapped_ids = [item["module_id"] for item in source_map["modules"]]
    assert len(mapped_ids) == len(set(mapped_ids)) == len(manifest["modules"])
    assert "Weeks 1–7" in (course_root / "syllabus.md").read_text(encoding="utf-8")
    crosswalk = (course_root / "assessment-crosswalk.md").read_text(encoding="utf-8")
    assert "not a midterm" in crosswalk
    assert "No exam questions" in crosswalk

    for lesson_id in (
        "cell-biology-1",
        "cell-biology-2",
        "cell-biology-5",
        "cell-biology-6",
        "cell-biology-7",
        "cell-biology-8",
        "cell-biology-9",
        "cell-biology-10",
        "cell-biology-11",
        "cell-biology-12",
        "cell-biology-13",
        "cell-biology-14",
        "cell-biology-15",
        "cell-biology-16",
        "cell-biology-17",
        "cell-biology-18",
        "cell-biology-19",
        "cell-biology-20",
        "cell-biology-21",
        "cell-biology-22",
    ):
        lesson = next(
            lesson
            for module in manifest["modules"]
            for lesson in module["lessons"]
            if lesson["id"] == lesson_id
        )
        reading = (course_root / lesson["reading"]).read_text(encoding="utf-8")
        assert len(reading.split()) >= 450


def test_week4_enzyme_numeric_keys_are_independently_recalculated(repository):
    bank = read(
        repository / "content/courses/cell-biology/question-banks/practice.json"
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["cell-biology-9:coupling-energy"]["solution_spec"]["answer"] == (
        12.0 - 21.0
    )
    assert questions["cell-biology-9:rate-at-km"]["solution_spec"]["answer"] == (
        (4 * 20) / 2
    )
    assert questions["cell-biology-10:rate-prediction"]["solution_spec"]["answer"] == (
        120 * 40 / (20 + 40)
    )


def test_week7_chip_percent_input_is_independently_recalculated(repository):
    bank = read(
        repository / "content/courses/cell-biology/question-banks/practice.json"
    )
    question = next(
        item for item in bank["questions"] if item["id"] == "cell-biology-16:chip-percent-input"
    )
    # Percent input = 100 × input aliquot fraction × 2^(Cq_input − Cq_IP).
    independent_value = 100 * 0.01 * (2 ** (25 - 22))
    assert independent_value == 8
    assert question["solution_spec"]["answer"] == independent_value
    assert question["solution_spec"]["unit"] == "%"


def test_graph_expected_mean_is_recalculated_from_source_replicates(repository):
    bank_path = repository / "content/courses/statistics/question-banks/practice.json"
    bank = read(bank_path)
    graph = next(item for item in bank["questions"] if item["type"] == "graph")
    graph["solution_spec"]["points"][0]["y"] = 5.1
    write(bank_path, bank)
    assert "numerical-recalculation" in codes(validate_repository(repository))


def test_graph_coordinate_criteria_must_map_one_to_one(repository):
    bank_path = repository / "content/courses/statistics/question-banks/practice.json"
    bank = read(bank_path)
    graph = next(item for item in bank["questions"] if item["type"] == "graph")
    graph["solution_spec"]["rubric"][0]["id"] = "unknown-coordinate"
    write(bank_path, bank)
    assert "answer-spec" in codes(validate_repository(repository))


def test_graph_coordinate_criteria_cannot_be_whitespace(repository):
    bank_path = repository / "content/courses/statistics/question-banks/practice.json"
    bank = read(bank_path)
    graph = next(item for item in bank["questions"] if item["type"] == "graph")
    graph["solution_spec"]["rubric"][0]["criterion"] = "          "
    write(bank_path, bank)
    assert "answer-spec" in codes(validate_repository(repository))


def test_graph_source_coordinates_must_fit_authored_axes(repository):
    bank_path = repository / "content/courses/statistics/question-banks/practice.json"
    bank = read(bank_path)
    graph = next(item for item in bank["questions"] if item["type"] == "graph")
    graph["graph_spec"]["observations"][0]["x"] = 9
    write(bank_path, bank)
    assert "numerical-recalculation" in codes(validate_repository(repository))


def test_structured_rubric_ids_must_map_one_to_one_to_response_fields(repository, course):
    bank_path = course[0].parent / "question-banks/practice.json"
    bank = read(bank_path)
    question = next(item for item in bank["questions"] if item["type"] == "structured")
    question["solution_spec"]["rubric"][0]["id"] = "unknown-criterion"
    write(bank_path, bank)
    assert "answer-spec" in codes(validate_repository(repository))


def test_structured_rubric_points_must_match_its_response_field(repository, course):
    bank_path = course[0].parent / "question-banks/practice.json"
    bank = read(bank_path)
    question = next(item for item in bank["questions"] if item["type"] == "structured")
    question["solution_spec"]["rubric"][0]["points"] = 0.5
    write(bank_path, bank)
    assert "answer-spec" in codes(validate_repository(repository))


def test_symbolic_assumptions_must_reference_declared_variables(repository, course):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    bank["questions"][0]["type"] = "symbolic"
    bank["questions"][0]["solution_spec"] = {
        "expression": "x + 1",
        "variables": ["x"],
        "assumptions": {"y": {"real": True}},
    }
    write(bank_path, bank)
    assert "answer-spec" in codes(validate_repository(repository))


def test_restricted_production_answer_key_cannot_enter_public_package(
    repository, course
):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    bank["questions"][0]["visibility"] = "restricted-server-assessment"
    write(bank_path, bank)
    assert "restricted-key" in codes(validate_repository(repository))


@pytest.mark.parametrize(
    "reference",
    [
        "../outside.md",
        "../../../outside.md",
        "/etc/passwd",
        "C:/Windows/system.ini",
        "..\\outside.md",
    ],
)
def test_content_paths_cannot_escape_course(repository, course, reference):
    path, manifest = course
    manifest["modules"][0]["lessons"][0]["reading"] = reference
    write(path, manifest)
    assert "path" in codes(validate_repository(repository))


def test_symlink_cannot_expose_host_file(repository, course):
    path, manifest = course
    outside = repository / "outside.md"
    outside.write_text(
        "Host-only file that a reading must not expose.", encoding="utf-8"
    )
    link = path.parent / "modules/escape.md"
    try:
        link.symlink_to(outside)
    except (OSError, NotImplementedError):
        pytest.skip(
            "Symlinks unsupported on this host; Docker dev exercises this check."
        )
    manifest["modules"][0]["lessons"][0]["reading"] = "modules/escape.md"
    write(path, manifest)
    assert "path" in codes(validate_repository(repository))


def test_unknown_prerequisite_fails(repository, course):
    path, manifest = course
    manifest["prerequisites"]["course_ids"] = ["invented-course"]
    write(path, manifest)
    assert "reference" in codes(validate_repository(repository))


def test_dependency_cycle_fails(repository, course):
    path, manifest = course
    manifest["prerequisites"]["course_ids"] = ["genetics"]
    write(path, manifest)
    assert "prerequisite-cycle" in codes(validate_repository(repository))


def test_unknown_objective_and_source_refs_fail(repository, course):
    path, manifest = course
    manifest["modules"][0]["lessons"][0]["objectives"] = ["invented-objective"]
    manifest["modules"][0]["source_ids"] = ["invented-source"]
    write(path, manifest)
    result = validate_repository(repository)
    assert "reference" in codes(result)
    assert any("invented-objective" in error["message"] for error in result.errors)
    assert any("invented-source" in error["message"] for error in result.errors)


def test_week_schedule_references_existing_content(repository, course):
    path, manifest = course
    manifest["duration"]["weeks"] = [
        {
            "week": 1,
            "title": "Experimental reasoning",
            "lesson_ids": ["not-authored"],
            "assessment_ids": ["not-authored"],
        }
    ]
    write(path, manifest)
    assert "reference" in codes(validate_repository(repository))


def test_formative_manifest_cannot_silently_include_a_graded_assignment(repository, course):
    path, manifest = course
    manifest["assessments"][0]["mode"] = "graded"
    write(path, manifest)
    assert "assessment-policy" in codes(validate_repository(repository))


def test_assessment_due_time_cannot_precede_release(repository, course):
    path, manifest = course
    manifest["assessments"][0]["release_at"] = "2026-10-08T00:00:00Z"
    manifest["assessments"][0]["due_at"] = "2026-10-07T00:00:00Z"
    write(path, manifest)
    assert "assessment-policy" in codes(validate_repository(repository))


def test_source_license_is_required(repository):
    registry_path = repository / "content/sources/registry.json"
    registry = read(registry_path)
    del registry["sources"][0]["license"]
    write(registry_path, registry)
    assert "schema" in codes(validate_repository(repository))


def test_comparator_cannot_claim_adaptation_permissions(repository):
    registry_path = repository / "content/sources/registry.json"
    registry = read(registry_path)
    registry["sources"][0]["permissions"]["adaptation"] = True
    write(registry_path, registry)
    assert "source-permissions" in codes(validate_repository(repository))


def test_link_only_research_reference_cannot_claim_reuse_permissions(repository):
    registry_path = repository / "content/sources/registry.json"
    registry = read(registry_path)
    reference = deepcopy(registry["sources"][0])
    reference.update(
        {
            "id": "synthetic-primary-reference",
            "title": "Synthetic primary research reference",
            "institution": "Synthetic journal citation",
            "license": "No reuse license asserted; citation and link only",
            "reuse_mode": "link-only-reference",
            "mapped_courses": [],
            "mapped_modules": [],
        }
    )
    registry["sources"].append(reference)
    write(registry_path, registry)
    assert validate_repository(repository).ok

    registry["sources"][-1]["permissions"]["quotation"] = True
    write(registry_path, registry)
    assert "source-permissions" in codes(validate_repository(repository))


def test_review_record_requires_real_evidence_file(repository, course):
    path, manifest = course
    # Synthetic adversary deliberately references no real approval document.
    manifest["review"] = {
        "status": "external",
        "reviewed_version": manifest["version"],
        "reviewers": [
            {
                "name": "Synthetic test name",
                "qualification": "Synthetic test qualification",
                "reviewed_at": "2026-10-05",
                "evidence": "review/nonexistent-approval.md",
            }
        ],
    }
    write(path, manifest)
    assert "missing-file" in codes(validate_repository(repository))


def test_malformed_manifest_returns_errors_instead_of_crashing(repository, course):
    path, _ = course
    path.write_text('{"id":', encoding="utf-8")
    assert "json" in codes(validate_repository(repository))


def test_nonfinite_numbers_are_not_valid_json_answer_keys(repository, course):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    bank["questions"][2]["solution_spec"]["answer"] = float("nan")
    write(bank_path, bank)
    assert "json" in codes(validate_repository(repository))


def test_csv_numeric_outputs_are_independently_recalculated(repository, course):
    path, _ = course
    bank_path = path.parent / "question-banks/practice.json"
    bank = read(bank_path)
    upload = next(
        item for item in bank["questions"] if item["type"] == "file_upload"
    )
    mean = next(
        item
        for item in upload["solution_spec"]["validation_spec"]["checks"]
        if item["id"] == "vehicle-mean-signal"
    )
    mean["answer"] = 12.5
    write(bank_path, bank)
    assert "numerical-recalculation" in codes(validate_repository(repository))


def test_malformed_retrieval_records_return_errors(repository, course):
    path, _ = course
    cards_path = path.parent / "question-banks/retrieval-cards.json"
    cards = read(cards_path)
    cards["cards"][0] = "not a card object"
    write(cards_path, cards)
    assert {"id", "cards"} <= codes(validate_repository(repository))


def test_duplicate_module_source_maps_fail(repository, course):
    path, _ = course
    source_path = path.parent / "source-map.json"
    mapping = read(source_path)
    mapping["modules"].append(mapping["modules"][0])
    write(source_path, mapping)
    assert "source-map" in codes(validate_repository(repository))


def test_migration_corrections_are_recorded(repository):
    calc = repository / "content/courses/calculus-2/course.json"
    manifest = read(calc)
    assert "0.008/0.8=0.01" in manifest["modules"][1]["lessons"][0]["worked_example"]
    assert manifest["content_origin"]["modifications"]
    organic = read(
        repository / "content/courses/organic-chemistry/question-banks/practice.json"
    )
    assert organic["questions"][2]["options"][0].startswith("Anti-periplanar")
    scaffold = read(
        repository / "content/courses/biomaterials/question-banks/practice.json"
    )
    assert "remaining mass" in scaffold["questions"][1]["prompt"]


def test_week5_imaging_and_fractionation_answers_are_independently_recalculated(repository):
    bank = read(repository / "content/courses/cell-biology/question-banks/practice.json")
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["cell-biology-11:resolution-estimate"]["solution_spec"]["answer"] == round(0.61 * 520 / 1.30, 2)
    assert questions["cell-biology-12:er-marker-recovery"]["solution_spec"]["answer"] == sum((4, 18, 68, 5))


def test_week6_semiconservative_hybrid_fraction_is_independently_recalculated(repository):
    bank = read(repository / "content/courses/cell-biology/question-banks/practice.json")
    questions = {item["id"]: item for item in bank["questions"]}
    # Each hybrid daughter produces one hybrid and one light molecule on the
    # second semiconservative round: 100 * (1 / 2) = 50 percent.
    expected_percent = 100 * (1 / 2)
    question = questions["cell-biology-13:hybrid-fraction"]
    assert question["solution_spec"]["answer"] == expected_percent
    assert question["solution_spec"]["unit"] == "%"
    assert question["solution_spec"]["tolerance"] == 0.5


def test_week9_isoform_fraction_and_protein_half_life_are_recalculated(repository):
    course_root = repository / "content/courses/cell-biology"
    bank = read(course_root / "question-banks/practice.json")
    questions = {item["id"]: item for item in bank["questions"]}

    isoform_answer = round(100 * 60 / (60 + 30), 1)
    isoform = questions["cell-biology-17:isoform-fraction"]
    assert isoform_answer == 66.7
    assert isoform["solution_spec"]["answer"] == isoform_answer
    assert isoform["solution_spec"]["unit"] == "%"
    assert isoform["solution_spec"]["significant_figures"] == 3

    # The synthetic labeled signal falls exactly by one half over four hours.
    estimated_k_deg = -math.log(40 / 80) / 4
    half_life = math.log(2) / estimated_k_deg
    turnover = questions["cell-biology-18:protein-half-life"]
    assert half_life == 4
    assert turnover["solution_spec"]["answer"] == half_life
    assert turnover["solution_spec"]["unit"] == "h"
    assert turnover["solution_spec"]["dimensions"] == {"time": 1}


def test_week9_schedule_objectives_and_practice_are_mapped(repository):
    course_root = repository / "content/courses/cell-biology"
    manifest = read(course_root / "course.json")
    week9 = next(item for item in manifest["duration"]["weeks"] if item["week"] == 9)
    assessment = next(item for item in manifest["assessments"] if item["id"] == "cell-biology-week9-practice")
    bank = read(course_root / assessment["path"])
    questions = {item["id"]: item for item in bank["questions"]}

    assert manifest["maturity"] == "partial"
    assert manifest["version"] == "0.12.0"
    assert week9["lesson_ids"] == ["cell-biology-17", "cell-biology-18"]
    assert week9["assessment_ids"] == [assessment["id"]]
    assert sum(questions[item]["points"] for item in assessment["question_ids"]) == assessment["points"] == 14
    assert set(assessment["objective_ids"]) <= {item["id"] for item in manifest["lesson_objectives"]}
    assert all(
        any(objective_id in questions[item]["objective_ids"] for item in assessment["question_ids"])
        for objective_id in assessment["objective_ids"]
    )
    assert all(questions[item]["visibility"] == "public-practice-authoring" for item in assessment["question_ids"])


def test_week10_inheritance_probability_and_isogenic_ratio_are_recalculated(repository):
    course_root = repository / "content/courses/cell-biology"
    bank = read(course_root / "question-banks/practice.json")
    questions = {item["id"]: item for item in bank["questions"]}

    expected_risk = 100 * (1 / 2) * 0.80
    risk = questions["cell-biology-19:affected-child-risk"]
    assert expected_risk == 40.0
    assert risk["solution_spec"]["answer"] == expected_risk
    assert risk["solution_spec"]["unit"] == "%"

    specific_activity_ratio = 54 / 55
    lesson = (course_root / "modules/09b-variant-mechanism-and-isogenic-evidence.md").read_text(encoding="utf-8")
    assert round(specific_activity_ratio, 2) == 0.98
    assert "54/55 ≈ 0.98" in lesson



def test_week11_occupancy_and_relative_response_are_recalculated(repository):
    course_root = repository / "content/courses/cell-biology"
    bank = read(course_root / "question-banks/practice.json")
    questions = {item["id"]: item for item in bank["questions"]}

    occupancy = 1 / (4 + 1)
    assert occupancy == 0.2
    assert questions["cell-biology-21:occupancy-model"]["solution_spec"]["answer"] == occupancy

    fold_ratio = 36 / 4
    assert fold_ratio == 9
    assert questions["cell-biology-21:relative-response"]["solution_spec"]["answer"] == fold_ratio
    lesson = (course_root / "modules/10b-signaling-dynamics-feedback-and-perturbations.md").read_text(encoding="utf-8")
    assert "5.8 ± 0.7" in lesson and "3.4 ± 0.5" in lesson
