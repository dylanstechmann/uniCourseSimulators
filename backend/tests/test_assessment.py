from datetime import datetime, timedelta
from decimal import Decimal

import pytest

from courselab.assessment import calculate_weighted_grade, validate_assessment_configuration

AS_OF = datetime(2026, 10, 6, 12, 0)


def course_fixture(aggregation="points"):
    policy = {
        "mode": "graded-course",
        "categories": [
            {"id": "homework", "weight": 0.6},
            {"id": "exam", "weight": 0.4},
        ],
        "category_aggregation": aggregation,
    }
    assessments = [
        {
            "id": "hw-a", "mode": "graded", "category_id": "homework", "points": 5,
            "attempt_limit": 2, "attempt_scoring": "highest", "release_at": "2026-10-01T00:00:00Z",
            "due_at": "2026-10-07T00:00:00Z",
        },
        {
            "id": "hw-b", "mode": "graded", "category_id": "homework", "points": 15,
            "attempt_limit": 2, "attempt_scoring": "latest", "release_at": "2026-10-01T00:00:00Z",
            "due_at": "2026-10-06T12:00:00Z",
        },
        {
            "id": "exam", "mode": "graded", "category_id": "exam", "points": 10,
            "attempt_limit": 1, "attempt_scoring": "latest", "due_at": "2026-10-05T23:00:00Z",
        },
        {
            "id": "future", "mode": "graded", "category_id": "exam", "points": 10,
            "release_at": "2026-10-07T00:00:00Z", "due_at": "2026-10-08T00:00:00Z",
        },
    ]
    return assessments, policy


def test_decimal_weighted_grade_is_reproducible_and_deadline_boundary_is_on_time():
    assessments, policy = course_fixture()
    attempts = {
        "hw-a": [
            {"score": 3, "max_score": 5, "submitted_at": "2026-10-02T12:00:00Z"},
            {"score": 4, "max_score": 5, "submitted_at": "2026-10-03T12:00:00Z"},
        ]
    }
    result = calculate_weighted_grade(assessments, policy, attempts, AS_OF)
    assert result == calculate_weighted_grade(assessments, policy, attempts, AS_OF)
    assert result["score_percent"] == Decimal("48.00")
    assert result["category_scores"] == {"homework": Decimal("80.00"), "exam": Decimal("0.00")}
    assert result["active_weight"] == Decimal("1.0")

    after_due = calculate_weighted_grade(
        assessments, policy, attempts, AS_OF + timedelta(microseconds=1)
    )
    assert after_due["score_percent"] == Decimal("12.00")
    assert after_due["category_scores"]["homework"] == Decimal("20.00")


def test_attempt_selection_and_assessment_average_are_configurable():
    assessments, policy = course_fixture("assessment-average")
    assessments = [*assessments[:2], assessments[3]]
    attempts = {
        "hw-a": [
            {"id": "1", "score": 2, "max_score": 5, "submitted_at": "2026-10-02T12:00:00Z"},
            {"id": "2", "score": 4, "max_score": 5, "submitted_at": "2026-10-03T12:00:00Z"},
        ],
        "hw-b": [
            {"score": 7, "max_score": 15, "submitted_at": "2026-10-02T12:00:00Z"},
            {"score": 10, "max_score": 15, "submitted_at": "2026-10-03T12:00:00Z"},
        ],
    }
    # hw-a uses highest (80%); hw-b uses latest (10/15). Only homework is active,
    # so its configured 60% category weight is normalized for a current grade.
    result = calculate_weighted_grade(assessments, policy, attempts, AS_OF)
    assert result["category_scores"]["homework"] == Decimal("73.33")
    assert result["score_percent"] == Decimal("73.33")
    assert result["active_weight"] == Decimal("0.6")


@pytest.mark.parametrize(
    "change,message",
    [
        ("bad_weights", "sum exactly to one"),
        ("missing_category", "valid grade category"),
        ("bad_schedule", "due before it is released"),
        ("boolean_limit", "positive integer"),
        ("duplicate_ids", "IDs must be nonempty and unique"),
    ],
)
def test_invalid_semester_assessment_policies_fail_closed(change, message):
    assessments, policy = course_fixture()
    if change == "bad_weights":
        policy["categories"][0]["weight"] = 0.61
    elif change == "missing_category":
        assessments[0]["category_id"] = "unknown"
    elif change == "bad_schedule":
        assessments[0]["release_at"] = "2026-10-08T00:00:00Z"
    elif change == "boolean_limit":
        assessments[0]["attempt_limit"] = True
    elif change == "duplicate_ids":
        assessments[1]["id"] = assessments[0]["id"]
    with pytest.raises(ValueError, match=message):
        validate_assessment_configuration(assessments, policy)


def test_formative_only_courses_never_receive_a_course_grade():
    with pytest.raises(ValueError, match="no weighted course grade"):
        calculate_weighted_grade([], {"mode": "formative-only", "categories": []}, {}, AS_OF)


@pytest.mark.parametrize(
    "attempts,message",
    [
        ({"hw-a": [{"score": 6, "max_score": 5, "submitted_at": "2026-10-02T12:00:00Z"}]}, "outside its configured points"),
        ({"missing": []}, "unknown assessment"),
        ({"hw-a": [
            {"score": 2, "max_score": 5, "submitted_at": "2026-10-02T12:00:00Z"},
            {"score": 3, "max_score": 5, "submitted_at": "2026-10-03T12:00:00Z"},
            {"score": 4, "max_score": 5, "submitted_at": "2026-10-04T12:00:00Z"},
        ]}, "exceeds its attempt limit"),
    ],
)
def test_bad_saved_grades_are_rejected(attempts, message):
    assessments, policy = course_fixture()
    with pytest.raises(ValueError, match=message):
        calculate_weighted_grade(assessments, policy, attempts, AS_OF)


def test_late_attempt_is_not_counted_after_the_strict_deadline():
    assessments, policy = course_fixture()
    attempts = {
        "hw-a": [{
            "score": 3, "max_score": 5, "submitted_at": "2026-10-07T00:00:01Z",
        }]
    }
    with pytest.raises(ValueError, match="after its deadline"):
        calculate_weighted_grade(assessments, policy, attempts, "2026-10-08T00:00:00Z")


def test_unsupported_late_work_policies_are_rejected():
    assessments, policy = course_fixture()
    policy["late_submission_policy"] = "accept-with-penalty"
    with pytest.raises(ValueError, match="strict-deadline"):
        validate_assessment_configuration(assessments, policy)


def test_objective_evidence_reports_authored_objectives_without_items():
    from courselab.evidence import objective_evidence

    questions = [{"id": "q1", "points": 2, "objective_ids": ["tagged"]}]
    result = objective_evidence(questions, [], authored_objective_ids=["tagged", "untagged"])

    assert result["tagged"]["status"] == "no_evidence"
    assert result["untagged"] == {
        "attempts": 0,
        "correct_results": 0,
        "attempted_items": 0,
        "item_count": 0,
        "best_score": 0.0,
        "best_possible_score": 0.0,
        "performance": None,
        "status": "no_items",
    }
    assert "untagged" not in objective_evidence(questions, [])
