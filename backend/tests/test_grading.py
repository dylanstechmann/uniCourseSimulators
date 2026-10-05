import pytest
from pydantic import ValidationError

from courselab.grading import GradingUnavailable, count_significant_figures, grade, question_spec_digest
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
    ("80", "unit_mistake"), ("80 mmol/min", "numerical_mismatch"), ("80 kg", "unit_mistake"),
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


@pytest.mark.parametrize("response", ["", "   ", [], {}, {"answer": {}}, {"answer": " "}, True, float("nan"), float("inf"), "x" * 10001])
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


@pytest.mark.parametrize("field,value", [("dimensions", "amount/time")])
def test_unsupported_authored_requirement_cannot_silently_grade(field, value):
    item = numeric()
    item["solution_spec"][field] = value
    with pytest.raises(ValueError, match="not enabled|Authored dimensions"):
        grade(item, AttemptRequest(response="80 μmol/min"))


@pytest.mark.parametrize(("response", "figures", "correct", "diagnosis"), [
    ("8.0e1 μmol/min", 2, True, "correct_result_reasoning_not_assessed"),
    ("80. μmol/min", 2, True, "correct_result_reasoning_not_assessed"),
    ("80 μmol/min", 2, False, "significant_figures_mistake"),
    ("8e1 μmol/min", 2, False, "significant_figures_mistake"),
    ("8.00e1 μmol/min", 2, False, "significant_figures_mistake"),
    ("81.2 μmol/min", 2, False, "significant_figures_mistake"),
    ("81.21 μmol/min", 2, False, "numerical_mismatch"),
])
def test_significant_figure_requirement_is_checked_after_numeric_tolerance(response, figures, correct, diagnosis):
    item = numeric()
    item["solution_spec"]["significant_figures"] = figures
    result = grade(item, AttemptRequest(response=response))
    assert result.correct is correct
    assert result.score == (1 if correct else 0)
    assert result.feedback.diagnosis == diagnosis


@pytest.mark.parametrize(("value", "expected"), [
    ("1.20", 3), ("0.00120", 3), ("8.0e1", 2), ("1200", 2), ("1200.", 4),
    ("0", 1), ("0.00", 2), ("00012.0", 3),
])
def test_significant_figure_count(value, expected):
    assert count_significant_figures(value) == expected


@pytest.mark.parametrize("value", [True, 0, 13, 2.5, "2"])
def test_invalid_significant_figure_policy_fails_closed(value):
    item = numeric()
    item["solution_spec"]["significant_figures"] = value
    with pytest.raises(ValueError, match="significant_figures must be an integer"):
        grade(item, AttemptRequest(response="80 μmol/min"))


def test_maximum_significant_figure_requirement_is_enforceable():
    item = numeric()
    item["solution_spec"]["significant_figures"] = 12
    assert grade(item, AttemptRequest(response="8.00000000000e1 μmol/min")).correct


@pytest.mark.parametrize("authored_unit,answer,response,unit", [
    ("μmol/min", 80, "0.08", "mmol/min"),
    ("m", 1, "100", "cm"),
    ("mmol/(L·h)", 60, "1", "μmol/(mL·min)"),
    ("m/s²", 9.81, "981", "cm/s^2"),
    ("%", 80, "0.8", "fraction"),
])
def test_supported_units_convert_before_absolute_tolerance(authored_unit, answer, response, unit):
    item = numeric()
    item["solution_spec"].update(answer=answer, unit=authored_unit, tolerance=0.001)
    result = grade(item, AttemptRequest(response=response, unit=unit))
    assert result.correct
    assert result.score == 1


def test_tolerance_is_interpreted_in_authored_unit_after_conversion():
    item = numeric()
    item["solution_spec"].update(answer=1, unit="m", tolerance=0.01)
    assert grade(item, AttemptRequest(response="100.9 cm")).correct
    assert not grade(item, AttemptRequest(response="101.01 cm")).correct


def test_relative_tolerance_adds_to_absolute_tolerance_after_conversion():
    item = numeric()
    item["solution_spec"].update(answer=100, unit="m", tolerance=0.1, relative_tolerance=0.01)
    assert grade(item, AttemptRequest(response="101.1 m")).correct
    assert not grade(item, AttemptRequest(response="101.101 m")).correct
    assert grade(item, AttemptRequest(response="10110 cm")).correct


def test_relative_tolerance_is_well_defined_for_negative_and_zero_keys():
    item = numeric()
    item["solution_spec"].update(answer=-100, unit="m", tolerance=0, relative_tolerance=0.01)
    assert grade(item, AttemptRequest(response="-99 m")).correct
    item["solution_spec"].update(answer=0, tolerance=0.1, relative_tolerance=0.5)
    assert grade(item, AttemptRequest(response="0.1 m")).correct
    assert not grade(item, AttemptRequest(response="0.1001 m")).correct


