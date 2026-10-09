"""The assessment-protection toggle: protected (private store required) versus open."""

import json
from copy import deepcopy

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import func, select

from courselab.assessment import effective_protection, validate_assessment_configuration
from courselab.config import Settings
from courselab.db import Base, GradedSubmission
from courselab.main import create_app
from tests.test_assessment_api import _configure_graded_homework

ORIGIN = "http://localhost:8080"
POLICY = {"mode": "graded-course", "categories": [{"id": "homework", "weight": 1}]}
PUBLIC = [{"id": "h", "mode": "graded", "path": "question-banks/h.json", "points": 1, "category_id": "homework",
           "type": "homework", "week": 1, "objective_ids": [], "question_ids": ["q"]}]


@pytest.mark.parametrize("private", [False, True])
@pytest.mark.parametrize("configuration", [{}, None, {
    "seeded": True, "generator_id": "authored-variants-v1",
    "variants": [{"id": "alternate", "prompt": "An alternate assigned case with a different correct response.",
                  "solution_spec": {"answer": 1}}],
}])
def test_graded_variants_fail_closed_before_delivery_or_submission(tmp_path, content_root, private, configuration):
    private_root = tmp_path / "private-assessments" if private else None
    _configure_graded_homework(content_root, private_root=private_root)
    if private:
        source = private_root / "courses/test-course/assignments/homework-1.json"
    else:
        source = content_root / "courses/test-course/question-banks/private-homework.json"
    bank = json.loads(source.read_text())
    bank["questions"][0]["randomization"] = configuration
    source.write_text(json.dumps(bank))
    application = make_app(tmp_path, content_root, "protected" if private else "open")
    with guest_client(application) as client:
        assert client.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
        route = "/api/v1/assessments/test-course/homework-1"
        served = client.get(route + "/questions")
        assert served.status_code == 409
        assert "variants are not supported" in served.json()["detail"]
        submitted = client.post(route + "/submissions", json={"responses": {"choice": {"response": 0}}})
        assert submitted.status_code == 409
        with application.state.sessions() as db:
            assert db.scalar(select(func.count()).select_from(GradedSubmission)) == 0
    application.state.engine.dispose()


def test_effective_protection_resolution():
    assert effective_protection({}) == "open"
    assert effective_protection({"assessment_protection": "protected"}) == "protected"
    assert effective_protection({"assessment_protection": "protected"}, "open") == "open"
    assert effective_protection({"assessment_protection": "open"}, "protected") == "protected"
    assert effective_protection({"assessment_protection": "open"}, "course") == "open"
    for bad in ("secret", "", None):
        with pytest.raises(ValueError):
            effective_protection({"assessment_protection": bad})
    with pytest.raises(ValueError):
        effective_protection({}, "closed")


def test_protected_mode_rejects_a_public_graded_source_and_open_mode_allows_it():
    protected = {**POLICY, "assessment_protection": "protected"}
    with pytest.raises(ValueError, match="public source"):
        validate_assessment_configuration(deepcopy(PUBLIC), protected)
    validate_assessment_configuration(deepcopy(PUBLIC), {**POLICY, "assessment_protection": "open"})
    validate_assessment_configuration(deepcopy(PUBLIC), POLICY)
    # An operator can force either direction.
    with pytest.raises(ValueError, match="public source"):
        validate_assessment_configuration(deepcopy(PUBLIC), POLICY, "protected")
    validate_assessment_configuration(deepcopy(PUBLIC), protected, "open")
    private = deepcopy(PUBLIC)
    private[0]["path"] = "private://assignments/h.json"
    validate_assessment_configuration(private, protected)


def make_app(tmp_path, content_root, mode):
    application = create_app(Settings(
        database_url=f"sqlite:///{tmp_path}/protection.db", content_root=content_root,
        private_assessments_root=tmp_path / "private-assessments", cookie_secure=False,
        rate_limit=1000, auth_rate_limit=1000, assessment_protection=mode))
    Base.metadata.create_all(application.state.engine)
    return application


def guest_client(application):
    client = TestClient(application, headers={"Origin": ORIGIN})
    response = client.post("/api/v1/auth/guest", json={})
    assert response.status_code == 200
    client.headers["X-CSRF-Token"] = response.json()["csrf_token"]
    return client


def set_course_protection(content_root, value):
    path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if value is None:
        manifest["grading_policy"].pop("assessment_protection", None)
    else:
        manifest["grading_policy"]["assessment_protection"] = value
    path.write_text(json.dumps(manifest), encoding="utf-8")


