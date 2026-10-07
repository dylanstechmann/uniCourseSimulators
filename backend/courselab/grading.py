"""Deterministic seed practice graders. No inference of reasoning or keyword grading."""

import base64
import binascii
import csv
import hashlib
import io
import json
import math
import re
from decimal import Decimal, DecimalException
from fractions import Fraction

from .schemas import (
    MAX_CSV_UPLOAD_BYTES,
    AttemptRequest,
    Feedback,
    FeedbackComponent,
    GradeResult,
)
from .symbolic import SymbolicExpressionError, matches_expected, prepare_answer
from .units import UnitParseError, dimensions_from_spec, parse_unit

NUMBER = re.compile(
    r"^([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*"
    r"((?:(?:[A-Za-zμµΩω°%]|1/[A-Za-z])[A-Za-z0-9μµΩω°%·/⁻¹²³^*(). _-]*)?)$"
)
GRADING_POLICY_VERSION = "practice-v10"
MAX_CSV_UPLOAD_COLUMNS = 20
MAX_CSV_UPLOAD_ROWS = 50


class GradingUnavailable(ValueError):
    """An authored requirement is not implemented; do not award a silent grade."""


def _grade_fielded_response(question: dict, request: AttemptRequest, points: float) -> GradeResult:
    """Grade explicit fields and, for structured items, their analytic rubric."""
    structured = question.get("type") == "structured"
    fields = question.get("response_fields")
    specifications = question.get("solution_spec", {}).get("field_specs")
    if not isinstance(fields, list) or not 2 <= len(fields) <= 20 or not isinstance(specifications, list):
        raise GradingUnavailable("Structured response field specifications are invalid")

    field_by_id = {}
    for field in fields:
        if not isinstance(field, dict) or not isinstance(field.get("id"), str):
            raise GradingUnavailable("Structured response fields are invalid")
        field_id = field["id"]
        if field_id in field_by_id or field.get("type") not in {"numeric", "single_choice"}:
            raise GradingUnavailable("Structured response fields are unsupported")
        field_points = field.get("points")
        if not isinstance(field_points, (int, float)) or isinstance(field_points, bool) or not math.isfinite(field_points) or field_points <= 0:
            raise GradingUnavailable("Structured response field points must be positive and finite")
        if not isinstance(field.get("prompt"), str) or not field["prompt"].strip():
            raise GradingUnavailable("Structured response field prompts are required")
        if field["type"] == "single_choice" and (
            not isinstance(field.get("options"), list) or len(field["options"]) < 2
            or any(not isinstance(option, str) for option in field["options"])
        ):
            raise GradingUnavailable("Structured response choice fields require options")
        field_by_id[field_id] = field

    spec_by_id = {}
    for specification in specifications:
        if not isinstance(specification, dict) or not isinstance(specification.get("id"), str):
            raise GradingUnavailable("Structured response answer fields are invalid")
        field_id = specification["id"]
        if field_id in spec_by_id:
            raise GradingUnavailable("Structured response answer field IDs must be unique")
        spec_by_id[field_id] = specification
    if set(field_by_id) != set(spec_by_id):
        raise GradingUnavailable("Structured response fields and answer specifications must match")

    rubric_by_id = {}
    if structured:
        rubric = question.get("solution_spec", {}).get("rubric")
        if not isinstance(rubric, list) or not 2 <= len(rubric) <= 20:
            raise GradingUnavailable("Structured response analytic rubric is invalid")
        for criterion in rubric:
            if (
                not isinstance(criterion, dict)
                or not isinstance(criterion.get("id"), str)
                or not isinstance(criterion.get("criterion"), str)
                or len(criterion["criterion"].strip()) < 10
                or not isinstance(criterion.get("evidence"), list)
                or not criterion["evidence"]
                or any(not isinstance(item, str) or len(item.strip()) < 3 for item in criterion["evidence"])
            ):
                raise GradingUnavailable("Structured response rubric criteria and evidence are required")
            criterion_id = criterion["id"]
            criterion_points = criterion.get("points")
            if (
                criterion_id in rubric_by_id
                or isinstance(criterion_points, bool)
                or not isinstance(criterion_points, (int, float))
                or not math.isfinite(criterion_points)
                or criterion_points <= 0
            ):
                raise GradingUnavailable("Structured response rubric IDs and points are invalid")
            rubric_by_id[criterion_id] = criterion
        if set(rubric_by_id) != set(field_by_id):
            raise GradingUnavailable("Each structured response field must map to one rubric criterion")
        if any(
            not math.isclose(
                float(rubric_by_id[field_id]["points"]),
                float(field["points"]),
                rel_tol=0,
                abs_tol=1e-8,
            )
            for field_id, field in field_by_id.items()
        ):
            raise GradingUnavailable("Structured response rubric points must match their response fields")

    maximum = sum(float(field["points"]) for field in fields)
    if not math.isclose(maximum, points, rel_tol=0, abs_tol=1e-8):
        raise GradingUnavailable("Structured response field points must sum to the question total")

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
                raise GradingUnavailable("Structured response field types must match their answer specifications")
            if field["type"] == "single_choice":
                answer = field_spec.get("answer")
                if type(answer) is not int or not 0 <= answer < len(field["options"]):
                    raise GradingUnavailable("Structured response choice answer is outside its option array")
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
                    raise GradingUnavailable("Structured response numeric answer specification is invalid")
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
                field_id=field_id,
                label=rubric_by_id[field_id]["criterion"] if structured else field["prompt"],
                score=child_result.score,
                max_score=child_result.max_score, diagnosis=child_result.feedback.diagnosis,
            ))
        correct = math.isclose(score, points, rel_tol=0, abs_tol=1e-8)
        if correct:
            diagnosis = "structured_rubric_complete" if structured else "correct_result_reasoning_not_assessed"
        elif score > 0:
            diagnosis = "structured_rubric_partial" if structured else "data_interpretation_partial"
        else:
            child_diagnoses = {component.diagnosis for component in components}
            if structured:
                diagnosis = next(
                    (item for item in ("malformed_response", "unit_mistake") if item in child_diagnoses),
                    "structured_rubric_incorrect",
                )
            else:
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
            next_step=(
                "Each structured analytic criterion met its deterministic check. Free-form reasoning was not assessed."
                if correct and structured else
                "Review the criterion-level results and revise each structured response; free-form reasoning is not scored."
                if structured else
                "Compare the computed result with the evidence limits; this item did not assess free-form reasoning."
                if correct else
                "The fields earn credit independently. Review each field-level result, then separate what the data show from what they do not establish."
            ),
            components=components,
        ),
        grading_policy_version=GRADING_POLICY_VERSION,
    )


