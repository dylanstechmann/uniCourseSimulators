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
    ("statistics", "statistics-7"), ("statistics", "statistics-8"), ("programming", "programming-6"), ("programming", "programming-7"),
    ("geroscience", "geroscience-15"), ("genetics", "genetics-9"), ("biochemistry", "biochemistry-7"), ("physiology", "physiology-7"),
    ("signals-control", "signals-control-6"), ("robotics", "robotics-6"), ("geroscience", "geroscience-16"),
] + [("genetics", f"genetics-{n}") for n in range(10, 16)]


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


def test_programming_code_blocks_keep_python_number_literals():
    text = (COURSES / "programming/modules/07-floating-point-rounding-and-cancellation.md").read_text(encoding="utf-8")
    block = text.split("```python", 1)[1].split("```", 1)[0]
    assert "1e8 + 1" in block and "10⁸" not in block


def test_biomarker_lesson_makes_no_human_anti_aging_claim():
    text = (COURSES / "geroscience/modules/11-biomarker-reliability-and-surrogate-endpoints.md").read_text(encoding="utf-8")
    assert "makes no claim that any intervention changes human aging" in text


def test_geroscience_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("geroscience")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]


def test_geroscience_lab_key_matches_its_dataset():
    import csv
    rows = list(csv.DictReader((COURSES / "geroscience/labs/lifespan-cohort.csv").open(encoding="utf-8")))
    bank = {q["id"]: q for q in json.loads((COURSES / "geroscience/question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank["geroscience-lab1:summary-table"]["solution_spec"]["validation_spec"]["checks"]}
    for group in ("control", "intervention"):
        grips = [float(r["grip_strength_g_day730"]) for r in rows if r["group"] == group and r["grip_strength_g_day730"]]
        assert checks[(group, "animals")] == sum(r["group"] == group for r in rows)
        assert checks[(group, "grip_measured")] == len(grips)
        assert abs(checks[(group, "mean_grip_g")] - sum(grips) / len(grips)) < 1e-9
    treated = sorted((int(r["last_day_observed"]), int(r["died"])) for r in rows if r["group"] == "intervention")
    at_risk, survival, median = len(treated), 1.0, None
    for day, died in treated:
        if died:
            survival *= 1 - 1 / at_risk
            if survival <= 0.5 and median is None:
                median = day
        at_risk -= 1
    assert bank["geroscience-lab1:km-median"]["solution_spec"]["field_specs"][0]["answer"] == median
    text = (COURSES / "geroscience/labs/01-lifespan-cohort-censoring-and-survivor-bias.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any compound or about human aging" in text


def test_genetics_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("genetics")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 16
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    lab_week = next(w for w in weeks if "genetics-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 12 and "genetics-week12-association-lab" in lab_week["assessment_ids"]
    assert "genetics-case" in weeks[-1]["assessment_ids"]


def test_carrier_risk_lesson_gives_no_counselling_advice():
    text = (COURSES / "genetics/modules/11-sex-linkage-pedigrees-and-bayesian-carrier-risk.md").read_text(encoding="utf-8")
    assert "is not genetic-counselling advice for any person" in text
    assert "All families and numbers here are synthetic" in text
    manifest = load("genetics")
    assert any("no genetic-counselling or medical advice" in item for item in manifest["limitations"])


def test_genetics_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "genetics/labs/case-control-genotypes.csv").open(encoding="utf-8")))
    bank = {q["id"]: q for q in json.loads((COURSES / "genetics/question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
    assert len(rows) == 100 and len({r["id"] for r in rows}) == 100
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank["genetics-lab1:stratum-summary"]["solution_spec"]["validation_spec"]["checks"]}
    for ancestry in ("A", "B"):
        for status in ("case", "control"):
            group = [r for r in rows if r["ancestry"] == ancestry and r["status"] == status]
            label = f"{ancestry.lower()}-{status}"
            assert checks[(label, "individuals")] == len(group)
            for variant in ("syn1", "syn2"):
                assert abs(checks[(label, f"mean_dosage_{variant}")] - sum(int(r[variant]) for r in group) / len(group)) < 1e-9

    def table(variant, status, ancestry=None):
        dosage = [int(r[variant]) for r in rows if r["status"] == status and (ancestry is None or r["ancestry"] == ancestry)]
        return sum(dosage), 2 * len(dosage) - sum(dosage)

    def odds_ratio(a, b, c, d):
        return (a / b) / (c / d)

    def chi_square(a, b, c, d):
        n, total = a + b + c + d, 0.0
        for observed, row, col in ((a, a + b, a + c), (b, a + b, b + d), (c, c + d, a + c), (d, c + d, b + d)):
            total += (observed - row * col / n) ** 2 / (row * col / n)
        return total

    pooled = {v: (*table(v, "case"), *table(v, "control")) for v in ("syn1", "syn2", "syn3")}
    interpretation = {f: bank[i]["solution_spec"]["field_specs"][0]["answer"]
                      for f, i in (("or1", "genetics-lab1:pooled-or-syn1"), ("mh2", "genetics-lab1:mh-syn2"))}
    assert interpretation["or1"] == round(odds_ratio(*pooled["syn1"]), 2)
    assert abs(bank["genetics-lab1:chi-square-syn1"]["solution_spec"]["answer"] - chi_square(*pooled["syn1"])) < 1e-3
    assert abs(bank["genetics-lab1:bonferroni"]["solution_spec"]["answer"] - 0.05 / 3) < 1e-4
    for ancestry in ("A", "B"):  # SYN1 is confounded: no association inside either population
        assert abs(odds_ratio(*table("syn1", "case", ancestry), *table("syn1", "control", ancestry)) - 1) < 1e-9
    numerator = denominator = 0.0
    for ancestry in ("A", "B"):
        (a, b), (c, d) = table("syn2", "case", ancestry), table("syn2", "control", ancestry)
        numerator += a * d / (a + b + c + d)
        denominator += b * c / (a + b + c + d)
    assert interpretation["mh2"] == round(numerator / denominator, 2)
    assert abs(numerator / denominator - odds_ratio(*pooled["syn2"])) < 1e-9
    text = (COURSES / "genetics/labs/01-association-study-and-population-structure.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any gene or about human health" in text
