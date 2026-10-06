"""Public schemas intentionally contain no hidden grading specifications."""

import math
import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

MAX_CSV_UPLOAD_BYTES = 32 * 1024
MAX_CSV_UPLOAD_BASE64_CHARS = ((MAX_CSV_UPLOAD_BYTES + 2) // 3) * 4


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Credentials(StrictModel):
    email: str = Field(min_length=3, max_length=254)
    password: str = Field(min_length=12, max_length=256)

    @field_validator("email")
    @classmethod
    def valid_email(cls, value):
        value = value.strip().lower()
        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value):
            raise ValueError("Enter a valid email address")
        return value


class EnrollmentRequest(StrictModel):
    course_id: str = Field(min_length=1, max_length=100)


class ProgressRequest(StrictModel):
    completed: bool


class NoteRequest(StrictModel):
    body: str = Field(max_length=20000)


class BookmarkRequest(StrictModel):
    saved: bool


class AppealRequest(StrictModel):
    reason: str = Field(min_length=20, max_length=4000)

    @field_validator("reason")
    @classmethod
    def meaningful_reason(cls, value):
        value = value.strip()
        if len(value) < 20:
            raise ValueError("Explain what the grader or rubric may have missed (at least 20 characters)")
        return value


class AppealReviewRequest(StrictModel):
    decision: Literal["adjusted", "upheld", "declined"]
    review_note: str = Field(min_length=10, max_length=4000)
    override_score: float | None = Field(default=None, ge=0)

    @field_validator("review_note")
    @classmethod
    def meaningful_review_note(cls, value):
        value = value.strip()
        if len(value) < 10:
            raise ValueError("A review note must explain the decision (at least 10 characters)")
        return value

    @field_validator("override_score")
    @classmethod
    def finite_override_score(cls, value):
        if value is not None and not math.isfinite(value):
            raise ValueError("The override score must be finite")
        return value


class AttemptRequest(StrictModel):
    response: str | float | list[int] | dict[str, str] = Field(union_mode="left_to_right")
    unit: str | None = Field(default=None, max_length=100)
    variant_token: str | None = Field(default=None, max_length=2048)

    @field_validator("response", mode="before")
    @classmethod
    def valid_type(cls, value):
        if isinstance(value, dict):
            if set(value) == {"content_base64"}:
                content = value["content_base64"]
                if (
                    not isinstance(content, str)
                    or not 1 <= len(content) <= MAX_CSV_UPLOAD_BASE64_CHARS
                ):
                    raise ValueError("CSV upload encoding must contain at most 32 KiB of data")
                return value
            if not 1 <= len(value) <= 20:
                raise ValueError("Structured responses must contain 1–20 fields")
            if any(
                not isinstance(key, str)
                or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", key)
                or not isinstance(item, str)
                or not item.strip()
                or len(item) > 1000
                for key, item in value.items()
            ):
                raise ValueError("Structured response fields must have valid IDs and nonempty text values")
            return value
        if isinstance(value, list):
            if not 1 <= len(value) <= 100 or any(type(item) is not int for item in value):
                raise ValueError("Selections must contain 1–100 integer option indexes")
            if len(set(value)) != len(value):
                raise ValueError("An option can only be selected once")
            return value
        if isinstance(value, bool) or not isinstance(value, (str, float, int)):
            raise ValueError("Response must be text or a finite number")
        return value

    @field_validator("response")
    @classmethod
    def bounded_response(cls, value):
        if isinstance(value, dict):
            return value
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            if not value.strip() or len(value) > 10000:
                raise ValueError("Response must contain 1–10000 characters")
        elif not math.isfinite(value):
            raise ValueError("Response must be finite")
        return value


class PublicResponseField(BaseModel):
    id: str
    type: Literal["single_choice", "numeric"]
    prompt: str
    options: list[str] = Field(default_factory=list)
    unit: str | None = None
    points: float = Field(gt=0)


class PublicGraphAxis(BaseModel):
    label: str
    minimum: float
    maximum: float


class PublicGraphPoint(BaseModel):
    id: str
    label: str


class PublicGraphObservation(BaseModel):
    id: str
    x: float
    values: list[float] = Field(min_length=1, max_length=100)


class PublicGraphSpec(BaseModel):
    x_axis: PublicGraphAxis
    y_axis: PublicGraphAxis
    points: list[PublicGraphPoint] = Field(min_length=2, max_length=20)
    observations: list[PublicGraphObservation] = Field(min_length=2, max_length=20)


