import json

from fastapi.testclient import TestClient
from sqlalchemy import select

from courselab.db import AssessmentInstance, AssessmentPlan, GradedSubmission


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
    content_root, *, release_at="2020-01-01T00:00:00Z", due_at=None,
):
    directory = content_root / "courses" / "test-course"
    manifest_path = directory / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    practice = json.loads((directory / "question-banks" / "practice.json").read_text(encoding="utf-8"))
    question = next(item for item in practice["questions"] if item["id"] == "choice")
    (directory / "question-banks" / "private-homework.json").write_text(
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
        "path": "question-banks/private-homework.json", "objective_ids": ["objective"],
        "question_ids": ["choice"], "points": 2, "category_id": "homework", "week": 1,
        "release_at": release_at, "due_at": due_at,
        "attempt_limit": 2, "attempt_scoring": "highest",
    }]
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")


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
