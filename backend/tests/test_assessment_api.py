import json

from fastapi.testclient import TestClient
from sqlalchemy import select

from courselab.db import (
    AssessmentInstance,
    AssessmentPlan,
    GradedSubmission,
    GradedSubmissionAppeal,
    GradedSubmissionAppealReview,
    User,
)


def test_assessment_plan_is_enrollment_scoped_and_never_returns_authoring_keys(app, guest):
    with TestClient(app, headers={"Origin": "http://localhost:8080"}) as unauthenticated:
        assert unauthenticated.get("/api/v1/assessments/test-course").status_code == 401

    denied = guest.get("/api/v1/assessments/test-course")
    assert denied.status_code == 403

    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    response = guest.get("/api/v1/assessments/test-course")
    assert response.status_code == 200
    plan = response.json()
    assert plan["grading_mode"] == "formative-only"
    assert plan["course_grade_status"] == "not_configured"
    assert plan["categories"] == []
    assert plan["assessments"][0]["title"] == "Control-selection practice"
    assert plan["assessments"][0]["schedule_status"] == "practice"
    assert not {"path", "question_ids", "objective_ids", "solution_spec", "answer"}.intersection(
        str(plan)
    )

    with app.state.sessions() as db:
        saved_plan = db.scalar(select(AssessmentPlan))
        saved_item = db.scalar(select(AssessmentInstance))
        assert len(saved_plan.snapshot_sha256) == 64
        assert saved_plan.grading_mode == "formative-only"
        assert saved_item.question_ids == ["choice"]
        assert len(saved_item.source_sha256) == 64

    second = TestClient(app, headers={"Origin": "http://localhost:8080"})
    second.post("/api/v1/auth/guest", json={})
    assert second.get("/api/v1/assessments/test-course").status_code == 403


