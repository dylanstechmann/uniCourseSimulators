"""Integrity checks for the cell-biology package and the generated gap report.

These tests read committed files only. They do not judge teaching quality, and passing them does not
mean any component was reviewed. They exist so the homework, lab and specification files cannot drift
away from the question bank, from their own example tables, or from the rule that no answer key for a
protected component is committed.
"""

from __future__ import annotations

import csv
import io
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content" / "courses" / "cell-biology"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def bank():
    return json.loads((COURSE / "question-banks" / "practice.json").read_text(encoding="utf-8"))["questions"]


def markdown_files():
    return sorted(p for p in COURSE.rglob("*.md"))


def test_relative_links_in_cell_biology_markdown_resolve():
    broken = []
    for path in markdown_files():
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in LINK.findall(text):
            if re.match(r"[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (path.parent / file_part).resolve().exists():
                broken.append(f"{path.relative_to(COURSE)} -> {target}")
    assert not broken, broken


def test_every_homework_and_lab_dataset_link_names_a_committed_file():
    missing = []
    for path in list((COURSE / "assignments").glob("*.md")) + list((COURSE / "labs").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for name in re.findall(r"(?:assignments|labs)/([A-Za-z0-9_.-]+\.csv)", text):
            if not (path.parent / name).is_file():
                missing.append(f"{path.name}: {name}")
    assert not missing, missing


def test_every_csv_summary_check_carries_an_independent_recalculation():
    unchecked = []
    for question in bank():
        if question["type"] != "file_upload":
            continue
        for check in question["solution_spec"]["validation_spec"]["checks"]:
            calculation = check.get("calculation")
            if not isinstance(calculation, dict) or calculation.get("operation") not in {"count", "mean"}:
                unchecked.append(f"{question['id']}:{check['id']}")
    assert not unchecked, unchecked


def parse_example_blocks(markdown: str):
    for block in re.findall(r"```csv\n(.*?)```", markdown, flags=re.S):
        yield list(csv.reader(io.StringIO(block.strip())))


def test_example_summary_tables_in_packets_equal_the_authored_keys():
    """The tables a learner is shown as the required format must agree with the grader's answers."""
    keys = {}
    for question in bank():
        if question["type"] == "file_upload":
            spec = question["solution_spec"]["validation_spec"]
            for check in spec["checks"]:
                keys.setdefault((tuple(spec["columns"]), check["row_id"], check["column"]), check["answer"])
    mismatches, compared = [], 0
    for path in list((COURSE / "assignments").glob("homework-0[2-8]-*.md")) + list((COURSE / "labs").glob("03-*.md")):
        for table in parse_example_blocks(path.read_text(encoding="utf-8")):
            header = tuple(table[0])
            for row in table[1:]:
                for column, value in zip(header[1:], row[1:]):
                    key = (header, row[0], column)
                    assert key in keys, f"{path.name}: example cell {key} has no authored check"
                    compared += 1
                    if abs(float(value) - float(keys[key])) > 1e-9:
                        mismatches.append(f"{path.name}: {key} shows {value}, key is {keys[key]}")
    assert compared >= 60
    assert not mismatches, mismatches


def test_assessment_specifications_contain_no_items_or_keys_and_say_so():
    folder = COURSE / "assessment-specs"
    documents = sorted(folder.glob("*.md"))
    assert {p.name for p in documents} >= {"midterm-specification.md", "final-specification.md",
                                           "integrative-project-specification.md"}
    for path in documents:
        text = path.read_text(encoding="utf-8")
        assert '"solution_spec"' not in text and '"answer"' not in text, path.name
        if path.name != "README.md":
            assert "not authored" in text.lower()
            assert "No question, answer key" in text
            assert "No reviewer has examined this specification" in text
    other = [p for p in folder.iterdir() if p.suffix not in {".md"}]
    assert not other, f"unexpected non-document files beside the specifications: {other}"


def test_no_answer_package_files_are_committed_anywhere_in_the_course_tree():
    offenders = [str(p.relative_to(ROOT)) for p in (ROOT / "content").rglob("*.json")
                 if "private" in p.parts or p.name.startswith("answer-package")]
    assert not offenders, offenders


def test_course_labels_are_unchanged_by_the_new_material():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert course["maturity"] == "partial"
    assert course["review"] == {"status": "unreviewed", "reviewed_version": None, "reviewers": []}
    assert course["grading_policy"]["mode"] == "formative-only"
    assert course["grading_policy"]["categories"] == []
    for assessment in course["assessments"]:
        assert assessment["mode"] in {"practice", "self-assessment"}, assessment["id"]


def test_homework_points_equal_the_sum_of_their_items():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    points = {q["id"]: q["points"] for q in bank()}
    for assessment in course["assessments"]:
        if assessment["type"] in {"homework", "lab"}:
            assert assessment["points"] == sum(points[i] for i in assessment["question_ids"]), assessment["id"]


def test_gap_report_is_current():
    result = subprocess.run([sys.executable, "-B", str(ROOT / "tools" / "objective_coverage.py"), "--check",
                             str(ROOT / "docs" / "COURSE_GAP_REPORT.md")], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
