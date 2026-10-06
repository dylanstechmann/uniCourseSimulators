"""Versioned assessment policy validation and deterministic weighted-grade math.

This module handles course policy only. It does not grade learner responses or
load answer keys; protected assignment delivery is a later capability.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from typing import Any


def utc_datetime(value: str | datetime | None) -> datetime | None:
    """Parse an ISO timestamp as UTC and return the database's naive UTC form."""
    if value is None or value == "":
        return None
    if isinstance(value, str):
        value = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.tzinfo is None:
        return value
    return value.astimezone(timezone.utc).replace(tzinfo=None)


def canonical_digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                         allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_assessment_configuration(assessments: list[dict], policy: dict) -> None:
    """Reject inconsistent categories, schedules, or attempt rules before persistence."""
    mode = policy.get("mode")
    if mode not in {"formative-only", "graded-course"}:
        raise ValueError("Unknown grading mode")

    categories = policy.get("categories", [])
    if not isinstance(categories, list):
        raise ValueError("Grade categories must be a list")
    category_ids: set[str] = set()
    total_weight = Decimal(0)
    for category in categories:
        category_id = category.get("id")
        if not isinstance(category_id, str) or not category_id or category_id in category_ids:
            raise ValueError("Grade category IDs must be nonempty and unique")
        category_ids.add(category_id)
        try:
            weight = Decimal(str(category.get("weight")))
        except (InvalidOperation, TypeError):
            raise ValueError(f"Category {category_id} has an invalid weight") from None
        if not weight.is_finite() or weight < 0 or weight > 1:
            raise ValueError(f"Category {category_id} weight must be between zero and one")
        total_weight += weight

    if mode == "formative-only":
        if categories:
            raise ValueError("Formative-only courses cannot define course-grade categories")
    elif not categories or total_weight != Decimal(1):
        raise ValueError("Graded-course category weights must sum exactly to one")

    aggregation = policy.get("category_aggregation", "points")
    if aggregation not in {"points", "assessment-average"}:
        raise ValueError("Category aggregation must be points or assessment-average")

    assessment_ids: set[str] = set()
    category_usage: set[str] = set()
    graded_count = 0
    for item in assessments:
        assessment_id = item.get("id")
        if not isinstance(assessment_id, str) or not assessment_id or assessment_id in assessment_ids:
            raise ValueError("Assessment IDs must be nonempty and unique")
        assessment_ids.add(assessment_id)
        item_mode = item.get("mode")
        if item_mode not in {"practice", "graded", "self-assessment"}:
            raise ValueError(f"Assessment {assessment_id} has an unknown mode")
        if mode == "formative-only" and item_mode == "graded":
            raise ValueError("Formative-only courses cannot contain graded assignments")
        if item_mode == "graded":
            graded_count += 1
            category_id = item.get("category_id")
            if category_id not in category_ids:
                raise ValueError(f"Graded assessment {assessment_id} requires a valid grade category")
            category_usage.add(category_id)
        elif item.get("category_id") is not None:
            raise ValueError(f"Non-graded assessment {assessment_id} cannot count toward a course grade")

        try:
            points = Decimal(str(item.get("points")))
        except (InvalidOperation, TypeError):
            raise ValueError(f"Assessment {assessment_id} has invalid points") from None
        if not points.is_finite() or points < 0 or (item_mode == "graded" and points <= 0):
            raise ValueError(f"Assessment {assessment_id} has invalid points")

        limit = item.get("attempt_limit")
        if limit is not None and (type(limit) is not int or limit < 1):
            raise ValueError(f"Assessment {assessment_id} attempt limit must be a positive integer or null")
        if item.get("attempt_scoring", "highest") not in {"highest", "latest"}:
            raise ValueError(f"Assessment {assessment_id} attempt scoring must be highest or latest")
        try:
            release_at = utc_datetime(item.get("release_at"))
            due_at = utc_datetime(item.get("due_at"))
        except (TypeError, ValueError):
            raise ValueError(f"Assessment {assessment_id} contains an invalid ISO timestamp") from None
        if release_at and due_at and due_at < release_at:
            raise ValueError(f"Assessment {assessment_id} is due before it is released")

        for field in ("question_ids", "objective_ids"):
            values = item.get(field, [])
            if not isinstance(values, list) or len(values) != len(set(values)):
                raise ValueError(f"Assessment {assessment_id} {field} must contain unique values")

    if mode == "graded-course":
        if graded_count == 0:
            raise ValueError("Graded-course policy requires at least one graded assignment")
        if category_usage != category_ids:
            raise ValueError("Every grade category must be used by a graded assessment")


def _attempt_time(attempt: dict) -> datetime:
    try:
        submitted_at = utc_datetime(attempt.get("submitted_at"))
    except (TypeError, ValueError):
        raise ValueError("Assessment attempt has an invalid submission time") from None
    if submitted_at is None:
        raise ValueError("Assessment attempt requires submitted_at")
    return submitted_at


