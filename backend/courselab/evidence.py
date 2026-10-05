"""Transparent, conservative objective-level practice evidence aggregation."""

from collections import defaultdict

POLICY_VERSION = "practice-evidence-v1"
MIN_DISTINCT_ITEMS = 3
MIN_ITEM_COVERAGE = 0.8
MIN_PERFORMANCE = 0.8


def objective_evidence(questions: list[dict], attempts: list) -> dict[str, dict]:
    """Aggregate best points per distinct item without counting retries as breadth."""
    items_by_objective: dict[str, dict[str, float]] = defaultdict(dict)
    for question in questions:
        question_id = question["id"]
        points = float(question.get("points", 1))
        for objective_id in set(question.get("objective_ids", [])):
            items_by_objective[objective_id][question_id] = points

    attempts_by_objective: dict[str, list] = defaultdict(list)
    for attempt in attempts:
        for objective_id in set(attempt.objective_ids or []):
            if attempt.question_id in items_by_objective.get(objective_id, {}):
                attempts_by_objective[objective_id].append(attempt)

    result = {}
    for objective_id, authored_items in items_by_objective.items():
        rows = attempts_by_objective.get(objective_id, [])
        best_by_question = {}
        correct_results = 0
        for attempt in rows:
            correct_results += int(bool(attempt.result.get("correct")))
            question_id = attempt.question_id
            current = best_by_question.get(question_id)
            if current is None or attempt.score > current[0]:
                best_by_question[question_id] = (float(attempt.score), float(attempt.max_score))

        attempted_items = len(best_by_question)
        best_score = sum(score for score, _ in best_by_question.values())
        possible_attempted = sum(max_score for _, max_score in best_by_question.values())
        performance = best_score / possible_attempted if possible_attempted else None
        coverage = attempted_items / len(authored_items) if authored_items else 0.0

        if attempted_items == 0:
            status = "no_evidence"
        elif attempted_items < MIN_DISTINCT_ITEMS or coverage < MIN_ITEM_COVERAGE:
            status = "insufficient_evidence"
        elif performance is not None and performance >= MIN_PERFORMANCE:
            status = "provisional_practice_mastery"
        else:
            status = "needs_practice"

        result[objective_id] = {
            "attempts": len(rows),
            "correct_results": correct_results,
            "attempted_items": attempted_items,
            "item_count": len(authored_items),
            "best_score": round(best_score, 4),
            "best_possible_score": round(possible_attempted, 4),
            "performance": round(performance, 4) if performance is not None else None,
            "status": status,
        }
    return result
