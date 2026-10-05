import pytest

from courselab.variants import (
    VariantTokenError,
    issue_variant_token,
    resolve_variant,
    verify_variant_token,
)

SECRET = b"test-signing-key-with-more-than-thirty-two-bytes"
QUESTION = {
    "id": "variant-choice",
    "type": "single_choice",
    "prompt": "Which mechanism best explains the observed difference?",
    "options": ["A", "B"],
    "points": 1,
    "solution_spec": {"answer": 0},
    "feedback": {"hint": "Compare mechanisms carefully.", "solution": "A is supported."},
    "randomization": {
        "seeded": True,
        "generator_id": "authored-variants-v1",
        "variants": [
            {
                "id": "condition-b",
                "prompt": "Which mechanism best explains the second condition?",
                "options": ["B", "A"],
                "solution_spec": {"answer": 0},
                "feedback": {"hint": "Inspect the second condition.", "solution": "B is supported."},
            }
        ],
    },
}


def test_issued_variant_replays_the_same_complete_specification():
    token, variant_id, selected = issue_variant_token(QUESTION, "course", "1.2.0", SECRET, now=100)
    assert token
    assert variant_id in {"base", "condition-b"}
    replay, replay_id = verify_variant_token(QUESTION, "course", "1.2.0", token, SECRET, now=101)
    assert replay_id == variant_id
    assert replay == selected
    assert "randomization" not in replay


@pytest.mark.parametrize("course,version", [("other-course", "1.2.0"), ("course", "1.2.1")])
def test_token_is_bound_to_course_and_content_version(course, version):
    token, _, _ = issue_variant_token(QUESTION, "course", "1.2.0", SECRET, now=100)
    with pytest.raises(VariantTokenError):
        verify_variant_token(QUESTION, course, version, token, SECRET, now=101)


def test_token_rejects_tampering_expiry_and_missing_value():
    token, _, _ = issue_variant_token(QUESTION, "course", "1.2.0", SECRET, now=100)
    with pytest.raises(VariantTokenError):
        verify_variant_token(QUESTION, "course", "1.2.0", token[:-1] + "x", SECRET, now=101)
    with pytest.raises(VariantTokenError):
        verify_variant_token(QUESTION, "course", "1.2.0", token, SECRET, now=100 + 7 * 24 * 60 * 60)
    with pytest.raises(VariantTokenError):
        verify_variant_token(QUESTION, "course", "1.2.0", None, SECRET, now=101)


def test_nonrandomized_question_needs_no_token_and_rejects_one():
    question = {key: value for key, value in QUESTION.items() if key != "randomization"}
    selected, variant_id = verify_variant_token(question, "course", "1.2.0", None, SECRET)
    assert selected == question and variant_id is None
    with pytest.raises(VariantTokenError):
        verify_variant_token(question, "course", "1.2.0", "unexpected", SECRET)


def test_variant_resolution_does_not_mutate_the_authored_bank():
    before = QUESTION["solution_spec"].copy()
    resolved = resolve_variant(QUESTION, "condition-b")
    assert resolved["solution_spec"] == {"answer": 0}
    assert resolved["prompt"] != QUESTION["prompt"]
    assert QUESTION["solution_spec"] == before