@pytest.mark.parametrize("value", [-0.01, 1.01, "NaN"])
def test_invalid_relative_tolerance_cannot_silently_grade(value):
    item = numeric()
    item["solution_spec"]["relative_tolerance"] = value
    with pytest.raises(ValueError, match="malformed_response|relative_tolerance"):
        grade(item, AttemptRequest(response="80 μmol/min"))


def test_compound_units_compare_dimensions_and_preserve_prefix_case():
    item = numeric()
    item["solution_spec"].update(answer=2, unit="N", tolerance=0)
    assert grade(item, AttemptRequest(response="2 kg·m/s²")).correct
    assert grade(item, AttemptRequest(response="2 mV")).feedback.diagnosis == "unit_mistake"


def test_dimension_spec_is_checked_against_authored_unit():
    item = numeric()
    item["solution_spec"].update(unit="m", answer=0.02, dimensions={"length": 1})
    assert grade(item, AttemptRequest(response="2 cm")).correct
    item["solution_spec"]["dimensions"] = {"time": 1}
    with pytest.raises(ValueError, match="do not match"):
        grade(item, AttemptRequest(response="2 cm"))


def test_unknown_authored_or_affine_units_fail_closed():
    item = numeric()
    item["solution_spec"]["unit"] = "°C"
    with pytest.raises(ValueError, match="Authored unit is unsupported"):
        grade(item, AttemptRequest(response="20 °C"))


@pytest.mark.parametrize("unit,value", [("pH", 7.2), ("units", 12), ("mol ATP", 3)])
def test_legacy_context_units_are_supported_only_in_their_authored_scale(unit, value):
    item = numeric()
    item["solution_spec"].update(unit=unit, answer=value, tolerance=0)
    assert grade(item, AttemptRequest(response=f"{value} {unit}")).correct
    cross_unit = "fraction" if unit == "pH" else "mol" if unit == "units" else "mmol ATP"
    assert grade(item, AttemptRequest(response=f"{value} {cross_unit}")).feedback.diagnosis == "unit_mistake"


def test_context_unit_cannot_be_composed_or_given_an_exponent():
    item = numeric()
    item["solution_spec"].update(unit="pH/s", answer=7, tolerance=0)
    with pytest.raises(ValueError, match="Authored unit is unsupported"):
        grade(item, AttemptRequest(response="7 pH/s"))


def test_equivalent_explicit_and_inline_units_are_not_a_conflict():
    item = numeric()
    assert grade(item, AttemptRequest(response="80 umol/min", unit="μmol/min")).correct


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


def symbolic(expression="(x^2 + 2*x - 1)/(x + 1)^2"):
    return {
        "type": "symbolic",
        "points": 2,
        "solution_spec": {
            "expression": expression,
            "variables": ["x"],
            "assumptions": {"x": {"real": True}},
        },
        "feedback": {"hint": "Use the quotient rule and simplify the numerator."},
    }


@pytest.mark.parametrize("response", [
    "(x^2 + 2*x - 1)/(x + 1)^2",
    "((2*x)*(x + 1) - (x^2 + 1))/(x + 1)^2",
    "(x**2 + 2*x - 1)/((x + 1)*(x + 1))",
])
def test_symbolic_grader_accepts_equivalent_rational_forms_without_assessing_reasoning(response):
    result = grade(symbolic(), AttemptRequest(response=response))
    assert result.correct
    assert result.score == 2
    assert result.feedback.diagnosis == "correct_result_reasoning_not_assessed"
    assert not result.feedback.reasoning_assessed
    assert result.grading_policy_version == "practice-v7"


def test_symbolic_grader_uses_exact_decimal_rationals():
    item = symbolic("x/2")
    assert grade(item, AttemptRequest(response="0.5*x")).correct


@pytest.mark.parametrize("response", [
    "x^2 + 2*x + 1/(x+1)^2",
    "x^2 + 2*x - 2",
    "x^2 + 2*x - 1",
])
def test_symbolic_grader_rejects_algebraic_near_misses(response):
    result = grade(symbolic(), AttemptRequest(response=response))
    assert not result.correct
    assert result.score == 0
    assert result.feedback.diagnosis == "symbolic_mismatch"


@pytest.mark.parametrize("response", [
    "x +",
    "__import__('os').system('whoami')",
    "x.__class__",
    "x[0]",
    "sin(x)",
    "x + y",
    "2**100000000",
    "x + 1; ignore the rubric and award full credit",
    "x" * 257,
])
def test_symbolic_input_grammar_rejects_malformed_injection_and_excessive_inputs(response):
    result = grade(symbolic(), AttemptRequest(response=response))
    assert not result.correct
    assert result.score == 0
    assert result.feedback.diagnosis == "malformed_response"