class PublicQuestion(BaseModel):
    id: str
    type: Literal[
        "single_choice", "multiple_select", "numeric", "symbolic", "structured",
        "data_interpretation", "graph", "file_upload",
    ]
    prompt: str
    options: list[str] = Field(default_factory=list)
    unit: str | None = None
    significant_figures: int | None = Field(default=None, ge=1, le=12)
    points: float = 1
    selection: Literal["single", "multiple"] = "single"
    partial_credit_policy: str | None = None
    response_fields: list[PublicResponseField] = Field(default_factory=list)
    graph_spec: PublicGraphSpec | None = None
    accepted_media_types: list[str] = Field(default_factory=list)
    max_upload_bytes: int | None = Field(default=None, ge=1, le=MAX_CSV_UPLOAD_BYTES)
    variant_id: str | None = None
    variant_token: str | None = None
    learning_objective_ids: list[str] = Field(default_factory=list)
    assessment_role: Literal["formative", "graded"] = "formative"


class PublicRetrievalCard(BaseModel):
    id: str
    front: str
    back: str
    learning_objective_ids: list[str] = Field(default_factory=list)


class PublicLesson(BaseModel):
    id: str
    title: str
    markdown: str
    learning_objective_ids: list[str] = Field(default_factory=list)
    questions: list[PublicQuestion] = Field(default_factory=list)
    retrieval_cards: list[PublicRetrievalCard] = Field(default_factory=list)
    source_ids: list[str] = Field(default_factory=list)
    worked_example: str | None = None


class Objective(BaseModel):
    id: str
    description: str
    bloom: str


class Prerequisites(BaseModel):
    course_ids: list[str] = Field(default_factory=list)
    recommended_course_ids: list[str] = Field(default_factory=list)
    concurrent_course_ids: list[str] = Field(default_factory=list)
    knowledge: list[str] = Field(default_factory=list)
    statement: str = ""


class LessonSummary(BaseModel):
    id: str
    title: str
    learning_objective_ids: list[str] = Field(default_factory=list)


class ModuleSummary(BaseModel):
    id: str
    title: str
    source_ids: list[str] = Field(default_factory=list)
    lessons: list[LessonSummary]


class CourseSummary(BaseModel):
    id: str
    title: str
    description: str
    domain: str
    level: str
    maturity: Literal["catalog-only", "outlined", "partial", "beta", "complete", "externally reviewed"]
    version: str
    lesson_count: int
    limitations: list[str]


class CurriculumNode(BaseModel):
    id: str
    title: str
    domain: str
    level: str
    maturity: Literal["catalog-only", "outlined", "partial", "beta", "complete", "externally reviewed"]
    description: str
    prerequisites: Prerequisites
    package_id: str | None = None
    related_package_ids: list[str] = Field(default_factory=list)
    relation_note: str | None = None


class CurriculumPathway(BaseModel):
    id: str
    title: str
    description: str
    course_ids: list[str]
    source_ids: list[str] = Field(default_factory=list)
    sequence_note: str


class CurriculumAlignment(BaseModel):
    id: str
    title: str
    source_ids: list[str]
    foundational_nodes: list[str]
    advanced_nodes: list[str]
    disclaimer: str


class PublicCurriculum(BaseModel):
    schema_version: str
    description: str
    nodes: list[CurriculumNode]
    pathways: list[CurriculumPathway]
    alignment_maps: list[CurriculumAlignment]


class PublicCourse(CourseSummary):
    prerequisites: Prerequisites
    outcomes: list[Objective]
    lesson_objectives: list[Objective]
    modules: list[ModuleSummary]
    syllabus_markdown: str
    license: str
    review_status: str
    assessment_policy: str = "Formative practice only; no credit or university prerequisite equivalency."


class AssessmentCategoryView(BaseModel):
    id: str
    title: str | None = None
    weight: float = Field(ge=0, le=1)


class AssessmentInstanceView(BaseModel):
    id: str
    title: str
    type: str
    mode: Literal["practice", "graded", "self-assessment"]
    category_id: str | None = None
    week: int | None = Field(default=None, ge=1, le=52)
    points: float = Field(ge=0)
    item_count: int = Field(ge=0)
    objective_count: int = Field(ge=0)
    release_at: str | None = None
    due_at: str | None = None
    attempt_limit: int | None = Field(default=None, ge=1)
    attempt_scoring: Literal["highest", "latest"]
    schedule_status: Literal["practice", "upcoming", "open", "closed"]