def test_public_practice_set_is_enrollment_scoped_answer_free_and_version_pinned(guest, content_root):
    route = "/api/v1/assessments/test-course/practice-controls/practice-questions"
    assert guest.get(route).status_code == 403
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201

    response = guest.get(route)
    assert response.status_code == 200
    payload = response.json()
    assert payload["assessment_id"] == "practice-controls"
    assert payload["content_version"] == "0.1.0"
    assert payload["points"] == 2
    assert [question["id"] for question in payload["questions"]] == ["choice"]
    assert payload["questions"][0]["assessment_role"] == "formative"
    for hidden_key in ("solution_spec", "answer", "solution", "PRIVATE_TEST_SENTINEL"):
        assert hidden_key not in response.text

    assert guest.get(
        "/api/v1/assessments/test-course/not-a-practice-set/practice-questions"
    ).status_code == 404

    source = content_root / "courses" / "test-course" / "question-banks" / "practice.json"
    source.write_text(source.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    assert guest.get(route).status_code == 409


def test_practice_mode_homework_assessment_can_serve_only_public_formative_items(guest, content_root):
    manifest_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["assessments"][0]["type"] = "homework"
    manifest["assessments"][0]["title"] = "Homework practice"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    response = guest.get(
        "/api/v1/assessments/test-course/practice-controls/practice-questions"
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["assessment_id"] == "practice-controls"
    assert [question["id"] for question in payload["questions"]] == ["choice"]
    assert "solution_spec" not in response.text


def test_practice_mode_lab_assessment_can_serve_only_public_formative_items(guest, content_root):
    manifest_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["assessments"][0]["type"] = "lab"
    manifest["assessments"][0]["title"] = "Virtual lab practice"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    response = guest.get(
        "/api/v1/assessments/test-course/practice-controls/practice-questions"
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["assessment_id"] == "practice-controls"
    assert [question["id"] for question in payload["questions"]] == ["choice"]
    assert "solution_spec" not in response.text


def test_public_practice_set_refuses_unreleased_questions(guest, content_root):
    source = content_root / "courses" / "test-course" / "question-banks" / "practice.json"
    package = json.loads(source.read_text(encoding="utf-8"))
    package["questions"][0]["visibility"] = "restricted"
    source.write_text(json.dumps(package), encoding="utf-8")

    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    response = guest.get(
        "/api/v1/assessments/test-course/practice-controls/practice-questions"
    )
    assert response.status_code == 409
    assert "only explicit public practice items" in response.json()["detail"]


def test_assessment_plan_pins_categories_and_keeps_prior_version_snapshot(guest, content_root):
    path = content_root / "courses" / "test-course" / "course.json"
    private_bank = path.parent / "question-banks" / "private.json"
    private_bank.write_text('{"course_id":"test-course","questions":[]}', encoding="utf-8")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["grading_policy"] = {
        "mode": "graded-course",
        "categories": [
            {"id": "homework", "title": "Homework", "weight": 0.6},
            {"id": "exam", "title": "Exams", "weight": 0.4},
        ],
        "category_aggregation": "assessment-average",
        "attempt_policy": "Two attempts; highest score counts.",
        "solution_release": "After the deadline.",
        "late_policy": "No late submissions.",
        "appeals": "Request human review.",
    }
    manifest["assessments"] = [
        {
            "id": "homework-1", "type": "homework", "mode": "graded", "title": "Homework 1",
            "path": "question-banks/private.json", "objective_ids": ["objective"],
            "question_ids": ["hidden-q"], "points": 10, "category_id": "homework", "week": 1,
            "release_at": "2099-09-01T00:00:00Z", "due_at": "2099-09-08T23:59:00Z",
            "attempt_limit": 2, "attempt_scoring": "highest",
        },
        {
            "id": "midterm-1", "type": "midterm", "mode": "graded", "title": "Midterm",
            "path": "question-banks/private.json", "objective_ids": ["objective"],
            "question_ids": ["hidden-exam-q"], "points": 20, "category_id": "exam", "week": 7,
            "attempt_limit": 1, "attempt_scoring": "latest",
        },
    ]
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201

    # A same-version manifest edit must not change the policy already pinned to this learner.
    manifest["grading_policy"]["categories"][0]["weight"] = 0.5
    manifest["grading_policy"]["categories"][1]["weight"] = 0.5
    path.write_text(json.dumps(manifest), encoding="utf-8")
    plan = guest.get("/api/v1/assessments/test-course").json()
    assert plan["course_grade_status"] == "configured_no_submissions"
    assert plan["categories"][0]["weight"] == 0.6
    assert plan["assessments"][0]["schedule_status"] == "upcoming"
    assert plan["assessments"][0]["item_count"] == 1
    assert plan["assessments"][0]["attempt_limit"] == 2
    assert "hidden-q" not in json.dumps(plan)
    assert "private.json" not in json.dumps(plan)

    manifest["version"] = "0.2.0"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    upgraded = guest.put("/api/v1/enrollments/test-course/version", json={})
    assert upgraded.status_code == 200
    latest = guest.get("/api/v1/assessments/test-course").json()
    assert latest["content_version"] == "0.2.0"
    assert latest["categories"][0]["weight"] == 0.5
    with guest.app.state.sessions() as db:
        snapshots = list(db.scalars(select(AssessmentPlan).order_by(AssessmentPlan.content_version)))
        assert [item.content_version for item in snapshots] == ["0.1.0", "0.2.0"]


def _configure_graded_homework(
    content_root, *, release_at="2020-01-01T00:00:00Z", due_at=None, private_root=None,
):
    directory = content_root / "courses" / "test-course"
    manifest_path = directory / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    practice = json.loads((directory / "question-banks" / "practice.json").read_text(encoding="utf-8"))
    question = next(item for item in practice["questions"] if item["id"] == "choice")
    if private_root is None:
        source_path = "question-banks/private-homework.json"
        source_file = directory / source_path
    else:
        source_path = "private://assignments/homework-1.json"
        source_file = private_root / "courses" / "test-course" / "assignments" / "homework-1.json"
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text(
        json.dumps({"course_id": "test-course", "questions": [question]}), encoding="utf-8",
    )
    manifest["grading_policy"] = {
        "mode": "graded-course",
        "categories": [{"id": "homework", "title": "Homework", "weight": 1.0}],
        "category_aggregation": "points",
        "attempt_policy": "Two attempts; highest score counts.",
        "solution_release": "Not released in this test fixture.",
        "late_policy": "No late work.",
        "appeals": "Request a manual review.",
    }
    manifest["assessments"] = [{
        "id": "homework-1", "type": "homework", "mode": "graded", "title": "Control analysis",
        "path": source_path, "objective_ids": ["objective"],
        "question_ids": ["choice"], "points": 2, "category_id": "homework", "week": 1,
        "release_at": release_at, "due_at": due_at,
        "attempt_limit": 2, "attempt_scoring": "highest",
    }]
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")


def test_private_assessment_keys_are_read_from_mount_and_never_returned(guest, app, content_root):
    private_root = app.state.settings.private_assessments_root
    _configure_graded_homework(content_root, private_root=private_root)
    key_file = private_root / "courses" / "test-course" / "assignments" / "homework-1.json"
    assert key_file.is_file()
    assert not key_file.is_relative_to(content_root)

    # Without the mounted key, enrollment plan creation fails closed.
    app.state.content.private_assessments_root = None
    unavailable = guest.post("/api/v1/enrollments", json={"course_id": "test-course"})
    assert unavailable.status_code == 409

    app.state.content.private_assessments_root = private_root
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    plan = guest.get("/api/v1/assessments/test-course")
    assert plan.status_code == 200
    assert "private://" not in plan.text and "PRIVATE_TEST_SENTINEL" not in plan.text
    questions = guest.get("/api/v1/assessments/test-course/homework-1/questions")
    assert questions.status_code == 200
    assert questions.json()["questions"][0]["prompt"] == "Select a negative control."
    for response in (
        questions,
        guest.get("/api/v1/courses/test-course"),
        guest.get("/api/v1/lessons/test-course/lesson-one"),
    ):
        assert "solution_spec" not in response.text
        assert "PRIVATE_TEST_SENTINEL" not in response.text
        assert "private://" not in response.text

    submitted = guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 0}}},
    )
    assert submitted.status_code == 201 and submitted.json()["score"] == 2


