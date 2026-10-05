"""Deterministic seed practice graders. No inference of reasoning or keyword grading."""

import hashlib
import json
import math
import re
from decimal import Decimal, DecimalException
from fractions import Fraction

from .schemas import AttemptRequest, Feedback, FeedbackComponent, GradeResult
from .symbolic import SymbolicExpressionError, matches_expected, prepare_answer
from .units import UnitParseError, dimensions_from_spec, parse_unit

NUMBER = re.compile(
    r"^([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*"
    r"((?:(?:[A-Za-zμµΩω°%]|1/[A-Za-z])[A-Za-z0-9μµΩω°%·/⁻¹²³^*(). _-]*)?)$"
)
GRADING_POLICY_VERSION = "practice-v7"


class GradingUnavailable(ValueError):
    """An authored requirement is not implemented; do not award a silent grade."""


def _grade_data_interpretation(question: dict, request: AttemptRequest, points: float) -> GradeResult:
    """Grade explicit data fields independently; never infer free-text reasoning."""
    fields = question.get("response_fields")
    specifications = question.get("solution_spec", {}).get("field_specs")
    if not isinstance(fields, list) or not 2 <= len(fields) <= 20 or not isinstance(specifications, list):
        raise GradingUnavailable("Data-interpretation field specifications are invalid")

    field_by_id = {}
    for field in fields:
        if not isinstance(field, dict) or not isinstance(field.get("id"), str):
            raise GradingUnavailable("Data-interpretation response fields are invalid")
        field_id = field["id"]
        if field_id in field_by_id or field.get("type") not in {"numeric", "single_choice"}:
            raise GradingUnavailable("Data-interpretation response fields are unsupported")
        field_points = field.get("points")
        if not isinstance(field_points, (int, float)) or isinstance(field_points, bool) or not math.isfinite(field_points) or field_points <= 0:
            raise GradingUnavailable("Data-interpretation field points must be positive and finite")
        if not isinstance(field.get("prompt"), str) or not field["prompt"].strip():
            raise GradingUnavailable("Data-interpretation field prompts are required")
        if field["type"] == "single_choice" and (
            not isinstance(field.get("options"), list) or len(field["options"]) < 2
            or any(not isinstance(option, str) for option in field["options"])
        ):
            raise GradingUnavailable("Data-interpretation choice fields require options")
        field_by_id[field_id] = field

    spec_by_id = {}
    for specification in specifications:
        if not isinstance(specification, dict) or not isinstance(specification.get("id"), str):
            raise GradingUnavailable("Data-interpretation answer fields are invalid")
        field_id = specification["id"]
        if field_id in spec_by_id:
            raise GradingUnavailable("Data-interpretation answer field IDs must be unique")
        spec_by_id[field_id] = specification
    if set(field_by_id) != set(spec_by_id):
        raise GradingUnavailable("Data-interpretation fields and answer specifications must match")

    maximum = sum(float(field["points"]) for field in fields)
    if not math.isclose(maximum, points, rel_tol=0, abs_tol=1e-8):
        raise GradingUnavailable("Data-interpretation field points must sum to the question total")

    response = request.response
    if not isinstance(response, dict):
        diagnosis = "malformed_response"
        components = []
        score = 0.0
    elif set(response) - set(field_by_id):
        diagnosis = "malformed_response"
        components = []
        score = 0.0
    else:
        authored_feedback = question.get("feedback", {})
        lesson_ids = authored_feedback.get("lesson_ids", [])
        components = []
        score = 0.0
        for field_id, field in field_by_id.items():
            field_spec = spec_by_id[field_id]
            if field_spec.get("type") != field["type"]:
                raise GradingUnavailable("Data-interpretation field types must match their answer specifications")
            if field["type"] == "single_choice":
                answer = field_spec.get("answer")
                if type(answer) is not int or not 0 <= answer < len(field["options"]):
                    raise GradingUnavailable("Data-interpretation choice answer is outside its option array")
            else:
                answer = field_spec.get("answer")
                unit = field_spec.get("unit")
                tolerance = field_spec.get("tolerance")
                relative_tolerance = field_spec.get("relative_tolerance", 0)
                unit_required = field_spec.get("unit_required", False)
                if (
                    isinstance(answer, bool) or not isinstance(answer, (int, float))
                    or not math.isfinite(answer)
                    or not isinstance(unit, str) or field.get("unit") != unit
                    or isinstance(tolerance, bool) or not isinstance(tolerance, (int, float))
                    or not math.isfinite(tolerance) or tolerance < 0
                    or isinstance(relative_tolerance, bool)
                    or not isinstance(relative_tolerance, (int, float))
                    or not math.isfinite(relative_tolerance)
                    or not 0 <= relative_tolerance <= 1
                    or not isinstance(unit_required, bool)
                ):
                    raise GradingUnavailable("Data-interpretation numeric answer specification is invalid")
            if field_id not in response:
                components.append(FeedbackComponent(
                    field_id=field_id, label=field["prompt"], score=0,
                    max_score=float(field["points"]), diagnosis="missing_response",
                ))
                continue
            child_question = {
                "type": field["type"], "options": field.get("options", []),
                "points": field["points"],
                "solution_spec": {key: value for key, value in field_spec.items() if key not in {"id", "type"}},
                "feedback": {"hint": authored_feedback.get("hint"), "lesson_ids": lesson_ids},
            }
            child_result = grade(child_question, AttemptRequest(response=response[field_id]))
            score += child_result.score
            components.append(FeedbackComponent(
                field_id=field_id, label=field["prompt"], score=child_result.score,
                max_score=child_result.max_score, diagnosis=child_result.feedback.diagnosis,
            ))
        correct = math.isclose(score, points, rel_tol=0, abs_tol=1e-8)
        if correct:
            diagnosis = "correct_result_reasoning_not_assessed"
        elif score > 0:
            diagnosis = "data_interpretation_partial"
        else:
            child_diagnoses = {component.diagnosis for component in components}
            diagnosis = next((item for item in (
                "unit_mistake", "malformed_response", "numerical_mismatch",
                "significant_figures_mistake", "incorrect_selection",
            ) if item in child_diagnoses), "data_interpretation_incorrect")

    authored = question.get("feedback", {})
    lesson_ids = authored.get("lesson_ids", [])
    correct = math.isclose(score, points, rel_tol=0, abs_tol=1e-8)
    return GradeResult(
        score=score, max_score=points, correct=correct,
        feedback=Feedback(
            diagnosis=diagnosis,
            hint=None if correct else authored.get("hint"),
            misconception=None if correct else authored.get("misconception"),
            lesson_id=lesson_ids[0] if lesson_ids else None,
            next_step=("Compare the computed result with the evidence limits; this item did not assess free-form reasoning."
                       if correct else "The fields earn credit independently. Review each field-level result, then separate what the data show from what they do not establish."),
            components=components,
        ),
        grading_policy_version=GRADING_POLICY_VERSION,
    )


