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
    source_ids = sorted(
        {
            source
            for path in (tmp_path / "content/courses").glob("*/course.json")
            for module in read(path)["modules"]
            for source in module["source_ids"]
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
        "lessons": 100,
        "questions": 101,
        "cards": 200,
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