def calculate_weighted_grade(
    assessments: list[dict],
    policy: dict,
    attempts_by_assessment: dict[str, list[dict]],
    as_of: str | datetime,
) -> dict:
    """Calculate an exact weighted percentage from scored assignments.

    Upcoming work is excluded. Missing released work enters the denominator as
    zero only strictly after its deadline; an attempt exactly at its due time is
    on time. Active category weights are normalized for the current-to-date
    percentage, while configured course weights remain unchanged in the plan.
    """
    validate_assessment_configuration(assessments, policy)
    if policy["mode"] != "graded-course":
        raise ValueError("A formative-only course has no weighted course grade")
    current = utc_datetime(as_of)
    if current is None:
        raise ValueError("Grade calculation requires a reference time")

    assessment_ids = {item["id"] for item in assessments}
    unexpected_assessments = set(attempts_by_assessment) - assessment_ids
    if unexpected_assessments:
        raise ValueError("Saved attempts reference an unknown assessment")

    categories = policy["categories"]
    aggregation = policy.get("category_aggregation", "points")
    category_values: dict[str, list[tuple[Decimal, Decimal]]] = {
        category["id"]: [] for category in categories
    }
    for item in assessments:
        if item["mode"] != "graded":
            if attempts_by_assessment.get(item["id"]):
                raise ValueError(f"Non-graded assessment {item['id']} cannot have course-grade attempts")
            continue
        release_at = utc_datetime(item.get("release_at"))
        due_at = utc_datetime(item.get("due_at"))
        if release_at and current < release_at:
            continue
        try:
            points = Decimal(str(item["points"]))
        except (InvalidOperation, TypeError):
            raise ValueError(f"Assessment {item['id']} has invalid points") from None

        attempts = attempts_by_assessment.get(item["id"], [])
        chronological = sorted(attempts, key=lambda attempt: (_attempt_time(attempt), str(attempt.get("id", ""))))
        if release_at and any(_attempt_time(attempt) < release_at for attempt in chronological):
            raise ValueError(f"Assessment {item['id']} has an attempt before release")
        if any(_attempt_time(attempt) > current for attempt in chronological):
            raise ValueError(f"Assessment {item['id']} has an attempt after the calculation time")
        if due_at and any(_attempt_time(attempt) > due_at for attempt in chronological):
            raise ValueError(f"Assessment {item['id']} has an attempt after its deadline")
        limit = item.get("attempt_limit")
        if limit is not None and len(chronological) > limit:
            raise ValueError(f"Assessment {item['id']} exceeds its attempt limit")

        if not chronological:
            if due_at is None or current <= due_at:
                continue
            earned = Decimal(0)
        else:
            for attempt in chronological:
                try:
                    score = Decimal(str(attempt.get("score")))
                    max_score = Decimal(str(attempt.get("max_score")))
                except (InvalidOperation, TypeError):
                    raise ValueError(f"Assessment {item['id']} has an invalid saved score") from None
                if (not score.is_finite() or not max_score.is_finite() or score < 0
                        or score > points or max_score != points):
                    raise ValueError(f"Assessment {item['id']} saved score is outside its configured points")
            if item.get("attempt_scoring", "highest") == "latest":
                selected = chronological[-1]
            else:
                selected = max(chronological, key=lambda attempt: (
                    Decimal(str(attempt["score"])), _attempt_time(attempt), str(attempt.get("id", ""))
                ))
            earned = Decimal(str(selected["score"]))

        category_values[item["category_id"]].append((earned, points))

    scores: dict[str, Decimal | None] = {}
    for category in categories:
        values = category_values[category["id"]]
        if not values:
            scores[category["id"]] = None
        elif aggregation == "assessment-average":
            scores[category["id"]] = sum(
                (earned / points for earned, points in values), Decimal(0)
            ) / Decimal(len(values))
        else:
            numerator = sum((earned for earned, _ in values), Decimal(0))
            denominator = sum((points for _, points in values), Decimal(0))
            scores[category["id"]] = numerator / denominator

    active = [(Decimal(str(category["weight"])), scores[category["id"]])
              for category in categories
              if scores[category["id"]] is not None and Decimal(str(category["weight"])) > 0]
    active_weight = sum((weight for weight, _ in active), Decimal(0))
    if active_weight == 0:
        overall = None
    else:
        overall = sum((weight * score for weight, score in active), Decimal(0)) / active_weight
        overall = (overall * Decimal(100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return {
        "score_percent": overall,
        "category_scores": {
            category_id: None if value is None else (value * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            for category_id, value in scores.items()
        },
        "active_weight": active_weight,
        "policy_version": "weighted-grade-v1",
    }