def test_graded_assignment_accepts_authored_colon_and_dot_question_ids(guest, app, content_root):
    # Regression (found by the protected-assignment browser QA): content ids may contain ":" and ".",
    # but graded submissions accepted only [a-z0-9_-] keys, so an assignment authored with the usual
    # "lesson:slug" question ids could never be submitted.
    private_root = app.state.settings.private_assessments_root
    _configure_graded_homework(content_root, private_root=private_root)
    key_file = private_root / "courses" / "test-course" / "assignments" / "homework-1.json"
    bank = json.loads(key_file.read_text(encoding="utf-8"))
    bank["questions"][0]["id"] = "lesson-one:choice.v2"
    key_file.write_text(json.dumps(bank), encoding="utf-8")
    manifest_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["assessments"][0]["question_ids"] = ["lesson-one:choice.v2"]
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    submitted = guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"lesson-one:choice.v2": {"response": 0}}},
    )
    assert submitted.status_code == 201 and submitted.json()["score"] == 2
    for bad in ("../choice", "Lesson-one:choice", "a b", "a/b", ":choice", "x" * 101):
        refused = guest.post(
            "/api/v1/assessments/test-course/homework-1/submissions",
            json={"responses": {bad: {"response": 0}}},
        )
        assert refused.status_code == 422, bad


def _provision_reviewer(app, client, email="reviewer@example.org"):
    registration = client.post("/api/v1/auth/register", json={
        "email": email, "password": "a-reviewer-test-password",
    })
    assert registration.status_code == 201
    client.headers["X-CSRF-Token"] = registration.json()["csrf_token"]
    user_id = registration.json()["user"]["id"]
    with app.state.sessions() as db:
        reviewer = db.get(User, user_id)
        assert reviewer is not None and reviewer.is_instructor is False
        reviewer.is_instructor = True
        db.commit()
    assert client.get("/api/v1/auth/session").json()["can_review"] is True
    return user_id


