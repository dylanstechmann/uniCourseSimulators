"""Deterministic seed practice graders. No inference of reasoning or keyword grading."""

import math
import re
from decimal import Decimal, DecimalException

from .schemas import AttemptRequest, Feedback, GradeResult

NUMBER = re.compile(
    r"^([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*"
    r"((?:(?:[A-Za-zμµΩω°%]|1/[A-Za-z])[A-Za-z0-9μµΩω°%·/⁻¹²³^*(). _-]*)?)$"
)


class GradingUnavailable(ValueError):
    """An authored requirement is not implemented; do not award a silent grade."""


def unit_text(value: str | None) -> str:
    # SI prefixes and symbols are case-sensitive (mV != MV, ms != mS).
    return (value or "").replace("μ", "u").replace("µ", "u").replace("·", "").replace(" ", "")


def grade(question: dict, request: AttemptRequest) -> GradeResult:
    spec = question["solution_spec"]
    if question.get("randomization") is not None:
        raise GradingUnavailable("Randomized question generation is not enabled")
    if spec.get("relative_tolerance") not in (None, 0, 0.0):
        raise GradingUnavailable("Relative tolerance grading is not enabled")
    correct = False
    diagnosis = "incorrect_result"
    points = float(question.get("points", 1))
    if not math.isfinite(points) or points <= 0:
        raise ValueError("Question points must be positive and finite")
    if question["type"] == "single_choice":
        text = str(request.response)
        try:
            response = Decimal(text)
            correct = response == response.to_integral() and 0 <= response < len(question["options"]) and response == Decimal(str(spec["answer"]))
        except DecimalException:
            diagnosis = "malformed_response"
    elif question["type"] == "numeric":
        if spec.get("significant_figures") is not None or spec.get("dimensions") is not None:
            raise GradingUnavailable("Dimensional conversion and significant-figure grading are not enabled")
        match = NUMBER.fullmatch(str(request.response).strip())
        if not match:
            diagnosis = "malformed_response"
        else:
            supplied_unit = request.unit if request.unit is not None else match[2]
            expected_unit = unit_text(spec.get("unit"))
            # Conflicting typed/unit-field responses are not silently normalized.
            if request.unit is not None and match[2] and unit_text(request.unit) != unit_text(match[2]):
                diagnosis = "unit_mistake"
            elif (supplied_unit and unit_text(supplied_unit) != expected_unit) or (
                spec.get("unit_required", False) and expected_unit and not supplied_unit
            ):
                diagnosis = "unit_mistake"
            else:
                try:
                    value = Decimal(match[1])
                    answer = Decimal(str(spec["answer"]))
                    tolerance = Decimal(str(spec.get("tolerance", 0)))
                    if not answer.is_finite() or not tolerance.is_finite() or tolerance < 0:
                        raise ValueError("Invalid authored numeric specification")
                    correct = value.is_finite() and abs(value - answer) <= tolerance
                    diagnosis = "correct_result" if correct else "numerical_mismatch"
                except DecimalException:
                    diagnosis = "malformed_response"
    else:
        raise GradingUnavailable("Unsupported question type: not enabled for server grading")
    if correct:
        diagnosis = "correct_result_reasoning_not_assessed"
    authored = question.get("feedback", {})
    lesson_ids = authored.get("lesson_ids", [])
    return GradeResult(
        score=points if correct else 0, max_score=points, correct=bool(correct),
        feedback=Feedback(
            diagnosis=diagnosis, hint=None if correct else authored.get("hint"),
            misconception=None, lesson_id=lesson_ids[0] if lesson_ids else None,
            next_step=("Explain why the result follows from the mechanism; this check did not assess reasoning."
                       if correct else "Revisit the linked lesson and check your assumptions before another attempt."),
        ),
    )
