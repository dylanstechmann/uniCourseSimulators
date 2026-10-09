"""Authored precision/unit boundaries for six public chemistry practice items."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

COURSE = Path(__file__).resolve().parents[2] / "content/courses/general-chemistry-1"
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text())["questions"]}
CASES = [
    ("general-chemistry-1-7:entity-count", ["1.506", "1.506e0"], ["1.5060", "1.51", "1.508", "not a number"]),
    ("general-chemistry-1-7:photon-energy", ["3.973", "3.973e0"], ["3.9730", "3.97", "3.975", "NaN"]),
    (
        "general-chemistry-1-7:photon-molar-energy",
        ["239.3 kJ/mol", "2.393e5 J/mol"],
        ["239.30 kJ/mol", "239.3", "239.3 mol", "239.4 kJ/mol"],
    ),
    ("general-chemistry-1-9:percent-yield", ["75.0", "7.50e1"], ["75", "75.00", "75.1", "unknown"]),
    (
        "general-chemistry-1-10:gas-pressure",
        ["1.247e5 Pa", "0.1247 MPa"],
        ["1.2470e5 Pa", "1.247e5", "1.247e5 J", "1.248e5 Pa"],
    ),
    (
        "general-chemistry-1-11:molar-enthalpy",
        ["-63.0 kJ/mol", "-6.30e4 J/mol"],
        ["-63 kJ/mol", "-63.00 kJ/mol", "-63.0", "-63.1 kJ/mol"],
    ),
]


@pytest.mark.parametrize("question_id,correct,incorrect", CASES, ids=[case[0] for case in CASES])
def test_authored_precision_units_and_near_misses(question_id, correct, incorrect):
    question = BANK[question_id]
    for response in correct:
        assert grade(question, AttemptRequest(response=response)).score == question["points"], response
    for response in incorrect:
        assert grade(question, AttemptRequest(response=response)).score == 0, response
