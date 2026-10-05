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
    root.mkdir(parents=True)
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
        "lesson_objectives": [
            {"id": "objective", "description": "Compare controls", "bloom": "analyze"},
            {"id": "symbolic-objective", "description": "Differentiate a rational function", "bloom": "apply"},
            {"id": "data-objective", "description": "Interpret a descriptive data summary", "bloom": "analyze"},
        ],
        "modules": [{"id": "module", "title": "Controls", "source_ids": ["fixture"], "lessons": [{
            "id": "lesson-one", "title": "Experiment", "reading": "modules/one.md", "objectives": ["objective"],
            "question_ids": ["choice", "numeric", "multi", "symbolic", "data"],
            "card_ids": ["control-card"], "worked_example": "Match the delivery procedure between groups."
        }]}], "syllabus": "syllabus.md", "license": "CC-BY-4.0", "review": {"status": "unreviewed"},
        "retrieval_cards": "question-banks/retrieval-cards.json",
    }
    (directory / "course.json").write_text(json.dumps(manifest))
    (root / "curriculum-map.json").write_text(json.dumps({
        "schema_version": "1.0",
        "description": "A synthetic fixture map used to test learner-facing prerequisite and pathway data.",
        "catalog_only": [{
            "id": "fixture-extension", "title": "Fixture Extension", "domain": "Life sciences",
            "level": "Year 2", "maturity": "catalog-only",
            "description": "A test-only catalog topic used to verify that planned study areas are not exposed as authored courses.",
            "prerequisites": {"course_ids": ["test-course"], "recommended_course_ids": [],
                              "concurrent_course_ids": [], "knowledge": [],
                              "statement": "Complete the synthetic fixture course before exploring this planning node."},
            "related_package_ids": ["test-course"],
            "relation_note": "The synthetic partial package only demonstrates the learner-facing link contract.",
        }],
        "pathways": [{
            "id": "fixture-pathway", "title": "Fixture pathway",
            "description": "A synthetic learning sequence used only by API tests.",
            "course_ids": ["test-course", "fixture-extension"], "source_ids": [],
            "sequence_note": "A fixture sequence that makes no university-equivalency claim.",
        }],
        "alignment_maps": [],
    }))
    (directory / "question-banks" / "retrieval-cards.json").write_text(json.dumps({
        "course_id": "test-course", "cards": [{
            "id": "control-card", "lesson_id": "lesson-one",
            "front": "What does a vehicle control match?",
            "back": "It controls for effects of the delivery vehicle.",
            "objective_ids": ["objective"], "license": "CC-BY-4.0",
        }],
    }))
    questions = {"course_id": "test-course", "questions": [
        {"id": "choice", "type": "single_choice", "prompt": "Select a negative control.",
         "visibility": "public-practice-authoring",
         "options": ["Vehicle", "Active drug"], "points": 2, "objective_ids": ["objective"],
         "solution_spec": {"answer": 0}, "feedback": {"hint": "Match all other conditions.",
         "solution": "PRIVATE_TEST_SENTINEL", "lesson_ids": ["lesson-one"]}},
        {"id": "numeric", "type": "numeric", "prompt": "Report the calculated rate.", "points": 1,
         "visibility": "public-practice-authoring",
         "objective_ids": ["objective"], "solution_spec": {"answer": 80, "unit": "μmol/min",
         "tolerance": 1.2, "relative_tolerance": 0.01, "significant_figures": 2, "unit_required": True}, "feedback": {"hint": "Keep the rate units.",
         "solution": "PRIVATE_TEST_SENTINEL", "lesson_ids": ["lesson-one"]}},
        {"id": "multi", "type": "multiple_select", "prompt": "Which controls separate these explanations? Select all that apply.",
         "visibility": "public-practice-authoring", "options": ["Vehicle", "No-target", "Positive standard", "Untreated only"],
         "points": 3, "objective_ids": ["objective"],
         "solution_spec": {"answer": [0, 1, 2], "partial_credit": "correct-minus-incorrect-clamped-v1"},
         "feedback": {"hint": "Consider vehicle effects and assay performance.", "solution": "Vehicle, no-target and positive-standard controls test distinct failure modes.", "lesson_ids": ["lesson-one"]}},
        {"id": "symbolic", "type": "symbolic", "prompt": "Enter the derivative as a simplified rational expression.",
         "visibility": "public-practice-authoring", "points": 1, "objective_ids": ["symbolic-objective"],
         "solution_spec": {"expression": "(x^2 + 2*x - 1)/(x + 1)^2", "variables": ["x"],
                            "assumptions": {"x": {"real": True}}},
         "feedback": {"hint": "Use the quotient rule.", "solution": "Simplify the quotient-rule numerator.",
                      "lesson_ids": ["lesson-one"]}},
        {"id": "data", "type": "data_interpretation", "prompt": "Compare the two group summaries and select the strongest conclusion supported by the data.",
         "visibility": "public-practice-authoring", "points": 2, "objective_ids": ["data-objective"],
         "response_fields": [
             {"id": "difference", "type": "numeric", "prompt": "Calculate the treatment minus vehicle sample mean.", "unit": "μM", "points": 1},
             {"id": "interpretation", "type": "single_choice", "prompt": "Choose the strongest supported conclusion.",
              "options": ["The sample means differ by 4.0 μM; the summary alone does not establish causation or uncertainty.", "The treatment caused every replicate to increase."], "points": 1}],
         "solution_spec": {"field_specs": [
             {"id": "difference", "type": "numeric", "answer": 4.0, "unit": "μM", "tolerance": 0, "unit_required": True, "significant_figures": 2, "dimensions": {"length": -3, "amount": 1}},
             {"id": "interpretation", "type": "single_choice", "answer": 0}]},
         "feedback": {"hint": "Calculate the contrast and distinguish it from an inference.", "solution": "A descriptive contrast does not establish causation.", "lesson_ids": ["lesson-one"]}},
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