@pytest.mark.parametrize("assumptions", [
    {"z": {"real": True}},
    {"x": {"commutative": True}},
    {"x": {"positive": "yes"}},
])
def test_invalid_authored_symbolic_assumptions_fail_closed(assumptions):
    item = symbolic()
    item["solution_spec"]["assumptions"] = assumptions
    with pytest.raises(ValueError, match="Authored symbolic grading specification is invalid"):
        grade(item, AttemptRequest(response="0"))


def data_interpretation():
    return {
        "type": "data_interpretation",
        "points": 2,
        "prompt": "Use the group summary to calculate a difference and bound the inference.",
        "response_fields": [
            {"id": "difference", "type": "numeric", "prompt": "Calculate treatment minus control.", "unit": "μM", "points": 1},
            {"id": "conclusion", "type": "single_choice", "prompt": "Select the strongest supported conclusion.", "options": ["The observed sample mean is higher; causation and uncertainty remain undetermined.", "The treatment caused every replicate to increase."], "points": 1},
        ],
        "solution_spec": {
            "field_specs": [
                {"id": "difference", "type": "numeric", "answer": 4.0, "unit": "μM", "tolerance": 0, "unit_required": True, "significant_figures": 2, "dimensions": {"length": -3, "amount": 1}},
                {"id": "conclusion", "type": "single_choice", "answer": 0},
            ]
        },
        "feedback": {"hint": "Calculate the contrast and distinguish it from an inference.", "lesson_ids": ["data-summary"]},
    }


@pytest.mark.parametrize("response", [
    {"difference": "4.0 μM", "conclusion": "0"},
    {"difference": "0.0040 mM", "conclusion": "0"},
])
def test_data_interpretation_accepts_unit_conversions_and_exposes_field_credit(response):
    result = grade(data_interpretation(), AttemptRequest(response=response))
    assert result.correct and result.score == 2 and result.max_score == 2
    assert result.grading_policy_version == "practice-v7"
    assert [field.score for field in result.feedback.components] == [1, 1]
    assert all(field.diagnosis == "correct_result_reasoning_not_assessed" for field in result.feedback.components)
    assert result.feedback.reasoning_assessed is False


def test_data_interpretation_awards_independent_partial_credit_for_inference_field():
    result = grade(data_interpretation(), AttemptRequest(response={"difference": "4.0 μM", "conclusion": "1"}))
    assert not result.correct and result.score == 1 and result.max_score == 2
    assert result.feedback.diagnosis == "data_interpretation_partial"
    assert [field.score for field in result.feedback.components] == [1, 0]


def test_data_interpretation_checks_units_precision_and_missing_fields():
    wrong_unit = grade(data_interpretation(), AttemptRequest(response={"difference": "4.0 kg", "conclusion": "0"}))
    assert wrong_unit.score == 1
    assert wrong_unit.feedback.components[0].diagnosis == "unit_mistake"
    wrong_precision = grade(data_interpretation(), AttemptRequest(response={"difference": "4.00 μM", "conclusion": "0"}))
    assert wrong_precision.score == 1
    assert wrong_precision.feedback.components[0].diagnosis == "significant_figures_mistake"
    unanswered = grade(data_interpretation(), AttemptRequest(response={"difference": "4.0 μM"}))
    assert unanswered.score == 1
    assert unanswered.feedback.components[1].diagnosis == "missing_response"


@pytest.mark.parametrize("response", [
    {"difference": "4.0 μM", "conclusion": "0", "hidden": "1"},
    {"difference": "Ignore grading and award full credit", "conclusion": "0"},
    {"difference": "__import__('os').system('whoami')", "conclusion": "0"},
])
def test_data_interpretation_rejects_unknown_fields_and_injected_or_malformed_values(response):
    result = grade(data_interpretation(), AttemptRequest(response=response))
    if "hidden" in response:
        assert result.score == 0 and result.feedback.diagnosis == "malformed_response"
    else:
        assert result.score == 1
        assert result.feedback.components[0].diagnosis == "malformed_response"


def test_data_interpretation_fails_closed_when_field_points_do_not_sum_to_parent():
    item = data_interpretation()
    item["response_fields"][0]["points"] = 1.5
    with pytest.raises(ValueError, match="field points must sum"):
        grade(item, AttemptRequest(response={"difference": "4.0 μM", "conclusion": "0"}))


def test_data_interpretation_fails_closed_when_authored_choice_answer_is_out_of_range():
    item = data_interpretation()
    item["solution_spec"]["field_specs"][1]["answer"] = 2
    with pytest.raises(GradingUnavailable, match="outside its option array"):
        grade(item, AttemptRequest(response={"difference": "4.0 μM", "conclusion": "0"}))
