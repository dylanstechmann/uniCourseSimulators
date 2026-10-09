"""Candidate audit rejects drift and public-key leaks, without reading private banks."""

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("candidate_audit", ROOT / "tools/assessment_candidates.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@pytest.fixture
def packet(tmp_path):
    course = tmp_path / "content/courses/example"
    folder = course / "assessment-specs"
    folder.mkdir(parents=True)
    (folder / "instructions.md").write_text("Inactive original draft.")
    (folder / "data.csv").write_text("culture,value\na,12\n")
    manifest = {
        "id": "example", "version": "1", "maturity": "partial", "review": {"status": "unreviewed"},
        "grading_policy": {"mode": "formative-only"}, "assessments": [], "history": [{"version": "1"}],
        "lesson_objectives": [{"id": "objective"}],
    }
    candidate = {
        "candidate_id": "draft", "course_id": "example", "content_version": "1",
        "state": "inactive-review-candidate", "objective_ids": ["objective"], "points": 2,
        "questions": [{"id": "question", "points": 2}], "review": {"status": "unreviewed"},
        "instruction_path": "assessment-specs/instructions.md", "dataset_path": "assessment-specs/data.csv",
        "activation_gates": ["subject-matter-review", "measured-workload"],
    }
    (course / "course.json").write_text(json.dumps(manifest))
    path = folder / "homework-candidate.json"
    path.write_text(json.dumps(candidate))
    return tmp_path, course, path, candidate


def test_real_report_is_current_and_does_not_open_private_stores():
    report = MODULE.audit(ROOT)
    assert len(report["packages"]) == 25
    assert sum(len(p["candidates"]) for p in report["packages"]) == 14
    assert MODULE.render(report) == (ROOT / "docs/ASSESSMENT_CANDIDATE_REPORT.md").read_text()
    assert "private_source_ref" not in json.dumps(report)
    assert report["evidence_scope"] == "public-authoring-artifact-audit-only"


def test_file_hashes_change_without_granting_review(packet):
    root, course, path, candidate = packet
    before = MODULE.audit(root)
    (course / "assessment-specs/data.csv").write_text("culture,value\na,13\n")
    after = MODULE.audit(root)
    assert before != after
    candidate["review"]["status"] = "externally-reviewed"
    path.write_text(json.dumps(candidate))
    audited = MODULE.audit(root)["packages"][0]["candidates"][0]
    assert audited["unresolved_activation_gates"] == candidate["activation_gates"]
    assert "remain unresolved" in MODULE.render(MODULE.audit(root))


@pytest.mark.parametrize("change", ["answer", "variant-answer", "points", "objective", "version", "escape", "prerequisite"])
def test_invalid_artifacts_fail_closed(packet, change):
    root, course, path, c = packet
    if change == "answer":
        c["questions"][0]["solution_spec"] = {"answer": 1}
    elif change == "variant-answer":
        c["variant_questions"] = {"question": {"answer": 1}}
    elif change == "points":
        c["points"] = 3
    elif change == "objective":
        c["objective_ids"] = ["missing"]
    elif change == "version":
        c["content_version"] = "missing"
    elif change == "escape":
        c["dataset_path"] = "../outside.csv"
    else:
        c["prerequisite_sha256"] = {"assessment-specs/data.csv": "0" * 64}
    path.write_text(json.dumps(c))
    with pytest.raises(ValueError):
        MODULE.audit(root)