def _grade_csv_upload(question: dict, request: AttemptRequest, points: float) -> GradeResult:
    """Parse bounded UTF-8 CSV as inert data and grade authored numeric cells."""
    spec = question.get("solution_spec", {})
    validation = spec.get("validation_spec")
    rubric = spec.get("rubric")
    checks = validation.get("checks") if isinstance(validation, dict) else None
    columns = validation.get("columns") if isinstance(validation, dict) else None
    key_column = validation.get("key_column") if isinstance(validation, dict) else None
    max_bytes = spec.get("max_bytes")
    accepted = spec.get("accepted_media_types")
    if (
        accepted != ["text/csv"]
        or isinstance(max_bytes, bool)
        or not isinstance(max_bytes, int)
        or not 1 <= max_bytes <= MAX_CSV_UPLOAD_BYTES
        or not isinstance(validation, dict)
        or validation.get("format") != "csv-numeric-table-v1"
        or validation.get("delimiter") != ","
        or not isinstance(columns, list)
        or not 2 <= len(columns) <= MAX_CSV_UPLOAD_COLUMNS
        or any(not isinstance(column, str) or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", column) for column in columns)
        or len(columns) != len(set(columns))
        or key_column not in columns
        or not isinstance(checks, list)
        or not 1 <= len(checks) <= MAX_CSV_UPLOAD_ROWS
        or not isinstance(rubric, list)
        or len(rubric) != len(checks)
    ):
        raise GradingUnavailable("CSV upload specification is invalid or exceeds supported limits")

    checks_by_id = {}
    expected_row_ids = set()
    checked_cells = set()
    for check in checks:
        if (
            not isinstance(check, dict)
            or not isinstance(check.get("id"), str)
            or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", check["id"])
            or not isinstance(check.get("row_id"), str)
            or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", check["row_id"])
            or not isinstance(check.get("column"), str)
            or check.get("column") not in columns
            or check.get("column") == key_column
            or check.get("type") != "numeric"
            or isinstance(check.get("answer"), bool)
            or not isinstance(check.get("answer"), (int, float))
            or not math.isfinite(check["answer"])
            or not isinstance(check.get("unit"), str)
            or isinstance(check.get("tolerance"), bool)
            or not isinstance(check.get("tolerance"), (int, float))
            or not math.isfinite(check["tolerance"])
            or check["tolerance"] < 0
            or isinstance(check.get("relative_tolerance", 0), bool)
            or not isinstance(check.get("relative_tolerance", 0), (int, float))
            or not math.isfinite(check.get("relative_tolerance", 0))
            or not 0 <= check.get("relative_tolerance", 0) <= 1
            or not isinstance(check.get("unit_required", False), bool)
            or (check.get("unit_required", False) and not check.get("unit"))
        ):
            raise GradingUnavailable("CSV numeric cell specifications are invalid")
        if check["id"] in checks_by_id or (check["row_id"], check["column"]) in checked_cells:
            raise GradingUnavailable("CSV check IDs and target cells must be unique")
        checks_by_id[check["id"]] = check
        expected_row_ids.add(check["row_id"])
        checked_cells.add((check["row_id"], check["column"]))

    rubric_by_id = {}
    for criterion in rubric:
        if (
            not isinstance(criterion, dict)
            or not isinstance(criterion.get("id"), str)
            or criterion.get("id") not in checks_by_id
            or criterion.get("id") in rubric_by_id
            or not isinstance(criterion.get("criterion"), str)
            or len(criterion["criterion"].strip()) < 10
            or not isinstance(criterion.get("evidence"), list)
            or not criterion["evidence"]
            or any(not isinstance(item, str) or len(item.strip()) < 3 for item in criterion["evidence"])
            or isinstance(criterion.get("points"), bool)
            or not isinstance(criterion.get("points"), (int, float))
            or not math.isfinite(criterion["points"])
            or criterion["points"] <= 0
        ):
            raise GradingUnavailable("CSV analytic rubric is invalid")
        rubric_by_id[criterion["id"]] = criterion
    if set(rubric_by_id) != set(checks_by_id):
        raise GradingUnavailable("Each CSV numeric check must map to one analytic criterion")
    rubric_points = sum(float(item["points"]) for item in rubric)
    if not math.isclose(rubric_points, points, rel_tol=0, abs_tol=1e-8):
        raise GradingUnavailable("CSV rubric points must sum to the question total")

    response = request.response
    if not isinstance(response, dict) or set(response) != {"content_base64"}:
        return _csv_upload_result(question, points, "malformed_upload")
    encoded = response["content_base64"]
    if not isinstance(encoded, str) or len(encoded) > ((MAX_CSV_UPLOAD_BYTES + 2) // 3) * 4:
        return _csv_upload_result(question, points, "malformed_upload")
    try:
        payload = base64.b64decode(encoded, validate=True)
        if not payload or len(payload) > max_bytes:
            return _csv_upload_result(question, points, "malformed_upload")
        text = payload.decode("utf-8-sig")
        if "\x00" in text:
            return _csv_upload_result(question, points, "malformed_upload")
        parsed = []
        for index, row in enumerate(
            csv.reader(io.StringIO(text, newline=""), delimiter=",", strict=True)
        ):
            if index > MAX_CSV_UPLOAD_ROWS:
                return _csv_upload_result(question, points, "malformed_upload")
            parsed.append(row)
    except (binascii.Error, UnicodeDecodeError, csv.Error, ValueError):
        return _csv_upload_result(question, points, "malformed_upload")
    if not parsed or parsed[0] != columns:
        return _csv_upload_result(question, points, "malformed_upload")

    table = {}
    for row in parsed[1:]:
        if not row or all(not value.strip() for value in row):
            continue
        if (
            len(row) != len(columns)
            or any(len(value) > 1000 for value in row)
            or len(table) >= len(expected_row_ids)
        ):
            return _csv_upload_result(question, points, "malformed_upload")
        row_id = row[columns.index(key_column)].strip()
        if row_id not in expected_row_ids or row_id in table:
            return _csv_upload_result(question, points, "malformed_upload")
        table[row_id] = dict(zip(columns, (value.strip() for value in row), strict=True))

    components = []
    score = 0.0
    authored_feedback = question.get("feedback", {})
    lesson_ids = authored_feedback.get("lesson_ids", [])
    for check in checks:
        criterion = rubric_by_id[check["id"]]
        row = table.get(check["row_id"])
        value = row.get(check["column"], "") if row else ""
        if not value:
            components.append(FeedbackComponent(
                field_id=check["id"], label=criterion["criterion"], score=0,
                max_score=float(criterion["points"]), diagnosis="missing_response",
            ))
            continue
        child_question = {
            "type": "numeric",
            "points": criterion["points"],
            "solution_spec": {
                "answer": check["answer"],
                "unit": check["unit"],
                "tolerance": check["tolerance"],
                "relative_tolerance": check.get("relative_tolerance", 0),
                "unit_required": check.get("unit_required", False),
            },
            "feedback": {"hint": authored_feedback.get("hint"), "lesson_ids": lesson_ids},
        }
        child_result = grade(child_question, AttemptRequest(response=value))
        component_score = child_result.score
        score += component_score
        components.append(FeedbackComponent(
            field_id=check["id"], label=criterion["criterion"],
            score=component_score, max_score=float(criterion["points"]),
            diagnosis=child_result.feedback.diagnosis,
        ))
    correct = math.isclose(score, points, rel_tol=0, abs_tol=1e-8)
    diagnosis = (
        "csv_results_complete" if correct
        else "csv_results_partial" if score > 0
        else "csv_results_incomplete" if all(item.diagnosis == "missing_response" for item in components)
        else "csv_results_incorrect"
    )
    return _csv_upload_result(question, points, diagnosis, components, score)


def _csv_upload_result(
    question: dict,
    points: float,
    diagnosis: str,
    components: list[FeedbackComponent] | None = None,
    score: float = 0.0,
) -> GradeResult:
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
            next_step=(
                "The requested numeric table cells meet their deterministic checks; interpretation beyond the output table was not assessed."
                if correct else
                "Check the UTF-8 CSV header, one unique row per condition, the required numeric outputs, and their units. The upload is parsed as data only."
            ),
            components=components or [],
        ),
        grading_policy_version=GRADING_POLICY_VERSION,
    )