def test_graded_assignment_submissions_are_persisted_safe_and_calculated(guest, content_root):
    _configure_graded_homework(content_root)
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201

    other_learner = TestClient(guest.app, headers={"Origin": "http://localhost:8080"})
    other_session = other_learner.post("/api/v1/auth/guest", json={}).json()
    other_learner.headers["X-CSRF-Token"] = other_session["csrf_token"]
    assert other_learner.get("/api/v1/assessments/test-course/submissions").status_code == 403
    assert other_learner.get(
        "/api/v1/assessments/test-course/homework-1/questions"
    ).status_code == 403

    questions = guest.get("/api/v1/assessments/test-course/homework-1/questions")
    assert questions.status_code == 200
    question_payload = questions.json()
    assert question_payload["schedule_status"] == "open"
    assert question_payload["questions"][0]["prompt"] == "Select a negative control."
    for hidden_key in ("solution_spec", "answer", "solution", "PRIVATE_TEST_SENTINEL"):
        assert hidden_key not in json.dumps(question_payload)

    assert guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {}},
    ).status_code == 422
    assert guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"unknown": {"response": 0}}},
    ).status_code == 422

    first = guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 1}}},
    )
    assert first.status_code == 201
    assert first.json()["attempt_number"] == 1
    assert first.json()["score"] == 0
    assert first.json()["results"][0]["feedback"]["diagnosis"] == "incorrect_result"

    second = guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 0}}},
    )
    assert second.status_code == 201
    assert second.json()["attempt_number"] == 2
    assert second.json()["score"] == 2
    assert guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 0}}},
    ).status_code == 409

    history = guest.get("/api/v1/assessments/test-course/submissions")
    assert history.status_code == 200
    assert [item["attempt_number"] for item in history.json()] == [1, 2]
    for hidden_key in ("solution_spec", "answer", "solution", "PRIVATE_TEST_SENTINEL"):
        assert hidden_key not in history.text

    plan = guest.get("/api/v1/assessments/test-course").json()
    assert plan["course_grade_status"] == "configured_with_submissions"
    gradebook = guest.get("/api/v1/gradebook/test-course").json()
    assert gradebook["course_grade"]["score_percent"] == 100
    assert gradebook["course_grade"]["active_weight"] == 1
    assert gradebook["course_grade"]["status"] == "in_progress"

    with guest.app.state.sessions() as db:
        saved = list(db.scalars(select(GradedSubmission).order_by(GradedSubmission.attempt_number)))
        assert len(saved) == 2
        assert all(len(item.source_sha256) == 64 for item in saved)
        assert all(len(item.question_spec_sha256) == 64 for item in saved)
        assert [item.score for item in saved] == [0, 2]

    exported = guest.get("/api/v1/learner/export").json()
    assert len(exported["graded_submissions"]) == 2
    assert guest.delete("/api/v1/learner").status_code == 204
    with guest.app.state.sessions() as db:
        assert db.scalar(select(GradedSubmission)) is None


def test_graded_assignment_release_and_pinned_source_gates(guest, content_root):
    _configure_graded_homework(content_root, release_at="2099-01-01T00:00:00Z")
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    assert guest.get("/api/v1/assessments/test-course/homework-1/questions").status_code == 409
    assert guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 0}}},
    ).status_code == 409


def test_graded_assignment_deadline_closes_submission(guest, content_root):
    _configure_graded_homework(
        content_root,
        release_at="2020-01-01T00:00:00Z",
        due_at="2020-01-02T00:00:00Z",
    )
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    question_response = guest.get("/api/v1/assessments/test-course/homework-1/questions")
    assert question_response.status_code == 200
    assert question_response.json()["schedule_status"] == "closed"
    assert guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 0}}},
    ).status_code == 409


