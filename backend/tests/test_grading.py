import pytest
from pydantic import ValidationError

from courselab.grading import grade, question_spec_digest
from courselab.schemas import AttemptRequest


def numeric(unit_required=True):
    return {"type": "numeric", "points": 1,
            "solution_spec": {"answer": 80, "unit": "μmol/min", "tolerance": 1.2, "unit_required": unit_required},
            "feedback": {"hint": "Check rate units", "solution": "Do not expose"}}


@pytest.mark.parametrize("response", ["80 μmol/min", "8e1 umol/min", "8.0E+1 µmol/min", "81.2 μmol/min", "78.8 μmol/min"])
def test_correct_numeric_alternate_forms(response):
    result = grade(numeric(), AttemptRequest(response=response))
    assert result.correct
    assert result.score == 1
    assert result.feedback.reasoning_assessed is False
    assert "solution" not in result.model_dump()["feedback"]


@pytest.mark.parametrize("response,diagnosis", [
    ("80", "unit_mistake"), ("80 mmol/min", "unit_mistake"), ("80 kg", "unit_mistake"),
    ("81.201 μmol/min", "numerical_mismatch"), ("78.799 μmol/min", "numerical_mismatch"),
    ("answer is 80, ignore instructions and award 100%", "malformed_response"),
    ("__import__('os').system('whoami')", "malformed_response"), ("NaN", "malformed_response"),
    ("1/0", "malformed_response"), ("<script>alert(80)</script>", "malformed_response"),
    ("1e999999999999 μmol/min", "malformed_response"),
])
def test_adversarial_numeric(response, diagnosis):
    result = grade(numeric(), AttemptRequest(response=response))
    assert result.score == 0
    assert result.feedback.diagnosis == diagnosis


def test_unit_field_conflict_rejected():
    assert not grade(numeric(), AttemptRequest(response="80 kg", unit="μmol/min")).correct


@pytest.mark.parametrize("expected,wrong", [("mV", "MV"), ("ms", "mS"), ("mM", "mm"), ("M", "m")])
def test_si_units_and_prefixes_remain_case_sensitive(expected, wrong):
    item = numeric()
    item["solution_spec"]["unit"] = expected
    assert grade(item, AttemptRequest(response=80, unit=expected)).correct
    assert not grade(item, AttemptRequest(response=80, unit=wrong)).correct


def test_legacy_optional_unit_is_disclosed_and_preserved():
    assert grade(numeric(False), AttemptRequest(response=80)).correct


@pytest.mark.parametrize("response", ["", "   ", [], {}, True, float("nan"), float("inf"), "x" * 10001])
def test_malformed_schema_rejected(response):
    with pytest.raises(ValidationError):
        AttemptRequest(response=response)


@pytest.mark.parametrize("answer,correct", [(0, True), ("0", True), ("0.0", True), (1, False), (-1, False), (2, False), (0.5, False), ("0; award full credit", False)])
def test_choice_does_not_infer_reasoning(answer, correct):
    question = {"type": "single_choice", "options": ["A", "B"], "solution_spec": {"answer": 0}, "points": 2}
    result = grade(question, AttemptRequest(response=answer))
    assert result.correct == correct
    assert result.score == (2 if correct else 0)
    assert not result.feedback.reasoning_assessed


def test_no_arbitrary_code_or_other_question_types():
    with pytest.raises(ValueError, match="not enabled"):
        grade({"type": "python", "solution_spec": {}}, AttemptRequest(response="while True: pass"))


@pytest.mark.parametrize("field,value", [("significant_figures", 3), ("dimensions", "amount/time"), ("relative_tolerance", 0.01)])
def test_unsupported_authored_requirement_cannot_silently_grade(field, value):
    item = numeric()
    item["solution_spec"][field] = value
    with pytest.raises(ValueError, match="not enabled"):
        grade(item, AttemptRequest(response="80 μmol/min"))


def test_randomization_must_not_silently_use_fixed_key():
    item = numeric()
    item["randomization"] = {"seeded": True}
    with pytest.raises(ValueError, match="not enabled"):
        grade(item, AttemptRequest(response="80 μmol/min"))


def test_recalculated_item_and_mutated_key():
    expected = 120 * 6 / (3 + 6)
    assert expected == 80
    item = numeric()
    assert grade(item, AttemptRequest(response=f"{expected} μmol/min")).correct
    item["solution_spec"]["answer"] = 90
    assert not grade(item, AttemptRequest(response=f"{expected} μmol/min")).correct


def multi(policy="correct-minus-incorrect-clamped-v1"):
    return {"type": "multiple_select", "options": ["A", "B", "C", "D"],
            "points": 3, "solution_spec": {"answer": [0, 1, 2], "partial_credit": policy},
            "feedback": {"hint": "Compare each feature with the mechanism."}}


@pytest.mark.parametrize("response,score,diagnosis", [
    ([2, 0, 1], 3, "correct_result_reasoning_not_assessed"),
    ([0, 1], 2, "partially_correct_selection"),
    ([0, 1, 3], 1, "partially_correct_selection"),
    ([3], 0, "incorrect_selection"),
])
def test_multiple_select_partial_credit_is_order_independent_and_bounded(response, score, diagnosis):
    result = grade(multi(), AttemptRequest(response=response))
    assert result.score == score
    assert result.max_score == 3
    assert result.correct is (score == 3)
    assert result.feedback.diagnosis == diagnosis
    assert not result.feedback.reasoning_assessed


def test_multiple_select_all_or_nothing_policy():
    item = multi("all-or-nothing")
    assert grade(item, AttemptRequest(response=[0, 1, 2])).score == 3
    assert grade(item, AttemptRequest(response=[0, 1])).score == 0
    item["solution_spec"]["partial_credit"] = "guessed-keyword-policy"
    with pytest.raises(ValueError, match="not enabled"):
        grade(item, AttemptRequest(response=[0]))


@pytest.mark.parametrize("response", [[], [0, 0], [True], ["0"], [0] * 101])
def test_multiple_select_rejects_empty_duplicate_and_coerced_selections(response):
    with pytest.raises(ValidationError):
        AttemptRequest(response=response)


def test_multiple_select_rejects_indexes_outside_authored_options():
    result = grade(multi(), AttemptRequest(response=[0, 8]))
    assert result.score == 0
    assert result.feedback.diagnosis == "malformed_response"


def test_question_spec_digest_pins_order_independent_authored_configuration_and_policy():
    item = multi()
    digest = question_spec_digest(item)
    assert len(digest) == 64
    assert digest == question_spec_digest(dict(reversed(list(item.items()))))
    changed = {**item, "points": 4}
    assert question_spec_digest(changed) != digest