def test_open_course_with_public_graded_source_works_and_reports_open(tmp_path, content_root):
    _configure_graded_homework(content_root)
    application = make_app(tmp_path, content_root, "course")
    with guest_client(application) as client:
        assert client.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
        plan = client.get("/api/v1/assessments/test-course").json()
        assert plan["assessment_protection"] == "open"
        assert client.get("/api/v1/assessments/test-course/homework-1/questions").status_code == 200
    application.state.engine.dispose()


def test_course_can_declare_protected_and_then_needs_the_private_store(tmp_path, content_root):
    _configure_graded_homework(content_root)
    set_course_protection(content_root, "protected")
    application = make_app(tmp_path, content_root, "course")
    with guest_client(application) as client:
        refused = client.post("/api/v1/enrollments", json={"course_id": "test-course"})
        assert refused.status_code == 409
    application.state.engine.dispose()

    _configure_graded_homework(content_root, private_root=tmp_path / "private-assessments")
    set_course_protection(content_root, "protected")
    application = make_app(tmp_path, content_root, "course")
    with guest_client(application) as client:
        assert client.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
        assert client.get("/api/v1/assessments/test-course").json()["assessment_protection"] == "protected"
        submitted = client.post("/api/v1/assessments/test-course/homework-1/submissions",
                                json={"responses": {"choice": {"response": 0}}})
        assert submitted.status_code == 201
    application.state.engine.dispose()


def test_protected_course_gradebook_counts_private_graded_work(tmp_path, content_root):
    # Regression (found by the protected-assignment browser QA): the grade calculation re-checked
    # protection without the pinned source paths, so every protected graded course answered 409 on
    # its gradebook, which also hid the assessment plan and the assignment in the learner view.
    _configure_graded_homework(content_root, private_root=tmp_path / "private-assessments")
    set_course_protection(content_root, "protected")
    application = make_app(tmp_path, content_root, "course")
    with guest_client(application) as client:
        assert client.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
        before = client.get("/api/v1/gradebook/test-course")
        assert before.status_code == 200
        assert before.json()["course_grade"]["status"] == "configured_no_submissions"
        submitted = client.post("/api/v1/assessments/test-course/homework-1/submissions",
                                json={"responses": {"choice": {"response": 0}}})
        assert submitted.status_code == 201
        after = client.get("/api/v1/gradebook/test-course")
        assert after.status_code == 200
        assert after.json()["course_grade"]["score_percent"] == 100
        assert "private://" not in after.text and "solution_spec" not in after.text
    application.state.engine.dispose()


def test_operator_override_forces_protection_for_a_course_that_chose_open(tmp_path, content_root):
    _configure_graded_homework(content_root)
    set_course_protection(content_root, "open")
    application = make_app(tmp_path, content_root, "protected")
    with guest_client(application) as client:
        assert client.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 409
    application.state.engine.dispose()


def test_switching_a_live_deployment_to_protected_closes_public_graded_assessments(tmp_path, content_root):
    _configure_graded_homework(content_root)
    first = make_app(tmp_path, content_root, "course")
    with guest_client(first) as client:
        assert client.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
        cookies, csrf = dict(client.cookies), client.headers["X-CSRF-Token"]
        assert client.get("/api/v1/assessments/test-course/homework-1/questions").status_code == 200
    first.state.engine.dispose()

    second = make_app(tmp_path, content_root, "protected")
    with TestClient(second, headers={"Origin": ORIGIN, "X-CSRF-Token": csrf}, cookies=cookies) as client:
        closed = client.get("/api/v1/assessments/test-course/homework-1/questions")
        assert closed.status_code == 409
        assert "private store" in closed.json()["detail"]
        submit = client.post("/api/v1/assessments/test-course/homework-1/submissions",
                             json={"responses": {"choice": {"response": 0}}})
        assert submit.status_code == 409
        assert client.get("/api/v1/assessments/test-course").json()["assessment_protection"] == "protected"
    second.state.engine.dispose()


def test_environment_setting_is_validated(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./x.db")
    monkeypatch.setenv("ASSESSMENT_PROTECTION", "Protected")
    assert Settings.from_environment().assessment_protection == "protected"
    monkeypatch.setenv("ASSESSMENT_PROTECTION", "maybe")
    with pytest.raises(ValueError):
        Settings.from_environment()
    monkeypatch.delenv("ASSESSMENT_PROTECTION")
    assert Settings.from_environment().assessment_protection == "course"