def test_graded_submission_appeal_is_audited_and_changes_only_effective_grade(guest, app, content_root):
    _configure_graded_homework(content_root)
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    submitted = guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 1}}},
    )
    assert submitted.status_code == 201
    automatic = submitted.json()
    assert automatic["score"] == automatic["effective_score"] == 0
    assert automatic["appeal"] is None

    reason = "The selected response is supported by the stated experimental comparison."
    appeal_response = guest.post(
        f"/api/v1/graded-submissions/{automatic['id']}/appeals",
        json={"reason": reason},
    )
    assert appeal_response.status_code == 201
    appeal = appeal_response.json()
    assert appeal["status"] == "open" and appeal["effective_score"] == 0
    assert guest.post(
        f"/api/v1/graded-submissions/{automatic['id']}/appeals",
        json={"reason": reason},
    ).status_code == 409
    own_appeals = guest.get("/api/v1/graded-appeals")
    assert own_appeals.status_code == 200 and own_appeals.json()[0]["reason"] == reason
    own_history = guest.get("/api/v1/assessments/test-course/submissions").json()
    assert own_history[0]["appeal"]["status"] == "open"

    stranger = TestClient(app, headers={"Origin": "http://localhost:8080"})
    stranger_session = stranger.post("/api/v1/auth/guest", json={}).json()
    stranger.headers["X-CSRF-Token"] = stranger_session["csrf_token"]
    assert stranger.get("/api/v1/graded-appeals").json() == []
    assert stranger.post(
        f"/api/v1/graded-submissions/{automatic['id']}/appeals",
        json={"reason": reason},
    ).status_code == 404
    assert stranger.get("/api/v1/instructor/graded-appeals").status_code == 403

    with TestClient(app, headers={"Origin": "http://localhost:8080"}) as reviewer:
        reviewer_id = _provision_reviewer(app, reviewer)
        queue = reviewer.get("/api/v1/instructor/graded-appeals")
        assert queue.status_code == 200 and len(queue.json()) == 1
        record = queue.json()[0]
        assert record["id"] == appeal["id"]
        assert record["learner"] == "Guest account"
        assert record["content_is_current"] is True
        assert record["assessment_title"] == "Control analysis"
        assert record["questions"][0]["prompt"] == "Select a negative control."
        assert record["responses"]["choice"]["response"] == 1
        assert "solution_spec" not in queue.text and "PRIVATE_TEST_SENTINEL" not in queue.text

        invalid = reviewer.post(
            f"/api/v1/instructor/graded-appeals/{appeal['id']}/review",
            json={"decision": "adjusted", "override_score": 2.1,
                  "review_note": "This score exceeds the maximum."},
        )
        assert invalid.status_code == 422
        decision = reviewer.post(
            f"/api/v1/instructor/graded-appeals/{appeal['id']}/review",
            json={"decision": "adjusted", "override_score": 2,
                  "review_note": "The learner identified the supported control comparison."},
        )
        assert decision.status_code == 200
        assert decision.json()["status"] == "adjusted"
        assert reviewer.get("/api/v1/instructor/graded-appeals").json() == []
        assert len(reviewer.get("/api/v1/instructor/graded-appeals?status=reviewed").json()) == 1
        assert reviewer.post(
            f"/api/v1/instructor/graded-appeals/{appeal['id']}/review",
            json={"decision": "adjusted", "override_score": 1,
                  "review_note": "A second decision cannot replace the first."},
        ).status_code == 409
        assert reviewer.delete("/api/v1/learner").status_code == 204

    history = guest.get("/api/v1/assessments/test-course/submissions").json()
    reviewed = history[0]
    assert reviewed["score"] == 0
    assert reviewed["effective_score"] == 2
    assert reviewed["score_percent"] == 0
    assert reviewed["effective_score_percent"] == 100
    assert reviewed["appeal"]["status"] == "adjusted"
    assert reviewed["appeal"]["review_note"] == "The learner identified the supported control comparison."
    gradebook = guest.get("/api/v1/gradebook/test-course").json()["course_grade"]
    assert gradebook["score_percent"] == 100
    assert gradebook["manual_override_count"] == 1
    assert "automatic score" in gradebook["explanation"]
    exported = guest.get("/api/v1/learner/export").json()
    assert exported["graded_submission_appeals"][0]["status"] == "adjusted"

    with app.state.sessions() as db:
        saved = db.get(GradedSubmission, automatic["id"])
        saved_appeal = db.scalar(select(GradedSubmissionAppeal))
        review = db.scalar(select(GradedSubmissionAppealReview))
        assert saved.score == 0 and saved.results_json[0]["score"] == 0
        assert saved_appeal is not None and review is not None
        assert review.reviewer_user_id is None
        assert review.reviewer_email == "deleted instructor account"
        assert db.get(User, reviewer_id) is None