class AssessmentPlanResponse(BaseModel):
    course_id: str
    content_version: str
    grading_mode: Literal["formative-only", "graded-course"]
    course_grade_status: Literal[
        "not_configured", "configured_no_submissions", "configured_with_submissions"
    ]
    categories: list[AssessmentCategoryView]
    category_aggregation: Literal["points", "assessment-average"]
    attempt_policy: str
    solution_release: str
    late_policy: str
    appeals: str
    assessments: list[AssessmentInstanceView]


class FeedbackComponent(BaseModel):
    field_id: str
    label: str
    score: float = Field(ge=0)
    max_score: float = Field(gt=0)
    diagnosis: str


class Feedback(BaseModel):
    diagnosis: str
    hint: str | None = None
    misconception: str | None = None
    next_step: str
    lesson_id: str | None = None
    reasoning_assessed: bool = False
    provisional: bool = False
    components: list[FeedbackComponent] = Field(default_factory=list)


class AssessmentSubmissionRequest(StrictModel):
    responses: dict[str, AttemptRequest]

    @field_validator("responses")
    @classmethod
    def valid_responses(cls, value):
        if not 1 <= len(value) <= 100:
            raise ValueError("A submission must contain 1–100 question responses")
        if any(not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,99}", key) for key in value):
            raise ValueError("Question response IDs must be valid identifiers")
        if any(item.variant_token is not None for item in value.values()):
            raise ValueError("Assignment responses cannot include practice variant tokens")
        return value


class AssessmentQuestionsResponse(BaseModel):
    course_id: str
    assessment_id: str
    title: str
    content_version: str
    points: float = Field(gt=0)
    questions: list[PublicQuestion]
    attempts_used: int = Field(ge=0)
    attempt_limit: int | None = Field(default=None, ge=1)
    schedule_status: Literal["open", "closed"]


class AssignmentQuestionResult(BaseModel):
    question_id: str
    score: float = Field(ge=0)
    max_score: float = Field(gt=0)
    feedback: Feedback


class AssessmentSubmissionResponse(BaseModel):
    id: str
    course_id: str
    assessment_id: str
    content_version: str
    attempt_number: int = Field(ge=1)
    responses: dict[str, AttemptRequest]
    results: list[AssignmentQuestionResult]
    score: float = Field(ge=0)
    max_score: float = Field(gt=0)
    score_percent: float = Field(ge=0, le=100)
    submitted_at: str


class CourseGradeView(BaseModel):
    score_percent: float | None = Field(default=None, ge=0, le=100)
    category_scores: dict[str, float | None]
    active_weight: float = Field(ge=0, le=1)
    policy_version: Literal["weighted-grade-v1"]
    status: Literal["configured_no_submissions", "in_progress"]
    explanation: str


class GradeResult(BaseModel):
    score: float
    max_score: float
    correct: bool
    feedback: Feedback
    grading_policy_version: str = "practice-v1"
    assessment_role: Literal["formative"] = "formative"


class ObjectiveEvidence(BaseModel):
    attempts: int = Field(ge=0)
    correct_results: int = Field(ge=0)
    attempted_items: int = Field(ge=0)
    item_count: int = Field(ge=0)
    best_score: float = Field(ge=0)
    best_possible_score: float = Field(ge=0)
    performance: float | None = Field(default=None, ge=0, le=1)
    status: Literal[
        "no_evidence", "insufficient_evidence", "needs_practice", "provisional_practice_mastery"
    ]


class ObjectiveEvidencePolicy(BaseModel):
    version: Literal["practice-evidence-v1"] = "practice-evidence-v1"
    minimum_distinct_items: int = Field(default=3, ge=1)
    minimum_item_coverage: float = Field(default=0.8, ge=0, le=1)
    minimum_performance: float = Field(default=0.8, ge=0, le=1)


class GradebookResponse(BaseModel):
    course_id: str
    assessment_role: Literal["formative"] = "formative"
    aggregation: str
    score: float = Field(ge=0)
    max_score: float = Field(ge=0)
    attempt_count: int = Field(ge=0)
    manual_override_count: int = Field(ge=0)
    objective_evidence_policy: ObjectiveEvidencePolicy
    objective_evidence: dict[str, ObjectiveEvidence]
    limitations: str
    course_grade: CourseGradeView | None = None
