from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    JSON,
    Boolean,
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    String,
    Text,
    UniqueConstraint,
    create_engine,
    false,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


def now() -> datetime:
    """Database timestamps are timezone-naive UTC for portable deterministic tests."""
    return datetime.utcnow()


def identifier() -> str:
    return str(uuid4())


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    email: Mapped[str | None] = mapped_column(String(254), unique=True, nullable=True)
    password_hash: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_guest: Mapped[bool] = mapped_column(Boolean, default=True)
    is_instructor: Mapped[bool] = mapped_column(Boolean, default=False, server_default=false())
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class SessionToken(Base):
    __tablename__ = "sessions"
    token_hash: Mapped[str] = mapped_column(String(64), primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    csrf_token: Mapped[str] = mapped_column(String(64))
    expires_at: Mapped[datetime] = mapped_column(DateTime, index=True)


class Enrollment(Base):
    __tablename__ = "enrollments"
    __table_args__ = (UniqueConstraint("user_id", "course_id", name="uq_enrollment_user_course"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    course_id: Mapped[str] = mapped_column(String(100))
    content_version: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class AssessmentPlan(Base):
    """Immutable policy snapshot attached to an enrollment and content version."""
    __tablename__ = "assessment_plans"
    __table_args__ = (UniqueConstraint("enrollment_id", "content_version", name="uq_assessment_plan_version"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    enrollment_id: Mapped[str] = mapped_column(ForeignKey("enrollments.id", ondelete="CASCADE"), index=True)
    content_version: Mapped[str] = mapped_column(String(100))
    grading_mode: Mapped[str] = mapped_column(String(32))
    policy_json: Mapped[dict] = mapped_column(JSON)
    snapshot_sha256: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class AssessmentInstance(Base):
    """Safe manifest reference snapshot; question keys are never stored here."""
    __tablename__ = "assessment_instances"
    __table_args__ = (
        UniqueConstraint("plan_id", "assessment_id", name="uq_assessment_instance_id"),
        CheckConstraint("mode IN ('practice', 'graded', 'self-assessment')", name="ck_assessment_instance_mode"),
        CheckConstraint("points >= 0", name="ck_assessment_instance_points_nonnegative"),
        CheckConstraint("attempt_limit IS NULL OR attempt_limit >= 1", name="ck_assessment_instance_attempt_limit"),
    )
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    plan_id: Mapped[str] = mapped_column(ForeignKey("assessment_plans.id", ondelete="CASCADE"), index=True)
    assessment_id: Mapped[str] = mapped_column(String(120))
    assessment_type: Mapped[str] = mapped_column(String(32))
    mode: Mapped[str] = mapped_column(String(24))
    title: Mapped[str | None] = mapped_column(String(240), nullable=True)
    category_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    week: Mapped[int | None] = mapped_column(nullable=True)
    points: Mapped[float] = mapped_column(Float)
    source_path: Mapped[str] = mapped_column(Text)
    source_sha256: Mapped[str] = mapped_column(String(64))
    objective_ids: Mapped[list] = mapped_column(JSON, default=list)
    question_ids: Mapped[list] = mapped_column(JSON, default=list)
    release_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    due_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    attempt_limit: Mapped[int | None] = mapped_column(nullable=True)
    attempt_scoring: Mapped[str] = mapped_column(String(16), default="highest")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class GradedSubmission(Base):
    """Append-only, enrollment-scoped submission for a pinned graded activity."""
    __tablename__ = "graded_submissions"
    __table_args__ = (
        UniqueConstraint(
            "enrollment_id", "assessment_instance_id", "attempt_number",
            name="uq_graded_submission_attempt",
        ),
        CheckConstraint("attempt_number >= 1", name="ck_graded_submission_attempt_positive"),
        CheckConstraint("score >= 0", name="ck_graded_submission_score_nonnegative"),
        CheckConstraint("max_score > 0", name="ck_graded_submission_max_score_positive"),
        CheckConstraint("score <= max_score", name="ck_graded_submission_score_lte_max"),
    )
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    enrollment_id: Mapped[str] = mapped_column(ForeignKey("enrollments.id", ondelete="CASCADE"), index=True)
    plan_id: Mapped[str] = mapped_column(ForeignKey("assessment_plans.id", ondelete="CASCADE"), index=True)
    assessment_instance_id: Mapped[str] = mapped_column(
        ForeignKey("assessment_instances.id", ondelete="CASCADE"), index=True
    )
    content_version: Mapped[str] = mapped_column(String(100))
    attempt_number: Mapped[int] = mapped_column()
    source_sha256: Mapped[str] = mapped_column(String(64))
    question_spec_sha256: Mapped[str] = mapped_column(String(64))
    responses_json: Mapped[dict] = mapped_column(JSON)
    results_json: Mapped[list] = mapped_column(JSON)
    score: Mapped[float] = mapped_column(Float)
    max_score: Mapped[float] = mapped_column(Float)
    submitted_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class GradedSubmissionAppeal(Base):
    """One immutable learner request for a human review of a graded submission."""
    __tablename__ = "graded_submission_appeals"
    __table_args__ = (UniqueConstraint("submission_id", name="uq_graded_submission_appeal_submission"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    submission_id: Mapped[str] = mapped_column(
        ForeignKey("graded_submissions.id", ondelete="CASCADE"), index=True
    )
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    reason: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class GradedSubmissionAppealReview(Base):
    """Append-only graded-submission review; the automatic score stays unchanged."""
    __tablename__ = "graded_submission_appeal_reviews"
    __table_args__ = (
        UniqueConstraint("appeal_id", name="uq_graded_submission_appeal_review_appeal"),
        CheckConstraint(
            "decision IN ('adjusted', 'upheld', 'declined')",
            name="ck_graded_submission_appeal_review_decision",
        ),
        CheckConstraint(
            "(decision = 'adjusted' AND override_score IS NOT NULL) OR "
            "(decision IN ('upheld', 'declined') AND override_score IS NULL)",
            name="ck_graded_submission_appeal_review_score_matches_decision",
        ),
        CheckConstraint(
            "override_score IS NULL OR override_score >= 0",
            name="ck_graded_submission_appeal_review_score_nonnegative",
        ),
    )
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    appeal_id: Mapped[str] = mapped_column(
        ForeignKey("graded_submission_appeals.id", ondelete="CASCADE"), index=True
    )
    reviewer_user_id: Mapped[str | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )
    reviewer_email: Mapped[str] = mapped_column(String(254))
    decision: Mapped[str] = mapped_column(String(20))
    review_note: Mapped[str] = mapped_column(Text)
    override_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class Progress(Base):
    __tablename__ = "progress"
    __table_args__ = (UniqueConstraint("user_id", "course_id", "lesson_id", name="uq_progress_lesson"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    course_id: Mapped[str] = mapped_column(String(100))
    lesson_id: Mapped[str] = mapped_column(String(100))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class Note(Base):
    __tablename__ = "notes"
    __table_args__ = (UniqueConstraint("user_id", "course_id", "lesson_id", name="uq_note_lesson"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    course_id: Mapped[str] = mapped_column(String(100))
    lesson_id: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(Text, default="")
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class Bookmark(Base):
    __tablename__ = "bookmarks"
    __table_args__ = (UniqueConstraint("user_id", "course_id", name="uq_bookmark_course"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    course_id: Mapped[str] = mapped_column(String(100))


class Attempt(Base):
    """Attempts are append-only through the application; no update endpoint exists."""
    __tablename__ = "attempts"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    course_id: Mapped[str] = mapped_column(String(100))
    question_id: Mapped[str] = mapped_column(String(100))
    content_version: Mapped[str] = mapped_column(String(100))
    grading_policy_version: Mapped[str] = mapped_column(String(100), default="practice-v1")
    question_spec_sha256: Mapped[str | None] = mapped_column(String(64), nullable=True)
    response: Mapped[dict] = mapped_column(JSON)
    score: Mapped[float] = mapped_column(Float)
    max_score: Mapped[float] = mapped_column(Float)
    result: Mapped[dict] = mapped_column(JSON)
    objective_ids: Mapped[list] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class Appeal(Base):
    """Immutable learner request for a human review of a saved attempt."""
    __tablename__ = "appeals"
    __table_args__ = (UniqueConstraint("attempt_id", name="uq_appeal_attempt"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    attempt_id: Mapped[str] = mapped_column(ForeignKey("attempts.id", ondelete="CASCADE"), index=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    reason: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


class AppealReview(Base):
    """Append-only instructor decision; deterministic attempt rows are untouched."""
    __tablename__ = "appeal_reviews"
    __table_args__ = (
        UniqueConstraint("appeal_id", name="uq_appeal_review_appeal"),
        CheckConstraint(
            "decision IN ('adjusted', 'upheld', 'declined')",
            name="ck_appeal_review_decision",
        ),
        CheckConstraint(
            "(decision = 'adjusted' AND override_score IS NOT NULL) OR "
            "(decision IN ('upheld', 'declined') AND override_score IS NULL)",
            name="ck_appeal_review_score_matches_decision",
        ),
        CheckConstraint("override_score IS NULL OR override_score >= 0", name="ck_appeal_review_score_nonnegative"),
    )
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=identifier)
    appeal_id: Mapped[str] = mapped_column(ForeignKey("appeals.id", ondelete="CASCADE"), index=True)
    reviewer_user_id: Mapped[str | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )
    reviewer_email: Mapped[str] = mapped_column(String(254))
    decision: Mapped[str] = mapped_column(String(20))
    review_note: Mapped[str] = mapped_column(Text)
    override_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now)


def database(database_url: str):
    kwargs = {"connect_args": {"check_same_thread": False}} if database_url.startswith("sqlite") else {}
    engine = create_engine(database_url, **kwargs)
    if database_url.startswith("sqlite"):
        from sqlalchemy import event

        @event.listens_for(engine, "connect")
        def sqlite_foreign_keys(connection, _):
            connection.execute("PRAGMA foreign_keys=ON")
    return engine, sessionmaker(engine, expire_on_commit=False)
