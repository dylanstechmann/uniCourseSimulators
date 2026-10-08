"""Learner-visible text must show numbers the way a person writes them.

Early authoring batches left raw exponent notation (a number, the letter e, a power of ten) and floating-point
artifacts (a decimal with a long run of trailing digits) in readings, prompts and solutions. These checks keep
them out. Code spans and the programming package are exempt, because Python literals and printed floats are
what that package teaches.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "content" / "courses"
CODE = re.compile(r"(```[\s\S]*?```|`[^`\n]*`)")
RAW_EXPONENT = re.compile(r"(?<![\w.`])\d(?:\.\d+)?e[-+]?\d+\b")
LONG_DECIMAL = re.compile(r"\d+\.\d{9,}")
SKIP_KEYS = {"solution_spec", "graph_spec", "id", "question_ids", "history"}
PYTHON_PACKAGES = {"programming"}


def defects(text: str) -> list[str]:
    return [m.group(0) for rx in (RAW_EXPONENT, LONG_DECIMAL) for m in rx.finditer(text)]


def prose_outside_code(markdown: str) -> str:
    return "".join(part for part in CODE.split(markdown) if not CODE.fullmatch(part))


def test_detector_flags_the_defects_and_ignores_code_and_ordinary_numbers():
    assert defects("rate 2.0e-10 per cell and 3.75e+09 cells") == ["2.0e-10", "3.75e+09"]
    assert defects("a difference of 0.15000000000000002") == ["0.15000000000000002"]
    assert defects("2.0×10⁻¹⁰ and 0.15, 1.0000001, 0.8187 and the base e") == []
    assert defects(prose_outside_code("Python gives `0.30000000000000004` and ```\n1e-9\n```")) == []


def test_readings_have_no_raw_exponents_or_float_artifacts_outside_code():
    found = {}
    for path in sorted(COURSES.glob("*/modules/*.md")) + sorted(COURSES.glob("*/labs/*.md")) + sorted(COURSES.glob("*/assignments/*.md")):
        bad = defects(prose_outside_code(path.read_text(encoding="utf-8")))
        if bad:
            found[str(path.relative_to(COURSES))] = bad
    assert not found, found


def _walk(value, where, out):
    if isinstance(value, str):
        out.extend((where, token) for token in defects(value))
    elif isinstance(value, list):
        for i, item in enumerate(value):
            _walk(item, f"{where}[{i}]", out)
    elif isinstance(value, dict):
        for key, item in value.items():
            if key not in SKIP_KEYS:
                _walk(item, f"{where}.{key}", out)


def test_learner_visible_json_text_has_no_raw_exponents_or_float_artifacts():
    found = []
    for package in sorted(COURSES.iterdir()):
        if not package.is_dir() or package.name in PYTHON_PACKAGES:
            continue
        files = [package / "course.json", *sorted((package / "question-banks").glob("*.json")), *sorted((package / "rubrics").glob("*.json"))]
        for path in files:
            if path.is_file():
                _walk(json.loads(path.read_text(encoding="utf-8")), str(path.relative_to(COURSES)), found)
    assert not found, found[:10]
