import json
from datetime import datetime, timedelta

import pytest

from courselab import main as main_module
from courselab.retrieval import (
    MAX_INTERVAL_DAYS,
    MIN_EASE,
    RATINGS,
    ScheduleState,
    card_digest,
    next_state,
)

START = datetime(2026, 10, 7, 12, 0, 0)
CARD = {"id": "control-card", "lesson_id": "lesson-one", "front": "Front", "back": "Back"}


def test_good_sequence_follows_published_intervals():
    first = next_state(None, "good", START)
    second = next_state(first, "good", first.due_at)
    third = next_state(second, "good", second.due_at)
    assert [first.interval_days, second.interval_days, third.interval_days] == [1.0, 6.0, 15.0]
    assert [first.repetitions, second.repetitions, third.repetitions] == [1, 2, 3]
    assert first.due_at == START + timedelta(days=1)
    assert third.ease == 2.5


def test_again_restarts_sequence_and_returns_card_after_relearn_delay():
    learned = next_state(next_state(None, "good", START), "good", START)
    lapsed = next_state(learned, "again", START)
    assert lapsed.repetitions == 0
    assert lapsed.interval_days == 0.0
    assert lapsed.due_at == START + timedelta(minutes=10)
    assert lapsed.ease == pytest.approx(learned.ease - 0.2)
    relearned = next_state(lapsed, "good", lapsed.due_at)
    assert relearned.interval_days == 1.0


@pytest.mark.parametrize("prior", [
    None,
    ScheduleState(1, 2.5, 1.0, START),
    ScheduleState(2, 2.5, 6.0, START),
    ScheduleState(5, 1.3, 40.0, START),
    ScheduleState(3, 3.0, 20.0, START),
])
def test_ratings_order_intervals_from_any_state(prior):
    intervals = {rating: next_state(prior, rating, START).interval_days for rating in RATINGS}
    assert intervals["again"] < intervals["hard"] <= intervals["good"] < intervals["easy"]


def test_ease_is_bounded_and_interval_is_capped():
    state = None
    for _ in range(12):
        state = next_state(state, "again", START)
    assert state.ease == MIN_EASE
    long_state = ScheduleState(9, 3.0, 300.0, START)
    capped = next_state(long_state, "easy", START)
    assert capped.interval_days == MAX_INTERVAL_DAYS
    assert capped.ease == 3.0


def test_unknown_rating_is_rejected():
    with pytest.raises(ValueError):
        next_state(None, "perfect", START)


def test_card_digest_tracks_visible_text_and_identity():
    base = card_digest("test-course", CARD)
    assert base == card_digest("test-course", dict(CARD))
    assert base != card_digest("test-course", {**CARD, "back": "Edited back"})
    assert base != card_digest("other-course", CARD)


def review(client, rating, card_id="control-card"):
    return client.post(f"/api/v1/courses/test-course/cards/{card_id}/reviews", json={"rating": rating})


def test_review_requires_session_enrollment_and_csrf(client, guest):
    assert client.get("/api/v1/reviews/test-course").status_code in {401, 403}
    assert review(guest, "good").status_code == 403
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    token = guest.headers.pop("X-CSRF-Token")
    assert review(guest, "good").status_code == 403
    guest.headers["X-CSRF-Token"] = token
    assert review(guest, "good").status_code == 201


def test_review_validates_rating_and_card(enrolled):
    assert review(enrolled, "perfect").status_code == 422
    assert review(enrolled, "good", card_id="missing-card").status_code == 404


def test_new_card_is_scheduled_and_queue_reports_it(enrolled, monkeypatch):
    queue = enrolled.get("/api/v1/reviews/test-course").json()
    assert queue["counts"] == {"due": 0, "new": 1, "upcoming": 0}
    assert queue["new"][0]["card_id"] == "control-card"
    assert queue["new"][0]["lesson_title"] == "Experiment"
    assert queue["new"][0]["schedule"] is None
    assert "not a practice score" in queue["limitations"]

    saved = review(enrolled, "good")
    assert saved.status_code == 201
    schedule = saved.json()["schedule"]
    assert schedule["interval_days"] == 1.0
    assert schedule["review_count"] == 1
    assert schedule["due"] is False

    queue = enrolled.get("/api/v1/reviews/test-course").json()
    assert queue["counts"] == {"due": 0, "new": 0, "upcoming": 1}

    later = main_module.now() + timedelta(days=2)
    monkeypatch.setattr(main_module, "now", lambda: later)
    queue = enrolled.get("/api/v1/reviews/test-course").json()
    assert queue["counts"] == {"due": 1, "new": 0, "upcoming": 0}
    assert queue["due"][0]["schedule"]["due"] is True

    second = review(enrolled, "good").json()["schedule"]
    assert second["interval_days"] == 6.0
    assert second["review_count"] == 2


def test_reviews_do_not_change_practice_gradebook(enrolled):
    before = enrolled.get("/api/v1/gradebook/test-course").json()
    assert review(enrolled, "easy").status_code == 201
    after = enrolled.get("/api/v1/gradebook/test-course").json()
    assert after == before


def test_edited_card_starts_a_new_schedule(enrolled, content_root):
    assert review(enrolled, "good").status_code == 201
    assert review(enrolled, "good").status_code == 201
    cards_path = content_root / "courses" / "test-course" / "question-banks" / "retrieval-cards.json"
    package = json.loads(cards_path.read_text())
    package["cards"][0]["back"] = "Vehicle controls match the delivery solution without the active agent."
    cards_path.write_text(json.dumps(package))

    queue = enrolled.get("/api/v1/reviews/test-course").json()
    assert queue["counts"]["new"] == 1
    assert queue["new"][0]["content_changed_since_last_review"] is True
    restarted = review(enrolled, "good").json()["schedule"]
    assert restarted["review_count"] == 1
    assert restarted["interval_days"] == 1.0


def test_card_reviews_are_exported_and_deleted_with_learner(enrolled):
    assert review(enrolled, "hard").status_code == 201
    exported = enrolled.get("/api/v1/learner/export").json()
    assert len(exported["card_reviews"]) == 1
    record = exported["card_reviews"][0]
    assert record["rating"] == "hard"
    assert record["policy_version"] == "retrieval-schedule-v1"
    assert len(record["card_sha256"]) == 64
    assert enrolled.delete("/api/v1/learner").status_code == 204


def test_gradebook_lists_authored_objectives_without_tagged_items(enrolled, content_root):
    course_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(course_path.read_text())
    manifest["lesson_objectives"].append(
        {"id": "untagged-objective", "description": "Explain a not-yet-practiced idea", "bloom": "understand"}
    )
    course_path.write_text(json.dumps(manifest))
    response = enrolled.get("/api/v1/gradebook/test-course")
    assert response.status_code == 200
    evidence = response.json()["objective_evidence"]
    assert evidence["untagged-objective"]["status"] == "no_items"
    assert evidence["untagged-objective"]["item_count"] == 0
    assert evidence["objective"]["status"] == "no_evidence"