def test_graded_submission_appeal_requires_verified_content_and_blocks_self_review(
    guest, app, content_root,
):
    _configure_graded_homework(content_root)
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    submission = guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 1}}},
    ).json()
    appeal = guest.post(
        f"/api/v1/graded-submissions/{submission['id']}/appeals",
        json={"reason": "Please review the saved answer against its original assessment."},
    ).json()

    bank = content_root / "courses" / "test-course" / "question-banks" / "private-homework.json"
    package = json.loads(bank.read_text(encoding="utf-8"))
    package["questions"][0]["prompt"] = "A same-version edit must not replace the saved prompt."
    bank.write_text(json.dumps(package), encoding="utf-8")
    with TestClient(app, headers={"Origin": "http://localhost:8080"}) as reviewer:
        _provision_reviewer(app, reviewer)
        record = reviewer.get("/api/v1/instructor/graded-appeals").json()[0]
        assert record["content_is_current"] is False
        assert record["questions"] is None and record["responses"] == {}
        for decision, extra in (("adjusted", {"override_score": 0}), ("upheld", {})):
            denied = reviewer.post(
                f"/api/v1/instructor/graded-appeals/{appeal['id']}/review",
                json={"decision": decision, **extra, "review_note": "The saved specification cannot be verified."},
            )
            assert denied.status_code == 409
        declined = reviewer.post(
            f"/api/v1/instructor/graded-appeals/{appeal['id']}/review",
            json={"decision": "declined", "review_note": "The original source version is unavailable."},
        )
        assert declined.status_code == 200


def test_instructor_cannot_review_own_graded_submission(guest, app, content_root):
    _configure_graded_homework(content_root)
    with TestClient(app, headers={"Origin": "http://localhost:8080"}) as reviewer:
        _provision_reviewer(app, reviewer)
        assert reviewer.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
        submission = reviewer.post(
            "/api/v1/assessments/test-course/homework-1/submissions",
            json={"responses": {"choice": {"response": 1}}},
        ).json()
        appeal = reviewer.post(
            f"/api/v1/graded-submissions/{submission['id']}/appeals",
            json={"reason": "This reviewer is also the learner on the submission."},
        ).json()
        assert all(
            item["id"] != appeal["id"]
            for item in reviewer.get("/api/v1/instructor/graded-appeals").json()
        )
        denied = reviewer.post(
            f"/api/v1/instructor/graded-appeals/{appeal['id']}/review",
            json={"decision": "adjusted", "override_score": 1,
                  "review_note": "This self-review must be rejected."},
        )
        assert denied.status_code == 403


def test_graded_assignment_rejects_same_version_source_edits(guest, content_root):
    _configure_graded_homework(content_root)
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    # Enrollment already pinned the earlier source digest; a same-version edit fails closed.
    bank = content_root / "courses" / "test-course" / "question-banks" / "private-homework.json"
    bank.write_text(bank.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    assert guest.get("/api/v1/assessments/test-course/homework-1/questions").status_code == 409
    assert guest.post(
        "/api/v1/assessments/test-course/homework-1/submissions",
        json={"responses": {"choice": {"response": 0}}},
    ).status_code == 409
