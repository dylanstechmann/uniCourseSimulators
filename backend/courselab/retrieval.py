"""Deterministic spaced-retrieval scheduling for self-assessed retrieval cards.

Policy ``retrieval-schedule-v1`` is an SM-2-style interval rule with four
learner self-ratings. A rating is the learner's own judgement after revealing
an answer. The resulting schedule is a study aid: it is not assessment
evidence, a practice score, or a mastery signal.
"""

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timedelta

POLICY_VERSION = "retrieval-schedule-v1"
RATINGS = ("again", "hard", "good", "easy")
INITIAL_EASE = 2.5
MIN_EASE = 1.3
MAX_EASE = 3.0
MAX_INTERVAL_DAYS = 365.0
RELEARN_DELAY = timedelta(minutes=10)
POLICY_SUMMARY = (
    "Self-rated retrieval schedule (retrieval-schedule-v1). 'Again' returns a card in "
    "10 minutes and restarts its sequence; 'hard' grows the previous interval by 1.2x; "
    "'good' uses 1 day, then 6 days, then the previous interval times the card's ease; "
    "'easy' adds 30% to the good interval and raises ease. Intervals are capped at 365 days. "
    "Ratings are self-assessments: they schedule study and are not practice scores or mastery evidence."
)


@dataclass(frozen=True)
class ScheduleState:
    repetitions: int
    ease: float
    interval_days: float
    due_at: datetime


def card_digest(course_id: str, card: dict) -> str:
    """Hash the learner-visible card text so a schedule never carries over edited content."""
    canonical = json.dumps(
        {
            "course_id": course_id,
            "card_id": card["id"],
            "lesson_id": card.get("lesson_id"),
            "front": card["front"],
            "back": card["back"],
        },
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def next_state(previous: ScheduleState | None, rating: str, reviewed_at: datetime) -> ScheduleState:
    """Return the schedule after one self-rating; ``previous`` is None for a new card."""
    if rating not in RATINGS:
        raise ValueError(f"Unsupported retrieval rating: {rating!r}")
    repetitions = previous.repetitions if previous else 0
    ease = previous.ease if previous else INITIAL_EASE
    interval = previous.interval_days if previous else 0.0

    if rating == "again":
        ease = max(MIN_EASE, ease - 0.20)
        return ScheduleState(0, round(ease, 2), 0.0, reviewed_at + RELEARN_DELAY)

    if repetitions == 0:
        good_interval = 1.0
    elif repetitions == 1:
        good_interval = 6.0
    else:
        good_interval = max(interval + 1.0, interval * ease)

    if rating == "hard":
        ease = max(MIN_EASE, ease - 0.15)
        new_interval = 1.0 if repetitions == 0 else max(1.0, interval * 1.2)
    elif rating == "good":
        new_interval = good_interval
    else:
        ease = min(MAX_EASE, ease + 0.15)
        new_interval = 4.0 if repetitions == 0 else good_interval * 1.3

    new_interval = round(min(MAX_INTERVAL_DAYS, new_interval), 2)
    return ScheduleState(
        repetitions + 1,
        round(ease, 2),
        new_interval,
        reviewed_at + timedelta(days=new_interval),
    )
