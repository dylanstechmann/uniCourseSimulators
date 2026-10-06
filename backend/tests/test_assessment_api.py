import json

from fastapi.testclient import TestClient
from sqlalchemy import select

from courselab.db import AssessmentInstance, AssessmentPlan


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
