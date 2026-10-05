import json

import pytest
from fastapi.testclient import TestClient

from courselab.config import Settings
from courselab.db import Base
from courselab.main import create_app

ORIGIN = "http://localhost:8080"


@pytest.fixture
def content_root(tmp_path):
    root = tmp_path / "content"
    directory = root / "courses" / "test-course"
    (directory / "modules").mkdir(parents=True)
    (directory / "question-banks").mkdir()
    (directory / "modules" / "one.md").write_text("# Experiment\n\nCompare a perturbation with a negative control.")
    (directory / "syllabus.md").write_text("# Partial test package\n\nThis is a server fixture, not a course.")
    manifest = {
        "id": "test-course", "title": "Fixture", "description": "Fixture course", "domain": "Life sciences",
        "level": "Year 1", "maturity": "partial", "version": "0.1.0", "limitations": ["Fixture only"],
        "prerequisites": {"course_ids": [], "statement": "Foundational biology"},
        "outcomes": [{"id": "outcome", "description": "Compare controls", "bloom": "analyze"}],
        "lesson_objectives": [{"id": "objective", "description": "Compare controls", "bloom": "analyze"}],
        "modules": [{"id": "module", "title": "Controls", "source_ids": ["fixture"], "lessons": [{
            "id": "lesson-one", "title": "Experiment", "reading": "modules/one.md", "objectives": ["objective"],
            "question_ids": ["choice", "numeric", "multi"], "worked_example": "Match the delivery procedure between groups."
        }]}], "syllabus": "syllabus.md", "license": "CC-BY-4.0", "review": {"status": "unreviewed"},
    }
    (directory / "course.json").write_text(json.dumps(manifest))
    questions = {"course_id": "test-course", "questions": [
        {"id": "choice", "type": "single_choice", "prompt": "Select a negative control.",
         "visibility": "public-practice-authoring",
         "options": ["Vehicle", "Active drug"], "points": 2, "objective_ids": ["objective"],
         "solution_spec": {"answer": 0}, "feedback": {"hint": "Match all other conditions.",
         "solution": "PRIVATE_TEST_SENTINEL", "lesson_ids": ["lesson-one"]}},
        {"id": "numeric", "type": "numeric", "prompt": "Report the calculated rate.", "points": 1,
         "visibility": "public-practice-authoring",
         "objective_ids": ["objective"], "solution_spec": {"answer": 80, "unit": "μmol/min",
         "tolerance": 1.2, "unit_required": True}, "feedback": {"hint": "Keep the rate units.",
         "solution": "PRIVATE_TEST_SENTINEL", "lesson_ids": ["lesson-one"]}},
        {"id": "multi", "type": "multiple_select", "prompt": "Which controls separate these explanations? Select all that apply.",
         "visibility": "public-practice-authoring", "options": ["Vehicle", "No-target", "Positive standard", "Untreated only"],
         "points": 3, "objective_ids": ["objective"],
         "solution_spec": {"answer": [0, 1, 2], "partial_credit": "correct-minus-incorrect-clamped-v1"},
         "feedback": {"hint": "Consider vehicle effects and assay performance.", "solution": "Vehicle, no-target and positive-standard controls test distinct failure modes.", "lesson_ids": ["lesson-one"]}},
    ]}
    (directory / "question-banks" / "practice.json").write_text(json.dumps(questions))
    return root


@pytest.fixture
def app(tmp_path, content_root):
    application = create_app(Settings(database_url=f"sqlite:///{tmp_path}/test.db", content_root=content_root,
                                      cookie_secure=False, rate_limit=1000, auth_rate_limit=1000))
    Base.metadata.create_all(application.state.engine)
    yield application
    application.state.engine.dispose()


@pytest.fixture
def client(app):
    with TestClient(app, headers={"Origin": ORIGIN}) as test_client:
        yield test_client


@pytest.fixture
def guest(client):
    response = client.post("/api/v1/auth/guest", json={})
    assert response.status_code == 200
    client.headers["X-CSRF-Token"] = response.json()["csrf_token"]
    return client


@pytest.fixture
def enrolled(guest):
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    return guest