def _grade_graph_response(question: dict, request: AttemptRequest, points: float) -> GradeResult:
    """Grade learner-entered coordinates against a bounded, authored scatter plot."""
    graph = question.get("graph_spec")
    answer_spec = question.get("solution_spec", {})
    authored_points = graph.get("points") if isinstance(graph, dict) else None
    observations = graph.get("observations") if isinstance(graph, dict) else None
    expected_points = answer_spec.get("points")
    rubric = answer_spec.get("rubric")
    if (
        not isinstance(graph, dict)
        or not isinstance(authored_points, list)
        or not 2 <= len(authored_points) <= 20
        or not isinstance(observations, list)
        or len(observations) != len(authored_points)
        or not isinstance(expected_points, list)
        or not isinstance(rubric, list)
        or len(rubric) != 2 * len(authored_points)
    ):
        raise GradingUnavailable("Graph response specification is invalid")

    axes = {}
    for axis_id in ("x_axis", "y_axis"):
        axis = graph.get(axis_id)
        if not isinstance(axis, dict):
            raise GradingUnavailable("Graph axes are invalid")
        label, minimum, maximum = axis.get("label"), axis.get("minimum"), axis.get("maximum")
        if (
            not isinstance(label, str) or len(label.strip()) < 3
            or isinstance(minimum, bool) or not isinstance(minimum, (int, float))
            or not math.isfinite(minimum) or abs(minimum) > 1e12
            or isinstance(maximum, bool) or not isinstance(maximum, (int, float))
            or not math.isfinite(maximum) or abs(maximum) > 1e12
            or minimum >= maximum
        ):
            raise GradingUnavailable("Graph axis labels and bounds are invalid")
        axes[axis_id] = (float(minimum), float(maximum))

    points_by_id = {}
    for item in authored_points:
        if (
            not isinstance(item, dict)
            or not isinstance(item.get("id"), str)
            or not re.fullmatch(r"[a-z][a-z0-9_-]{0,47}", item["id"])
            or not isinstance(item.get("label"), str)
            or len(item["label"].strip()) < 2
            or item["id"] in points_by_id
        ):
            raise GradingUnavailable("Graph point labels and IDs must be valid and unique")
        points_by_id[item["id"]] = item

    answers_by_id = {}
    for item in expected_points:
        if (
            not isinstance(item, dict)
            or not isinstance(item.get("id"), str)
            or item["id"] not in points_by_id
            or item["id"] in answers_by_id
        ):
            raise GradingUnavailable("Graph points and answer coordinates must have matching unique IDs")
        for coordinate, axis_id in (("x", "x_axis"), ("y", "y_axis")):
            value = item.get(coordinate)
            tolerance = item.get(f"{coordinate}_tolerance")
            minimum, maximum = axes[axis_id]
            if (
                isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or not minimum <= value <= maximum
                or isinstance(tolerance, bool) or not isinstance(tolerance, (int, float))
                or not math.isfinite(tolerance) or not 0 <= tolerance <= maximum - minimum
            ):
                raise GradingUnavailable("Graph answer coordinates or tolerances are invalid")
        answers_by_id[item["id"]] = item
    if set(points_by_id) != set(answers_by_id):
        raise GradingUnavailable("Every public graph point requires one answer coordinate pair")

    observations_by_id = {}
    for observation in observations:
        if (
            not isinstance(observation, dict)
            or not isinstance(observation.get("id"), str)
            or observation["id"] not in points_by_id
            or observation["id"] in observations_by_id
            or isinstance(observation.get("x"), bool)
            or not isinstance(observation.get("x"), (int, float))
            or not math.isfinite(observation["x"])
            or not axes["x_axis"][0] <= observation["x"] <= axes["x_axis"][1]
            or not isinstance(observation.get("values"), list)
            or not 1 <= len(observation["values"]) <= 100
            or any(
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or not axes["y_axis"][0] <= value <= axes["y_axis"][1]
                for value in observation["values"]
            )
        ):
            raise GradingUnavailable("Graph observations must be finite, bounded, and map to public points")
        observations_by_id[observation["id"]] = observation
    if set(observations_by_id) != set(points_by_id):
        raise GradingUnavailable("Every graph point must have one public observation row")

    criteria_by_id = {}
    for criterion in rubric:
        if (
            not isinstance(criterion, dict)
            or not isinstance(criterion.get("id"), str)
            or not isinstance(criterion.get("criterion"), str)
            or len(criterion["criterion"].strip()) < 10
            or not isinstance(criterion.get("evidence"), list)
            or not criterion["evidence"]
            or any(not isinstance(evidence, str) or len(evidence.strip()) < 3 for evidence in criterion["evidence"])
            or isinstance(criterion.get("points"), bool)
            or not isinstance(criterion.get("points"), (int, float))
            or not math.isfinite(criterion["points"])
            or criterion["points"] <= 0
        ):
            raise GradingUnavailable("Graph analytic rubric criteria are invalid")
        criterion_id = criterion["id"]
        if criterion_id in criteria_by_id:
            raise GradingUnavailable("Graph rubric criterion IDs must be unique")
        criteria_by_id[criterion_id] = criterion

    expected_criteria = {
        f"{point_id}_{coordinate}"
        for point_id in points_by_id
        for coordinate in ("x", "y")
    }
    if set(criteria_by_id) != expected_criteria:
        raise GradingUnavailable("Each graph coordinate must map to one analytic rubric criterion")
    if not math.isclose(
        sum(float(item["points"]) for item in rubric), points, rel_tol=0, abs_tol=1e-8
    ):
        raise GradingUnavailable("Graph rubric points must sum to the question total")

    response = request.response
    if not isinstance(response, dict) or set(response) - expected_criteria:
        return _graph_result(question, points, 0, "malformed_response", [])

    components = []
    score = 0.0
    feedback = question.get("feedback", {})
    lesson_ids = feedback.get("lesson_ids", [])
    for point_id, expected in answers_by_id.items():
        for coordinate in ("x", "y"):
            component_id = f"{point_id}_{coordinate}"
            criterion = criteria_by_id[component_id]
            value = response.get(component_id)
            if value is None:
                components.append(FeedbackComponent(
                    field_id=component_id, label=criterion["criterion"], score=0,
                    max_score=float(criterion["points"]), diagnosis="missing_response",
                ))
                continue
            child_question = {
                "type": "numeric",
                "points": criterion["points"],
                "solution_spec": {
                    "answer": expected[coordinate],
                    "unit": "",
                    "tolerance": expected[f"{coordinate}_tolerance"],
                    "unit_required": False,
                },
                "feedback": {"hint": feedback.get("hint"), "lesson_ids": lesson_ids},
            }
            result = grade(child_question, AttemptRequest(response=value))
            score += result.score
            components.append(FeedbackComponent(
                field_id=component_id, label=criterion["criterion"],
                score=result.score, max_score=float(criterion["points"]),
                diagnosis=result.feedback.diagnosis,
            ))

    # Many fractional coordinate criteria can accumulate binary floating-point
    # noise (for example, thirty 0.2-point entries). Re-sum the components
    # accurately before persisting and displaying the learner's total.
    score = math.fsum(component.score for component in components)
    complete = math.isclose(score, points, rel_tol=0, abs_tol=1e-8)
    diagnosis = "graph_coordinates_complete" if complete else "graph_coordinates_partial" if score else "graph_coordinates_incorrect"
    return _graph_result(question, points, score, diagnosis, components)


def _graph_result(
    question: dict,
    points: float,
    score: float,
    diagnosis: str,
    components: list[FeedbackComponent],
) -> GradeResult:
    authored = question.get("feedback", {})
    lesson_ids = authored.get("lesson_ids", [])
    correct = math.isclose(score, points, rel_tol=0, abs_tol=1e-8)
    return GradeResult(
        score=score,
        max_score=points,
        correct=correct,
        feedback=Feedback(
            diagnosis=diagnosis,
            hint=None if correct else authored.get("hint"),
            misconception=None if correct else authored.get("misconception"),
            lesson_id=lesson_ids[0] if lesson_ids else None,
            next_step=(
                "Every plotted coordinate matched within its authored tolerance. Axis selection and scientific interpretation were not assessed."
                if correct else
                "Each x and y coordinate is scored separately. Check the source pairs, the point labels, and the units printed on both axes."
            ),
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
    if question["type"] in {"data_interpretation", "structured"}:
        return _grade_fielded_response(question, request, points)
    if question["type"] == "graph":
        return _grade_graph_response(question, request, points)
    if question["type"] == "file_upload":
        return _grade_csv_upload(question, request, points)
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
