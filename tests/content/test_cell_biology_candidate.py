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
    params=sorted((COURSE / "assessment-specs").glob("*-candidate.json")),
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
    if "case_id" in rows[0]:
        assert {r["form"] for r in rows} == {"A", "B"}
        assert all(math.isfinite(float(r["value"])) for r in rows)
        assert len({(r["case_id"], r["form"], r["metric"]) for r in rows}) == len(rows)
        for row in rows:
            assert row["case_id"] and row["metric"] and row["unit"]
        return
    if "clone" in rows[0]:
        assert len(rows) == 24
        groups = {}
        for row in rows:
            groups.setdefault(row["clone"], []).append(row)
            assert 0 < float(row["recovery_fraction"]) <= 1
            assert float(row["viable_cells_thousands"]) > 0
            assert float(row["protein_signal_ug"]) > float(row["protein_background_ug"])
            assert float(row["activity_signal_nmol_min"]) > float(
                row["activity_background_nmol_min"]
            )
            assert (
                0
                <= int(row["response_positive_cells"])
                <= int(row["response_cells_assayed"])
            )
        assert len(groups) == 12 and all(len(v) == 2 for v in groups.values())
        return
    if "original_area_mm2" in rows[0]:
        assert len(rows) == 24
        groups = {}
        for row in rows:
            groups.setdefault(row["preparation"], []).append(row)
            assert all(
                float(row[k]) > 0
                for k in ("original_area_mm2", "initial_length_mm", "extension_mm")
            )
            assert float(row["force_signal_n"]) > float(row["force_background_n"])
            assert (
                0
                <= int(row["nuclear_marker_positive_cells"])
                <= int(row["viable_attached_cells"])
                <= int(row["seeded_cells"])
            )
        assert len(groups) == 4 and all(len(v) == 6 for v in groups.values())
        return
    if "viable_singlets" in rows[0]:
        assert len(rows) == 36
        groups = {}
        for row in rows:
            groups.setdefault(row["culture"], []).append(row)
            live = int(row["viable_singlets"])
            assert live > 0 and live <= int(row["all_recovered_cells"])
            assert (
                sum(
                    int(row[k]) for k in ("dna_2n_cells", "dna_s_cells", "dna_4n_cells")
                )
                == live
            )
            assert all(
                0 <= int(row[k]) <= live
                for k in (
                    "edu_positive_viable",
                    "p21_high_viable",
                    "beta_gal_high_viable",
                    "mitotic_marker_positive_viable",
                )
            )
            assert (
                0
                <= int(row["caspase_positive_all_recovered"])
                <= int(row["all_recovered_cells"])
            )
        assert len(groups) == 12
        assert all(
            {int(row["time_h"]) for row in v} == {0, 24, 72} for v in groups.values()
        )
        return
    if "rna_spike_input_eq" in rows[0]:
        assert len(rows) == 12 and len({row["culture"] for row in rows}) == 12
        for row in rows:
            assert float(row["viable_cells_thousands"]) > 0
            assert (
                0
                < float(row["rna_spike_recovered_eq"])
                <= float(row["rna_spike_input_eq"])
            )
            for channel in ("included", "skipped", "shared", "precursor"):
                assert float(row[f"{channel}_signal_eq"]) > float(
                    row[f"{channel}_background_eq"]
                )
        with (COURSE / CANDIDATE["additional_dataset_paths"][0]).open(
            newline=""
        ) as stream:
            chase = list(csv.DictReader(stream))
        assert len(chase) == 48
        assert {row["culture"] for row in chase} == {row["culture"] for row in rows}
        for culture in {row["culture"] for row in rows}:
            assert {
                float(row["time_h"]) for row in chase if row["culture"] == culture
            } == {0, 2, 4, 6}
        for row in chase:
            assert float(row["recovery_reference_au"]) > 0
            assert float(row["labeled_target_signal_au"]) > float(
                row["labeled_target_background_au"]
            )
        return
    if "amplification_factor" in rows[0]:
        assert len(rows) == 72
        groups = {}
        for row in rows:
            groups.setdefault((row["culture"], row["locus"]), []).append(row)
            assert 0 < float(row["input_fraction"]) <= 1
            assert 1 < float(row["amplification_factor"]) <= 2
            assert all(
                math.isfinite(float(row[key]))
                for key in ("cq_input", "cq_specific", "cq_igg")
            )
        assert len(groups) == 36
        for observations in groups.values():
            assert {row["technical_well"] for row in observations} == {"1", "2"}
            assert (
                len(
                    {
                        (
                            row["condition"],
                            row["input_fraction"],
                            row["amplification_factor"],
                        )
                        for row in observations
                    }
                )
                == 1
            )
        assert len(CANDIDATE["additional_dataset_paths"]) == 1
        with (COURSE / CANDIDATE["additional_dataset_paths"][0]).open(
            newline=""
        ) as stream:
            reporters = list(csv.DictReader(stream))
        assert len(reporters) == 12
        assert len({row["preparation"] for row in reporters}) == 12
        assert not {row["preparation"] for row in reporters}.intersection(
            row["culture"] for row in rows
        )
        for row in reporters:
            for construct in ("promoter", "wt", "mutant", "positive"):
                for channel in ("firefly", "renilla"):
                    assert float(row[f"{construct}_{channel}_au"]) > float(
                        row[f"{construct}_{channel}_background_au"]
                    )
        return
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
    assert "inactive candidate" in text.lower()
    assert "workload has not been measured" in text.lower()
    assert "no live submission route" in text.lower()
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


def test_authored_variants_remain_answer_free_and_field_mappings_are_complete(
    candidate,
):
    if "variant_questions" not in candidate:
        return
    questions = {q["id"]: q for q in candidate["questions"]}
    assert set(candidate["variant_questions"]) == set(questions)
    forbidden = {
        "solution_spec",
        "answer",
        "field_specs",
        "feedback",
        "rubric",
        "checks",
    }
    assert not forbidden.intersection(nested_keys(candidate["variant_questions"]))
    for key, variant in candidate["variant_questions"].items():
        assert variant["variant_id"] == "form-b"
        assert variant["prompt"] != questions[key]["prompt"]
        assert variant["response_fields"] == questions[key]["response_fields"]
        assert variant["prompt"] in (COURSE / candidate["instruction_path"]).read_text()
    mappings = candidate["objective_evidence"]
    assert {(r["question_id"], r["field_id"]) for r in mappings} == {
        (q["id"], f["id"]) for q in questions.values() for f in q["response_fields"]
    }
    assert {o for r in mappings for o in r["objective_ids"]} == set(
        candidate["objective_ids"]
    )
    assert sum(r["points"] for r in mappings) == candidate["points"]
    for row in mappings:
        field = next(
            f
            for f in questions[row["question_id"]]["response_fields"]
            if f["id"] == row["field_id"]
        )
        assert row["points"] == field["points"]
