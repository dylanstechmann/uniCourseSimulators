"""Checks for the 2026-10-08 lessons: geroscience 9 to 14, statistics 6, transport 5, bioreactors 5, programming 5,
genetics, biochemistry, physiology and biomaterials 5 and 6, genetics 7 and 8,
and the chemistry, mathematics, biomechanics, physics and engineering lessons added later the same day.

They check structure, labelling and sources, not scientific quality. Passing does not mean any review.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "content" / "courses"
LESSONS = [("geroscience", f"geroscience-{n}") for n in range(9, 15)] + [
    ("statistics", "statistics-6"), ("transport", "transport-5"), ("bioreactors", "bioreactors-5"), ("programming", "programming-5"),
] + [(c, f"{c}-{n}") for c in ("genetics", "biochemistry", "physiology", "biomaterials") for n in (5, 6)] + [("genetics", "genetics-7"), ("genetics", "genetics-8")] + [
    ("general-chemistry-1", "general-chemistry-1-5"), ("general-chemistry-2", "general-chemistry-2-5"), ("general-chemistry-2", "general-chemistry-2-6"),
    ("organic-chemistry", "organic-chemistry-5"), ("calculus-1", "calculus-1-5"), ("calculus-2", "calculus-2-5"),
    ("differential-equations", "differential-equations-5"), ("differential-equations", "differential-equations-6"),
    ("cellular-biomechanics", "cellular-biomechanics-5"), ("cellular-biomechanics", "cellular-biomechanics-6"),
    ("linear-algebra", "linear-algebra-5"), ("linear-algebra", "linear-algebra-6"), ("statics-materials", "statics-materials-5"),
    ("physics-mechanics", "physics-mechanics-5"), ("physics-em", "physics-em-5"), ("circuits", "circuits-5"), ("signals-control", "signals-control-5"),
    ("calculus-3", "calculus-3-5"), ("robotics", "robotics-5"),
    ("bioreactors", "bioreactors-6"), ("transport", "transport-6"), ("calculus-1", "calculus-1-6"), ("calculus-2", "calculus-2-6"),
    ("calculus-3", "calculus-3-6"), ("circuits", "circuits-6"), ("general-chemistry-1", "general-chemistry-1-6"), ("general-chemistry-2", "general-chemistry-2-7"),
    ("organic-chemistry", "organic-chemistry-6"), ("physics-em", "physics-em-6"), ("physics-mechanics", "physics-mechanics-6"), ("statics-materials", "statics-materials-6"),
]


def load(course):
    return json.loads((COURSES / course / "course.json").read_text(encoding="utf-8"))


def lesson_record(course, lesson_id):
    manifest = load(course)
    for module in manifest["modules"]:
        for lesson in module["lessons"]:
            if lesson["id"] == lesson_id:
                return manifest, module, lesson
    raise AssertionError(lesson_id)


@pytest.mark.parametrize("course,lesson_id", LESSONS)
def test_lesson_is_labelled_synthetic_bounded_and_substantial(course, lesson_id):
    _, _, lesson = lesson_record(course, lesson_id)
    text = (COURSES / course / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    assert "synthetic" in text.lower()
    assert "## Limits of this lesson" in text
    assert "## Learning objectives" in text and "## Worked example" in text
    lowered = text.lower()
    for phrase in ("you should take", "we recommend taking", "consult your", "dose of"):
        assert phrase not in lowered, phrase


@pytest.mark.parametrize("course,lesson_id", LESSONS)
def test_objectives_are_linked_to_outcomes_and_assessed(course, lesson_id):
    manifest, _, lesson = lesson_record(course, lesson_id)
    objectives = {o["id"]: o for o in manifest["lesson_objectives"]}
    outcomes = {o["id"] for o in manifest["outcomes"]}
    assert len(lesson["objectives"]) == 3
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"], objective_id
        assert set(objectives[objective_id]["course_outcome_ids"]) <= outcomes
    bank = {q["id"]: q for q in json.loads((COURSES / course / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
    covered = {o for q in lesson["question_ids"] for o in bank[q]["objective_ids"]}
    assert covered == set(lesson["objectives"])
    assert len(lesson["card_ids"]) == 4
    assert len(lesson["question_ids"]) >= 5


def test_new_references_are_link_only_and_dated():
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for course, lesson_id in LESSONS:
        _, module, _ = lesson_record(course, lesson_id)
        for source_id in module["source_ids"]:
            source = registry[source_id]
            assert source["permissions"]["quotation"] is False and source["permissions"]["redistribution"] is False, source_id
            assert source_id in registry
            if source["reuse_mode"] == "link-only-reference" and source.get("accessed_at") == "2026-10-08":
                assert source["url"].startswith("https://pubmed.ncbi.nlm.nih.gov/"), source_id


def test_evidence_tier_lesson_makes_no_human_anti_aging_claim():
    text = (COURSES / "geroscience/modules/10-from-model-to-human-evidence-tiers.md").read_text(encoding="utf-8")
    assert "does not assert that any intervention slows or reverses human aging" in text
    assert "none of its lessons is medical advice" in text
    assert "unproven" in text


def test_geroscience_outcomes_are_now_linked_from_lesson_objectives():
    manifest = load("geroscience")
    linked = {oid for o in manifest["lesson_objectives"] for oid in o["course_outcome_ids"]}
    assert {o["id"] for o in manifest["outcomes"]} <= linked


def test_package_labels_are_unchanged():
    for course in ("geroscience", "statistics"):
        manifest = load(course)
        assert manifest["maturity"] == "partial"
        assert manifest["review"]["status"] == "unreviewed"
        assert manifest["grading_policy"]["mode"] == "formative-only"
