"""Grade every public practice item in the repository against its own authored key.

For each item the correct response must earn full credit and a deliberately wrong response must
earn none. This guards the authoring itself (a key that does not grade, an option order that was
changed without its answer index, a numeric key outside its own tolerance) for every package, not
only for the grader code. Items that depend on randomization variants are checked in test_variants.
"""

from __future__ import annotations

import base64
import json
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

COURSES = Path(__file__).resolve().parents[2] / "content" / "courses"


def load_items():
    items = []
    for path in sorted(COURSES.glob("*/question-banks/practice.json")):
        for question in json.loads(path.read_text(encoding="utf-8"))["questions"]:
            if "randomization" in question:
                continue
            items.append(pytest.param(question, id=question["id"]))
    return items


def correct_response(question):
    kind, spec = question["type"], question["solution_spec"]
    if kind == "multiple_select":
        return list(spec["answer"])
    if kind == "single_choice":
        return spec["answer"]
    if kind == "numeric":
        return f"{spec['answer']} {spec.get('unit', '')}".strip()
    if kind in ("data_interpretation", "structured"):
        return {f["id"]: str(f["answer"]) if f["type"] == "single_choice" else f"{f['answer']} {f['unit']}".strip()
                for f in spec["field_specs"]}
    if kind == "graph":
        return {**{f"{p['id']}_x": str(p["x"]) for p in spec["points"]},
                **{f"{p['id']}_y": str(p["y"]) for p in spec["points"]}}
    if kind == "file_upload":
        validation, rows = spec["validation_spec"], {}
        for check in validation["checks"]:
            rows.setdefault(check["row_id"], {})[check["column"]] = check["answer"]
        lines = [",".join(validation["columns"])]
        lines += [",".join([row] + [str(rows[row][c]) for c in validation["columns"] if c != validation["key_column"]])
                  for row in rows]
        return {"content_base64": base64.b64encode(("\n".join(lines) + "\n").encode()).decode()}
    return None


def wrong_response(question):
    kind, spec = question["type"], question["solution_spec"]
    if kind == "single_choice":
        return (spec["answer"] + 1) % len(question["options"])
    if kind == "multiple_select":
        options = len(question["options"])
        return [i for i in range(options) if i not in spec["answer"]][: max(1, len(spec["answer"]))]
    if kind == "numeric":
        scale = abs(spec["answer"]) or 1.0
        shifted = spec["answer"] + 10 * (spec.get("tolerance", 0) + scale * (spec.get("relative_tolerance") or 0) + 0.1 * scale)
        return f"{shifted} {spec.get('unit', '')}".strip()
    if kind in ("data_interpretation", "structured"):
        fields = {f["id"]: f for f in question["response_fields"]}
        out = {}
        for f in spec["field_specs"]:
            if f["type"] == "single_choice":
                out[f["id"]] = str((f["answer"] + 1) % len(fields[f["id"]]["options"]))
            else:
                scale = abs(f["answer"]) or 1.0
                out[f["id"]] = f"{f['answer'] + 10 * (f.get('tolerance', 0) + 0.1 * scale)} {f['unit']}".strip()
        return out
    if kind == "graph":
        return {**{f"{p['id']}_x": str(p["x"] + 1000) for p in spec["points"]},
                **{f"{p['id']}_y": str(p["y"] + 1000) for p in spec["points"]}}
    if kind == "file_upload":
        validation, rows = spec["validation_spec"], {}
        for check in validation["checks"]:
            rows.setdefault(check["row_id"], {})[check["column"]] = check["answer"] + 1000
        lines = [",".join(validation["columns"])]
        lines += [",".join([row] + [str(rows[row][c]) for c in validation["columns"] if c != validation["key_column"]])
                  for row in rows]
        return {"content_base64": base64.b64encode(("\n".join(lines) + "\n").encode()).decode()}
    return None


@pytest.mark.parametrize("question", load_items())
def test_authored_key_earns_full_credit(question):
    response = correct_response(question)
    if response is None:
        pytest.skip(f"no response builder for {question['type']}")
    result = grade(question, AttemptRequest(response=response))
    assert result.score == pytest.approx(question["points"]), result.feedback.diagnosis


@pytest.mark.parametrize("question", load_items())
def test_deliberately_wrong_answer_earns_no_credit(question):
    response = wrong_response(question)
    if response is None:
        pytest.skip(f"no wrong-response builder for {question['type']}")
    result = grade(question, AttemptRequest(response=response))
    assert result.score == 0, question["id"]
