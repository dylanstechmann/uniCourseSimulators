#!/usr/bin/env python3
"""Authoring adversaries: a valid inventory must not become a fabricated full course."""

from __future__ import annotations

import json
import shutil
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
        "lessons": 101,
        "questions": 106,
        "cards": 203,
        "cases": 25,
    }
    assert sum(warning["code"] == "legacy-depth" for warning in result.warnings) == 100
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
    assert manifest["version"] == "0.3.2"
    assert manifest["maturity"] == "partial"
    assert result.inventory["questions"] == 106
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
    assert result.inventory["questions"] == 106


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
