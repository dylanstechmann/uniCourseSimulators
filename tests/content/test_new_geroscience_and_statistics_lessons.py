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
] + [("genetics", f"genetics-{n}") for n in range(10, 16)] + [("physiology", f"physiology-{n}") for n in range(8, 15)] + [("biochemistry", f"biochemistry-{n}") for n in range(8, 14)] + [
    ("statistics", f"statistics-{n}") for n in range(9, 16)] + [("biomaterials", f"biomaterials-{n}") for n in range(7, 14)] + [
    ("bioreactors", f"bioreactors-{n}") for n in range(7, 14)] + [("transport", f"transport-{n}") for n in range(7, 14)] + [
    ("cellular-biomechanics", f"cellular-biomechanics-{n}") for n in range(7, 14)] + [
    ("statics-materials", f"statics-materials-{n}") for n in range(7, 14)] + [
    ("signals-control", f"signals-control-{n}") for n in range(7, 14)] + [
    ("differential-equations", f"differential-equations-{n}") for n in range(7, 14)] + [
    ("linear-algebra", f"linear-algebra-{n}") for n in range(7, 14)]


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


def test_physiology_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("physiology")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 15
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    lab_week = next(w for w in weeks if "physiology-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 13 and "physiology-week13-closure-lab" in lab_week["assessment_ids"]
    assert "physiology-case" in weeks[-1]["assessment_ids"] and "physiology-14" in weeks[-1]["lesson_ids"]


def test_physiology_lessons_give_no_medical_advice():
    manifest = load("physiology")
    assert any("gives no medical advice" in item for item in manifest["limitations"])
    for name, phrase in (("11-respiratory-mechanics-and-gas-exchange.md", "gives no medical advice"),
                         ("14-compensation-and-reserve.md", "does not describe any person or recommend any test or treatment"),
                         ("12-skeletal-muscle-mechanics-and-power.md", "gives no training or medical advice"),
                         ("09-membrane-potential-nernst-and-ghk.md", "gives no medical advice")):
        text = (COURSES / "physiology/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name


def test_physiology_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "physiology/labs/scratch-assay-closure.csv").open(encoding="utf-8")))
    bank = {q["id"]: q for q in json.loads((COURSES / "physiology/question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
    assert len(rows) == 60
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank["physiology-lab1:summary-table"]["solution_spec"]["validation_spec"]["checks"]}

    def open_area(condition, hours):
        return [float(r["open_area_pct"]) for r in rows if r["condition"] == condition and int(r["time_h"]) == hours]

    for condition in ("control", "migration-inhibitor", "division-blocked"):
        assert checks[(condition, "experiments")] == len(open_area(condition, 12)) == 4
        for hours in (12, 24):
            assert abs(checks[(condition, f"mean_open_{hours}h")] - sum(open_area(condition, hours)) / 4) < 1e-9
        assert all(value == 100 for value in open_area(condition, 0))
    control12 = 100 - sum(open_area("control", 12)) / 4
    inhibitor12 = 100 - sum(open_area("migration-inhibitor", 12)) / 4
    block24 = 100 - sum(open_area("division-blocked", 24)) / 4
    control24 = 100 - sum(open_area("control", 24)) / 4
    rate = bank["physiology-lab1:control-rate"]["solution_spec"]["field_specs"][0]["answer"]
    assert rate == float(f"{control12 / 12:.3g}")
    assert abs(bank["physiology-lab1:relative-closure"]["solution_spec"]["answer"] - inhibitor12 / control12) < 1e-3
    assert abs(bank["physiology-lab1:edge-speed"]["solution_spec"]["answer"] - control12 / 100 * 400 / 2 / 12) < 1e-3
    assert abs(bank["physiology-lab1:division-block"]["solution_spec"]["answer"] - block24 / control24) < 1e-3
    text = (COURSES / "physiology/labs/01-scratch-assay-closure-kinetics.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any treatment or about human healing" in text


def test_biochemistry_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("biochemistry")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    lab_week = next(w for w in weeks if "biochemistry-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 7 and "biochemistry-week7-kinetics-lab" in lab_week["assessment_ids"]
    assert "biochemistry-case" in weeks[-1]["assessment_ids"] and "biochemistry-13" in weeks[-1]["lesson_ids"]


def test_biochemistry_package_gives_no_protocols_or_advice():
    manifest = load("biochemistry")
    assert any("gives no laboratory protocols or medical advice" in item for item in manifest["limitations"])
    for name in ("08-amino-acids-charge-and-isoelectric-points.md", "09-protein-folding-and-stability.md",
                 "13-reading-a-metabolic-perturbation.md"):
        text = (COURSES / "biochemistry/modules" / name).read_text(encoding="utf-8")
        assert "gives no laboratory protocol" in text, name


def test_biochemistry_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "biochemistry/labs/enzyme-kinetics-rates.csv").open(encoding="utf-8")))
    bank = {q["id"]: q for q in json.loads((COURSES / "biochemistry/question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
    assert len(rows) == 36
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank["biochemistry-lab1:rate-summary"]["solution_spec"]["validation_spec"]["checks"]}

    def rate_values(condition, substrate):
        return [float(r["rate_um_per_min"]) for r in rows if r["condition"] == condition and float(r["substrate_um"]) == substrate]

    for condition in ("control", "inhibitor"):
        assert checks[(condition, "replicates")] == len(rate_values(condition, 5)) == 3
        for substrate in (1, 5, 20, 50):
            values = rate_values(condition, substrate)
            assert abs(checks[(condition, f"mean_v_{substrate}um")] - sum(values) / len(values)) < 1e-4
    text = (COURSES / "biochemistry/labs/01-enzyme-kinetics-and-inhibition-from-data.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any compound or any cell" in text
    vmax = bank["biochemistry-lab1:control-fit"]["solution_spec"]["field_specs"][0]
    assert vmax["significant_figures"] == 4


def test_statistics_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("statistics")
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
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"statistics-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"statistics-1": 1, "statistics-2": 4, "statistics-3": 6, "statistics-4": 8}
    lab_week = next(w for w in weeks if "statistics-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 12 and "statistics-week12-nested-design-lab" in lab_week["assessment_ids"]
    assert "statistics-case" in weeks[-1]["assessment_ids"] and "statistics-15" in weeks[-1]["lesson_ids"]


def test_statistics_package_gives_no_protocols_or_advice():
    manifest = load("statistics")
    assert any("gives no laboratory protocols or medical advice" in item for item in manifest["limitations"])
    text = (COURSES / "statistics/modules/15-planning-a-confirmatory-study.md").read_text(encoding="utf-8")
    assert "not guidance for any real study or for any person or animal" in text
    syllabus = (COURSES / "statistics/syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.4.0." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"]) and len(manifest["outcomes"]) == 5


def test_statistics_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "statistics/labs/nested-biomarker-readings.csv").open(encoding="utf-8")))
    bank = {q["id"]: q for q in json.loads((COURSES / "statistics/question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
    assert len(rows) == 24
    checks = {(c["row_id"], c["column"]): c["answer"] for c in bank["statistics-lab1:animal-summary"]["solution_spec"]["validation_spec"]["checks"]}
    animals = sorted({r["animal_id"] for r in rows})
    assert animals == ["c1", "c2", "c3", "c4", "t1", "t2", "t3", "t4"] and len(checks) == 2 * len(animals)
    for animal in animals:
        values = [float(r["value_au"]) for r in rows if r["animal_id"] == animal]
        assert checks[(animal, "readings")] == len(values) == 3
        assert abs(checks[(animal, "mean_value")] - sum(values) / len(values)) < 1e-4
    text = (COURSES / "statistics/labs/01-pseudoreplication-and-nested-designs.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any compound or any organism" in text


def test_biomaterials_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("biomaterials")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"biomaterials-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"biomaterials-1": 1, "biomaterials-2": 3, "biomaterials-3": 9, "biomaterials-4": 13}
    lab_week = next(w for w in weeks if "biomaterials-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 12 and "biomaterials-week12-degradation-lab" in lab_week["assessment_ids"]
    assert "biomaterials-case" in weeks[-1]["assessment_ids"] and "biomaterials-13" in weeks[-1]["lesson_ids"]


def test_biomaterials_package_gives_no_protocols_or_advice_and_no_efficacy_claim():
    manifest = load("biomaterials")
    assert any("gives no laboratory protocols or medical advice" in item for item in manifest["limitations"])
    limits = {
        "11-biocompatibility-evidence-and-the-unit-of-analysis.md": "says nothing about the response of any real material in any animal or person",
        "12-cells-for-a-scaffold-seeding-and-expansion.md": "Nothing here is a protocol or a claim about any real cell type or tissue",
        "13-reading-a-failure-in-a-degrading-vascular-scaffold.md": "not a protocol, a safety plan or a statement about any real device or person",
    }
    for name, phrase in limits.items():
        text = (COURSES / "biomaterials/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name
    syllabus = (COURSES / "biomaterials/syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.3.0." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"])


def test_biomaterials_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "biomaterials/labs/scaffold-degradation-time-course.csv").open(encoding="utf-8")))
    assert len(rows) == 21 and {int(r["specimen"]) for r in rows} == {1, 2, 3}
    text = (COURSES / "biomaterials/labs/01-degradation-time-course-of-a-synthetic-scaffold.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any material or implant" in text
    assert "values slightly above 100 reflect weighing variability" in text


def test_bioreactors_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("bioreactors")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"bioreactors-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"bioreactors-1": 1, "bioreactors-2": 5, "bioreactors-3": 9, "bioreactors-4": 12}
    lab_week = next(w for w in weeks if "bioreactors-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 7 and "bioreactors-week7-kla-lab" in lab_week["assessment_ids"]
    assert "bioreactors-case" in weeks[-1]["assessment_ids"] and "bioreactors-13" in weeks[-1]["lesson_ids"]


def test_bioreactors_package_gives_no_protocols_recipes_or_advice():
    manifest = load("bioreactors")
    assert any("gives no laboratory protocols, process recipes or medical advice" in item for item in manifest["limitations"])
    limits = {
        "07-growth-kinetics-monod-and-yield.md": "The lesson says nothing about any real cell line or process",
        "08-continuous-culture-washout-and-perfusion.md": "Nothing here is a protocol or a statement about any real cell line",
        "10-shear-eddies-and-cell-damage.md": "Nothing here is a design or a statement about any real cell line",
        "13-designing-a-scale-down-experiment.md": "not a protocol, a validation plan or a statement about any real process",
    }
    for name, phrase in limits.items():
        text = (COURSES / "bioreactors/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name
    syllabus = (COURSES / "bioreactors/syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.4.0." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"])


def test_bioreactors_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "bioreactors/labs/gassing-out-do-curves.csv").open(encoding="utf-8")))
    assert len(rows) == 63 and {int(r["run"]) for r in rows} == {1, 2, 3}
    text = (COURSES / "bioreactors/labs/01-measuring-kla-by-dynamic-gassing-out.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any culture or process" in text
    assert "describes the logic of the method, not an operating procedure" in text


def test_transport_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("transport")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"transport-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"transport-1": 1, "transport-2": 3, "transport-3": 9, "transport-4": 12}
    lab_week = next(w for w in weeks if "transport-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 8 and "transport-week8-oxygen-profile-lab" in lab_week["assessment_ids"]
    assert "transport-case" in weeks[-1]["assessment_ids"] and "transport-13" in weeks[-1]["lesson_ids"]


def test_transport_package_gives_no_protocols_or_handling_procedures():
    manifest = load("transport")
    assert any("gives no laboratory protocols, handling procedures or medical advice" in item for item in manifest["limitations"])
    limits = {
        "07-transient-diffusion-and-the-error-function.md": "Nothing here is a protocol or a statement about any real solute",
        "08-advection-diffusion-and-the-peclet-number.md": "Nothing here is a design for any device",
        "09-oxygen-in-a-spheroid-and-the-anoxic-core.md": "Nothing here is a protocol or a statement about any real aggregate",
        "11-heat-transfer-lumped-capacitance-and-the-biot-number.md": "Nothing here is a protocol for warming, cooling, freezing or thawing any sample",
        "13-perfused-construct-with-a-hypoxic-center.md": "not a protocol, and nothing here is a statement about any real device",
    }
    for name, phrase in limits.items():
        text = (COURSES / "transport/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name
    syllabus = (COURSES / "transport/syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.4.0." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"])


def test_transport_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "transport/labs/oxygen-depth-profiles.csv").open(encoding="utf-8")))
    assert len(rows) == 81 and {int(r["replicate"]) for r in rows} == {1, 2, 3}
    text = (COURSES / "transport/labs/01-oxygen-depth-profiles-in-cell-laden-slabs.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any construct or cell" in text
    assert "describes the logic of the measurement, not an operating procedure" in text


def test_cellular_biomechanics_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("cellular-biomechanics")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"cellular-biomechanics-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"cellular-biomechanics-1": 1, "cellular-biomechanics-2": 5, "cellular-biomechanics-3": 8, "cellular-biomechanics-4": 10}
    lab_week = next(w for w in weeks if "cellular-biomechanics-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 13 and "cellular-biomechanics-week13-stiffness-ligand-lab" in lab_week["assessment_ids"]
    assert "cellular-biomechanics-case" in weeks[-1]["assessment_ids"] and "cellular-biomechanics-13" in weeks[-1]["lesson_ids"]


def test_cellular_biomechanics_package_gives_no_protocols_or_handling_procedures():
    manifest = load("cellular-biomechanics")
    assert any("gives no laboratory protocols, handling procedures or medical advice" in item for item in manifest["limitations"])
    limits = {
        "07-oscillatory-rheology-storage-and-loss-moduli.md": "Nothing here is a measurement of any real gel or cell",
        "08-traction-forces-from-micropillars.md": "Nothing here is a measurement of any real cell or array",
        "09-bonds-under-force-and-the-molecular-clutch.md": "is not a quantitative model of any real adhesion or cell",
        "10-cortical-tension-and-micropipette-aspiration.md": "the numbers are not measurements of any real cell",
        "11-dose-response-to-stiffness-and-the-hill-function.md": "Nothing here is a statement about any real cell, gel or marker",
        "12-applying-strain-to-cells.md": "Nothing here is a protocol for stretching cells",
        "13-decoupling-stiffness-from-ligand-density.md": "The design is an outline of how to reason, not a protocol",
    }
    for name, phrase in limits.items():
        text = (COURSES / "cellular-biomechanics/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name
    syllabus = (COURSES / "cellular-biomechanics/syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.3.0." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"])


def test_cellular_biomechanics_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "cellular-biomechanics/labs/stiffness-ligand-marker-expression.csv").open(encoding="utf-8")))
    assert len(rows) == 180 and {int(r["gel"]) for r in rows} == {1, 2, 3}
    text = (COURSES / "cellular-biomechanics/labs/01-stiffness-ligand-density-and-the-unit-of-analysis.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any cell type or material" in text


def test_statics_materials_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("statics-materials")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"statics-materials-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"statics-materials-1": 1, "statics-materials-2": 3, "statics-materials-3": 4, "statics-materials-4": 8}
    lab_week = next(w for w in weeks if "statics-materials-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 12 and "statics-materials-week12-fatigue-lab" in lab_week["assessment_ids"]
    assert "statics-materials-case" in weeks[-1]["assessment_ids"] and "statics-materials-13" in weeks[-1]["lesson_ids"]
    # the fatigue lesson comes before the lab that uses it, and the capstone comes after the lessons it draws on
    order = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"]}
    assert order["statics-materials-8"] < order["statics-materials-lab-01"] < order["statics-materials-13"]


def test_statics_materials_package_gives_no_design_basis_or_test_protocol():
    manifest = load("statics-materials")
    assert any("gives no design basis, test protocol or safety advice" in item for item in manifest["limitations"])
    limits = {
        "07-stress-concentrations-holes-and-notches.md": "Nothing here is a design check for any part",
        "08-fatigue-sn-curves-and-cumulative-damage.md": "Nothing here is a design check for any part",
        "09-buckling-of-slender-struts.md": "Nothing in this lesson is a design check for any device or structure",
        "10-principal-stresses-mohrs-circle-and-yield.md": "is not a statement about the safety of any device or person",
        "11-beam-deflection-and-flexural-modulus.md": "is not a test method for any real material",
        "12-weibull-strength-and-the-size-effect.md": "Nothing here is a design basis for any device",
        "13-cyclic-perfusion-failure-analysis-and-test-plan.md": "not a laboratory protocol or a design basis for any device",
    }
    for name, phrase in limits.items():
        text = (COURSES / "statics-materials/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name
    syllabus = (COURSES / "statics-materials/syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.4.0." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"])


def test_statics_materials_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "statics-materials/labs/fatigue-lives-by-stress-amplitude.csv").open(encoding="utf-8")))
    assert len(rows) == 20 and {int(r["specimen"]) for r in rows} == {1, 2, 3, 4, 5}
    assert {r["status"] for r in rows} == {"failed", "runout"}
    text = (COURSES / "statics-materials/labs/01-fatigue-lives-scatter-and-run-outs.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any device" in text


def test_signals_control_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("signals-control")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"signals-control-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"signals-control-1": 1, "signals-control-2": 4, "signals-control-3": 8, "signals-control-4": 12}
    lab_week = next(w for w in weeks if "signals-control-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 11 and "signals-control-week11-identification-lab" in lab_week["assessment_ids"]
    assert "signals-control-case" in weeks[-1]["assessment_ids"] and "signals-control-13" in weeks[-1]["lesson_ids"]
    # prerequisites come first: poles before Bode plots, margins before PI tuning, PI tuning before the lab and the capstone
    order = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"]}
    assert order["signals-control-7"] < order["signals-control-9"] < order["signals-control-10"] < order["signals-control-11"] < order["signals-control-lab-01"] < order["signals-control-13"]


def test_signals_control_package_gives_no_controller_settings_or_protocols():
    manifest = load("signals-control")
    assert any("gives no controller settings, safety procedures or test protocols for any real device" in item for item in manifest["limitations"])
    limits = {
        "07-laplace-transforms-poles-zeros-and-the-final-value.md": "Limits of this lesson",
        "08-second-order-systems-damping-and-overshoot.md": "a real measuring line must be tested",
        "09-bode-plots-decibels-phase-and-delay.md": "the Bode plot of a real system must be measured, not assumed",
        "10-stability-margins-gain-phase-and-delay.md": "plants with unstable poles, several crossovers or a changing delay need the full Nyquist criterion",
        "11-pi-control-tuning-and-integrator-windup.md": "real loops need a measured model, a check of the margins and a test of the saturation behavior",
        "12-sampling-aliasing-and-discrete-pi-control.md": "the ten-per-time-constant rule is a rule of thumb",
        "13-sensor-filter-phase-lag-and-safe-retuning.md": "not a procedure for any real incubator or process, whose limits, alarms and safety interlocks come first",
    }
    for name, phrase in limits.items():
        text = (COURSES / "signals-control/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name
    syllabus = (COURSES / "signals-control/syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.4.0." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"])


def test_signals_control_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "signals-control/labs/incubator-step-tests.csv").open(encoding="utf-8")))
    assert len(rows) == 366 and {int(r["run"]) for r in rows} == {1, 2}
    assert {r["power_w"] for r in rows} == {"10", "20", "30"}
    text = (COURSES / "signals-control/labs/01-identifying-an-incubator-from-step-tests.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any device" in text


def test_differential_equations_schedule_places_every_lesson_once_and_stays_partial():
    manifest = load("differential-equations")
    weeks = manifest["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    scheduled = [lesson for w in weeks for lesson in w["lesson_ids"]]
    all_lessons = [lesson["id"] for m in manifest["modules"] for lesson in m["lessons"]]
    assert len(all_lessons) == 14
    assert sorted(scheduled) == sorted(all_lessons) and len(scheduled) == len(set(scheduled))
    assessments = {a["id"]: a for a in manifest["assessments"]}
    assert all(a in assessments for w in weeks for a in w["assessment_ids"])
    assert all(a["mode"] != "graded" for a in manifest["assessments"])
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert "not evidence of semester equivalence" in manifest["duration"]["equivalent_structure"]
    prototype_weeks = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"] if lesson in {f"differential-equations-{n}" for n in range(1, 5)}}
    assert prototype_weeks == {"differential-equations-1": 1, "differential-equations-2": 4, "differential-equations-3": 6, "differential-equations-4": 11}
    lab_week = next(w for w in weeks if "differential-equations-lab-01" in w["lesson_ids"])
    assert lab_week["week"] == 13 and "differential-equations-week13-fitting-lab" in lab_week["assessment_ids"]
    assert "differential-equations-case" in weeks[-1]["assessment_ids"] and "differential-equations-13" in weeks[-1]["lesson_ids"]
    # prerequisites come first: linear flows before the toggle switch, numerical ODEs and stiffness before the lab and capstone
    order = {lesson: w["week"] for w in weeks for lesson in w["lesson_ids"]}
    assert order["differential-equations-9"] < order["differential-equations-11"] < order["differential-equations-lab-01"] < order["differential-equations-13"]
    assert order["differential-equations-4"] < order["differential-equations-12"] < order["differential-equations-13"]


def test_differential_equations_package_gives_no_protocols_or_parameter_values_for_real_organisms():
    manifest = load("differential-equations")
    assert any("gives no experimental protocols, parameter values for any real organism or process, or safety advice" in item for item in manifest["limitations"])
    limits = {
        "07-forced-first-order-systems-in-a-perfused-chamber.md": "the amplitude and lag formulas hold only after the transient has decayed",
        "08-resonance-and-damping-of-a-spring-mass-damper.md": "the amplitude formulas hold only in steady state",
        "09-phase-portraits-of-linear-systems.md": "a linear portrait describes a nonlinear system only near an equilibrium",
        "10-logistic-growth-solution-fitting-and-extrapolation.md": "The logistic equation is a minimal model",
        "11-linearization-and-bistability-in-a-toggle-switch.md": "a stable state of a deterministic model is not a prediction about any real cell",
        "12-stiff-equations-and-implicit-methods.md": "the stiffness ratio is only a guide",
        "13-negative-counts-model-structure-step-size-and-validation.md": "the validation list is a minimum, not a protocol for any real experiment",
    }
    for name, phrase in limits.items():
        text = (COURSES / "differential-equations/modules" / name).read_text(encoding="utf-8")
        assert phrase in text, name
    syllabus = (COURSES / "differential-equations/syllabus.md").read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus and "Proposed 14-week schedule" in syllabus
    assert all(f"- {outcome['description']}" in syllabus for outcome in manifest["outcomes"])


def test_differential_equations_lab_keys_match_the_dataset_and_the_lab_is_labelled_synthetic():
    import csv
    rows = list(csv.DictReader((COURSES / "differential-equations/labs/cell-counts-after-growth-factor-removal.csv").open(encoding="utf-8")))
    assert len(rows) == 21 and {int(r["hours"]) for r in rows} == {0, 6, 12, 18, 24, 36, 48}
    text = (COURSES / "differential-equations/labs/01-fitting-decay-models-and-testing-them-beyond-the-window.md").read_text(encoding="utf-8")
    assert "nothing here is evidence about any culture" in text
