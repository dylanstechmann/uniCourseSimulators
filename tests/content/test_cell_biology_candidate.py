"""Public inactive-candidate integrity; no protected answers belong in these tests."""

import csv
import hashlib
import json
import math
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cell-biology"
MANIFEST = json.loads((COURSE / "course.json").read_text())


@pytest.fixture(
    params=sorted((COURSE / "assessment-specs").glob("homework-??-candidate.json")),
    ids=lambda path: path.stem,
)
def candidate(request):
    return json.loads(request.param.read_text())


def nested_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from nested_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from nested_keys(item)


def test_candidate_is_version_bound_and_blocked_on_real_review(candidate):
    CANDIDATE = candidate
    assert CANDIDATE["content_version"] in {
        entry["version"] for entry in MANIFEST["history"]
    }
    assert tuple(map(int, CANDIDATE["content_version"].split("."))) <= tuple(
        map(int, MANIFEST["version"].split("."))
    )
    for name, digest in CANDIDATE.get("prerequisite_sha256", {}).items():
        assert hashlib.sha256((COURSE / name).read_bytes()).hexdigest() == digest
    assert CANDIDATE["state"] == "inactive-review-candidate"
    assert CANDIDATE["review"] == {"status": "unreviewed", "reviewers": []}
    assert {
        "independent-recalculation",
        "subject-matter-review",
        "assessment-review",
        "accessibility-review",
        "measured-workload",
        "operator-provisioning-and-release-policy",
    }.issubset(CANDIDATE["activation_gates"])
    assert re.fullmatch(r"[a-f0-9]{64}", CANDIDATE["private_source_sha256"])
    assert CANDIDATE["private_source_ref"].startswith("private://assignments/")


def test_public_candidate_has_only_answer_free_item_fields(candidate):
    CANDIDATE = candidate
    assert not {
        "solution_spec",
        "answer",
        "feedback",
        "field_specs",
        "rubric",
        "checks",
    }.intersection(nested_keys(CANDIDATE["questions"]))
    allowed = {
        "id",
        "type",
        "prompt",
        "options",
        "unit",
        "significant_figures",
        "points",
        "selection",
        "partial_credit_policy",
        "response_fields",
        "graph_spec",
        "accepted_media_types",
        "max_upload_bytes",
        "variant_id",
        "variant_token",
        "learning_objective_ids",
        "assessment_role",
    }
    questions = CANDIDATE["questions"]
    assert len({q["id"] for q in questions}) == len(questions)
    assert sum(q["points"] for q in questions) == CANDIDATE["points"]
    assert all(set(q) <= allowed for q in questions)


def test_candidate_maps_to_existing_instruction_and_actual_outcome_links(candidate):
    CANDIDATE = candidate
    lessons = {
        lesson["id"] for module in MANIFEST["modules"] for lesson in module["lessons"]
    }
    objectives = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
    assert set(CANDIDATE["lesson_ids"]) <= lessons
    assert set(CANDIDATE["objective_ids"]) <= set(objectives)
    expected = {
        outcome
        for key in CANDIDATE["objective_ids"]
        for outcome in objectives[key].get("course_outcome_ids", [])
    }
    assert set(CANDIDATE["course_outcome_ids"]) == expected
    assert all(
        set(q["learning_objective_ids"]) <= set(CANDIDATE["objective_ids"])
        for q in CANDIDATE["questions"]
    )


def test_public_data_keep_observation_units_and_series_consistent(candidate):
    CANDIDATE = candidate
    with (COURSE / CANDIDATE["dataset_path"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    if "dna_reference_au" in rows[0]:
        assert len(rows) == 36
        groups = {}
        for row in rows:
            groups.setdefault(row["culture"], []).append(row)
            assert float(row["dna_reference_au"]) > 0
            assert float(row["lesion_signal_au"]) >= float(row["lesion_background_au"])
            assert float(row["loaded_dna_ng"]) > 0
            assert float(row["viable_cells_thousands"]) >= 0
            assert 0 <= float(row["dna_synthesis_label_pct"]) <= 100
        assert len(groups) == 12
        for observations in groups.values():
            assert {float(row["time_h"]) for row in observations} == {0, 2, 6}
            assert len({row["condition"] for row in observations}) == 1
        return
    if "series" in rows[0]:
        assert len(rows) == 420
        assert len({tuple(row.values())[:-1] for row in rows}) == len(rows)
        blocks = {}
        for row in rows:
            assert math.isfinite(float(row["signal_au"]))
            blocks.setdefault((row["day"], row["condition"]), []).append(row)
        assert len(blocks) == 12
        for observations in blocks.values():
            standards = [row for row in observations if row["series"] == "standard"]
            assert {float(row["product_standard_nm"]) for row in standards} == {
                0,
                500,
                1000,
            }
            for series in ("blank", "reaction"):
                selected = [row for row in observations if row["series"] == series]
                assert len(selected) == 16
                assert {float(row["substrate_um"]) for row in selected} == {
                    5,
                    15,
                    45,
                    135,
                }
                assert {float(row["time_s"]) for row in selected} == {0, 2, 4, 10}
        return
    groups = {}
    for row in rows:
        groups.setdefault(row["preparation"], []).append(row)
        amounts = [
            float(row[key])
            for key in (
                "lysosome_intact_nmol",
                "medium_intact_nmol",
                "other_intact_nmol",
                "fragments_nmol",
            )
        ]
        assert all(value >= 0 for value in amounts)
        assert sum(amounts) <= float(row["pulse_input_nmol"])
    assert len(rows) == 36 and len(groups) == 12
    for observations in groups.values():
        assert {int(r["chase_min"]) for r in observations} == {0, 30, 90}
        assert len({r["condition"] for r in observations}) == 1
        assert len({r["pulse_input_nmol"] for r in observations}) == 1


def test_handout_contains_all_stems_fields_and_explicit_inactive_scope(candidate):
    CANDIDATE = candidate
    text = (COURSE / CANDIDATE["instruction_path"]).read_text()
    assert "inactive candidate" in text
    assert "workload has not been measured" in text
    assert "no live submission route" in text
    for question in CANDIDATE["questions"]:
        assert question["prompt"] in text
        for option in question["options"]:
            assert option in text
        for field in question["response_fields"]:
            assert field["prompt"] in text
            assert all(option in text for option in field["options"])


def test_candidate_does_not_activate_any_catalog_grade_or_private_source(candidate):
    CANDIDATE = candidate
    assert CANDIDATE["candidate_id"] not in {a["id"] for a in MANIFEST["assessments"]}
    for path in (ROOT / "content/courses").glob("*/course.json"):
        course = json.loads(path.read_text())
        assert course["maturity"] == "partial"
        assert course["review"]["status"] == "unreviewed"
        assert course["grading_policy"]["mode"] == "formative-only"
        assert all(a["mode"] != "graded" for a in course["assessments"])
        assert all(
            not a["path"].startswith("private://") for a in course["assessments"]
        )