def count_significant_figures(number: str) -> int:
    """Count precision encoded lexically in a decimal/scientific-notation answer."""
    mantissa = re.split(r"[eE]", number, maxsplit=1)[0].lstrip("+-")
    if "." in mantissa:
        digits = mantissa.replace(".", "").lstrip("0")
        if digits:
            return len(digits)
        decimal_places = len(mantissa.split(".", maxsplit=1)[1])
        return decimal_places or 1
    digits = mantissa.lstrip("0")
    if not digits:
        return 1
    return len(digits.rstrip("0"))


def question_spec_digest(question: dict, variant_id: str | None = None) -> str:
    """Fingerprint the exact authored question and the deterministic grader version."""
    payload = json.dumps(
        {"policy": GRADING_POLICY_VERSION, "question": question, "variant_id": variant_id},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def grade(question: dict, request: AttemptRequest) -> GradeResult:
    spec = question["solution_spec"]
    if question.get("randomization") is not None:
        raise GradingUnavailable("Randomized question generation is not enabled")
    correct = False
    diagnosis = "incorrect_result"
    points = float(question.get("points", 1))
    score = 0.0
    if not math.isfinite(points) or points <= 0:
        raise ValueError("Question points must be positive and finite")
    if question["type"] == "data_interpretation":
        return _grade_data_interpretation(question, request, points)
    if question["type"] == "multiple_select":
        if not isinstance(request.response, list):
            diagnosis = "malformed_response"
        else:
            options = question.get("options", [])
            answer = spec.get("answer")
            policy = spec.get("partial_credit")
            if (
                not isinstance(options, list)
                or len(options) < 2
                or any(not isinstance(option, str) for option in options)
                or not isinstance(answer, list)
                or not answer
                or any(type(index) is not int or index < 0 or index >= len(options) for index in answer)
                or len(answer) != len(set(answer))
            ):
                raise ValueError("Invalid multiple-select answer specification")
            if policy not in {"all-or-nothing", "correct-minus-incorrect-clamped-v1"}:
                raise GradingUnavailable("Multiple-select partial-credit policy is not enabled")
            if any(type(index) is not int or index < 0 or index >= len(options) for index in request.response):
                diagnosis = "malformed_response"
            else:
                selected, key = set(request.response), set(answer)
                if policy == "all-or-nothing":
                    fraction = float(selected == key)
                else:
                    fraction = max(0, len(selected & key) - len(selected - key)) / len(key)
                correct = fraction == 1
                score = points * fraction
                diagnosis = (
                    "correct_result_reasoning_not_assessed" if correct
                    else "partially_correct_selection" if score > 0
                    else "incorrect_selection"
                )
    elif question["type"] == "single_choice":
        text = str(request.response)
        try:
            response = Decimal(text)
            correct = response == response.to_integral() and 0 <= response < len(question["options"]) and response == Decimal(str(spec["answer"]))
        except DecimalException:
            diagnosis = "malformed_response"
    elif question["type"] == "numeric":
        significant_figures = spec.get("significant_figures")
        if significant_figures is not None and (
            type(significant_figures) is not int or not 1 <= significant_figures <= 12
        ):
            raise GradingUnavailable("significant_figures must be an integer from 1 through 12")
        match = NUMBER.fullmatch(str(request.response).strip())
        if not match:
            diagnosis = "malformed_response"
        else:
            supplied_unit = request.unit if request.unit is not None else match[2]
            authored_unit = spec.get("unit") or ""
            try:
                expected = parse_unit(authored_unit)
            except UnitParseError as exc:
                raise GradingUnavailable(f"Authored unit is unsupported: {authored_unit}") from exc
            if spec.get("dimensions") is not None:
                try:
                    authored_dimensions = dimensions_from_spec(spec["dimensions"])
                except UnitParseError as exc:
                    raise GradingUnavailable("Authored dimensions are invalid or unsupported") from exc
                if authored_dimensions != expected.dimensions:
                    raise GradingUnavailable("Authored dimensions do not match the authored unit")
            try:
                if request.unit is not None and match[2]:
                    field_unit = parse_unit(request.unit)
                    inline_unit = parse_unit(match[2])
                    if field_unit != inline_unit:
                        diagnosis = "unit_mistake"
                        supplied = None
                    else:
                        supplied = field_unit
                else:
                    supplied = parse_unit(supplied_unit) if supplied_unit else expected
                if supplied is None:
                    pass
                elif (spec.get("unit_required", False) and authored_unit and not supplied_unit):
                    diagnosis = "unit_mistake"
                elif supplied.dimensions != expected.dimensions or supplied.context != expected.context:
                    diagnosis = "unit_mistake"
                else:
                    try:
                        value = Decimal(match[1])
                        answer = Decimal(str(spec["answer"]))
                        tolerance = Decimal(str(spec.get("tolerance", 0)))
                        relative_tolerance = Decimal(str(spec.get("relative_tolerance") or 0))
                        if (
                            not relative_tolerance.is_finite()
                            or relative_tolerance < 0
                            or relative_tolerance > 1
                        ):
                            raise ValueError("relative_tolerance must be finite and between 0 and 1")
                        if (
                            not value.is_finite()
                            or not answer.is_finite()
                            or not tolerance.is_finite()
                            or tolerance < 0
                            or len(match[1]) > 128
                            or abs(value.adjusted()) > 100
                            or abs(answer.adjusted()) > 100
                            or (tolerance != 0 and abs(tolerance.adjusted()) > 100)
                        ):
                            diagnosis = "malformed_response"
                        else:
                            # Convert the learner's number and the authored absolute
                            # tolerance into the question's authored unit. This
                            # policy adds relative tolerance × |key| to the absolute
                            # tolerance, so it remains meaningful for a zero key.
                            value_in_expected_unit = Fraction(value) * supplied.scale / expected.scale
                            allowed_error = Fraction(tolerance) + Fraction(relative_tolerance) * abs(Fraction(answer))
                            correct = abs(value_in_expected_unit - Fraction(answer)) <= allowed_error
                            diagnosis = "correct_result" if correct else "numerical_mismatch"
                            if correct and significant_figures is not None:
                                if count_significant_figures(match[1]) != significant_figures:
                                    correct = False
                                    diagnosis = "significant_figures_mistake"
                    except DecimalException:
                        diagnosis = "malformed_response"
            except UnitParseError:
                # Unknown or malformed learner units cannot receive credit.
                diagnosis = "unit_mistake"
            except DecimalException:
                diagnosis = "malformed_response"
    elif question["type"] == "symbolic":
        try:
            symbols, expected = prepare_answer(
                spec.get("expression"), spec.get("variables"), spec.get("assumptions")
            )
        except SymbolicExpressionError as exc:
            raise GradingUnavailable("Authored symbolic grading specification is invalid") from exc
        try:
            correct = matches_expected(str(request.response), symbols, expected)
            diagnosis = "correct_result" if correct else "symbolic_mismatch"
        except (SymbolicExpressionError, ArithmeticError, RecursionError, ValueError, TypeError):
            diagnosis = "malformed_response"
        except Exception:
            # SymPy errors fail closed. Learner-controlled expressions never turn
            # an internal symbolic limitation into a passing grade or API crash.
            diagnosis = "malformed_response"
    else:
        raise GradingUnavailable("Unsupported question type: not enabled for server grading")
    if correct:
        score = points
        diagnosis = "correct_result_reasoning_not_assessed"
    authored = question.get("feedback", {})
    lesson_ids = authored.get("lesson_ids", [])
    return GradeResult(
        score=score, max_score=points, correct=bool(correct),
        feedback=Feedback(
            diagnosis=diagnosis, hint=None if correct else authored.get("hint"),
            misconception=None, lesson_id=lesson_ids[0] if lesson_ids else None,
            next_step=("Explain why the result follows from the mechanism; this check did not assess reasoning."
                       if correct else "Check that the units are dimensionally compatible and convert the quantity into the requested unit."
                       if diagnosis == "unit_mistake" else "Report exactly the requested number of significant figures; use a decimal point or scientific notation to make trailing zeros explicit."
                       if diagnosis == "significant_figures_mistake" else "Check the algebraic form, signs, powers, and declared variables; this practice check accepts equivalent rational expressions."
                       if diagnosis == "symbolic_mismatch" else "Revisit the linked lesson and check your assumptions before another attempt."),
        ),
        grading_policy_version=GRADING_POLICY_VERSION,
    )
