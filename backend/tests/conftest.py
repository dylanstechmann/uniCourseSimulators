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
            {"id": "structured-objective", "description": "Construct an evidence-bounded experimental inference", "bloom": "analyze"},
        ],
        "modules": [{"id": "module", "title": "Controls", "source_ids": ["fixture"], "lessons": [{
            "id": "lesson-one", "title": "Experiment", "reading": "modules/one.md", "objectives": ["objective", "structured-objective"],
            "question_ids": ["choice", "numeric", "multi", "symbolic", "data", "structured", "graph"],
            "card_ids": ["control-card"], "worked_example": "Match the delivery procedure between groups."
        }]}], "syllabus": "syllabus.md", "license": "CC-BY-4.0", "review": {"status": "unreviewed"},
        "retrieval_cards": "question-banks/retrieval-cards.json",
        "assessments": [{
            "id": "practice-controls", "type": "practice", "mode": "practice",
            "title": "Control-selection practice", "path": "question-banks/practice.json",
            "objective_ids": ["objective"], "question_ids": ["choice"], "points": 2,
        }],
        "grading_policy": {
            "mode": "formative-only", "categories": [], "category_aggregation": "points",
            "attempt_policy": "Unlimited practice retries; no graded assignments.",
            "solution_release": "Practice solutions may be shown after submission.",
            "late_policy": "No deadline or late penalty is configured.",
            "appeals": "Request human review of a saved practice attempt.",
        },
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
        {"id": "structured", "type": "structured", "prompt": "Build an experiment-and-inference chain for the candidate regulator using the explicit rubric criteria.",
         "visibility": "public-practice-authoring", "points": 3, "objective_ids": ["structured-objective"],
         "response_fields": [
             {"id": "control", "type": "single_choice", "prompt": "Select the matched delivery control.",
              "options": ["A non-targeting oligonucleotide with the same delivery reagent and timing.", "Untreated cells with no delivery reagent."], "points": 1},
             {"id": "binding", "type": "single_choice", "prompt": "Select direct evidence of regulator occupancy at the target promoter.",
              "options": ["Validated promoter enrichment by ChIP-qPCR over its assay control.", "A lower bulk target-RNA measurement after depletion."], "points": 1},
             {"id": "claim", "type": "single_choice", "prompt": "Select the conclusion bounded to the tested system.",
              "options": ["The evidence supports a contribution in this tested system, not a universal effect.", "The regulator is necessary in every cell type and condition."], "points": 1}],
         "solution_spec": {
             "field_specs": [
                 {"id": "control", "type": "single_choice", "answer": 0},
                 {"id": "binding", "type": "single_choice", "answer": 0},
                 {"id": "claim", "type": "single_choice", "answer": 0}],
             "rubric": [
                 {"id": "control", "criterion": "Control fidelity", "points": 1, "evidence": ["Delivery reagent and timing are matched with a non-targeting oligonucleotide."]},
                 {"id": "binding", "criterion": "Direct promoter occupancy", "points": 1, "evidence": ["Target-locus enrichment is compared with the assay control."]},
                 {"id": "claim", "criterion": "Evidence-bounded causal claim", "points": 1, "evidence": ["The conclusion is limited to the tested system and conditions."]}]},
         "feedback": {"hint": "Separate reagent controls, promoter occupancy, and the scope of an inference.", "solution": "A matched non-targeting control addresses delivery effects; controlled locus enrichment tests occupancy; the causal claim must stay within the tested system.", "lesson_ids": ["lesson-one"]}},
        {"id": "graph", "type": "graph", "prompt": "Calculate group means and plot their coordinates on the supplied axes.",
         "visibility": "public-practice-authoring", "points": 2, "objective_ids": ["data-objective"],
         "graph_spec": {
             "x_axis": {"label": "Dose (μM)", "minimum": 0, "maximum": 1},
             "y_axis": {"label": "Mean response (units)", "minimum": 0, "maximum": 10},
             "points": [{"id": "vehicle", "label": "Vehicle"}, {"id": "treatment", "label": "Treatment"}],
             "observations": [
                 {"id": "vehicle", "x": 0, "values": [4, 5, 6]},
                 {"id": "treatment", "x": 1, "values": [8, 9, 10]}]},
         "solution_spec": {
             "points": [
                 {"id": "vehicle", "x": 0, "y": 5, "x_tolerance": 0, "y_tolerance": 0.01},
                 {"id": "treatment", "x": 1, "y": 9, "x_tolerance": 0, "y_tolerance": 0.01}],
             "rubric": [
                 {"id": "vehicle_x", "criterion": "Vehicle dose coordinate", "points": 0.5, "evidence": ["The vehicle point lies at zero dose."]},
                 {"id": "vehicle_y", "criterion": "Vehicle mean coordinate", "points": 0.5, "evidence": ["The vehicle replicate mean is five response units."]},
                 {"id": "treatment_x", "criterion": "Treatment dose coordinate", "points": 0.5, "evidence": ["The treatment point lies at one micromolar."]},
                 {"id": "treatment_y", "criterion": "Treatment mean coordinate", "points": 0.5, "evidence": ["The treatment replicate mean is nine response units."]}]},
         "feedback": {"hint": "Average replicates within a group before plotting the mean.", "solution": "The vehicle mean is 5 at 0 μM; the treatment mean is 9 at 1 μM.", "lesson_ids": ["lesson-one"]}},
    ]}
    (directory / "question-banks" / "practice.json").write_text(json.dumps(questions))
    return root


@pytest.fixture
def app(tmp_path, content_root):
    application = create_app(Settings(database_url=f"sqlite:///{tmp_path}/test.db", content_root=content_root,
                                      private_assessments_root=tmp_path / "private-assessments",
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
