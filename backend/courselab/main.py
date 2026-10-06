"""FastAPI learner service with server ownership and formative-only assessment."""

import base64
import binascii
import hashlib
import json
import math
import secrets
import time
from collections import defaultdict, deque
from datetime import timedelta
from typing import Annotated

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError
from fastapi import Depends, FastAPI, HTTPException, Query, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import delete, func, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .assessment import (
    calculate_weighted_grade,
    canonical_digest,
    utc_datetime,
    validate_assessment_configuration,
)
from .config import Settings
from .content import ContentInvalid, ContentMissing, ContentRepository
from .db import (
    Appeal,
    AppealReview,
    AssessmentInstance,
    AssessmentPlan,
    Attempt,
    Bookmark,
    Enrollment,
    GradedSubmission,
    GradedSubmissionAppeal,
    GradedSubmissionAppealReview,
    Note,
    Progress,
    SessionToken,
    User,
    database,
    now,
)
from .evidence import (
    MIN_DISTINCT_ITEMS,
    MIN_ITEM_COVERAGE,
    MIN_PERFORMANCE,
    POLICY_VERSION,
    objective_evidence,
)
from .grading import GradingUnavailable, grade, question_spec_digest
from .schemas import (
    AppealRequest,
    AppealReviewRequest,
    AssessmentPlanResponse,
    AssessmentQuestionsResponse,
    AssessmentSubmissionRequest,
    AssessmentSubmissionResponse,
    AttemptRequest,
    BookmarkRequest,
    CourseSummary,
    Credentials,
    EnrollmentRequest,
    GradebookResponse,
    GradedSubmissionAppealResponse,
    InstructorGradedSubmissionAppealResponse,
    NoteRequest,
    PracticeAssessmentResponse,
    ProgressRequest,
    PublicCourse,
    PublicCurriculum,
    PublicLesson,
)
from .variants import VariantTokenError, issue_variant_token, resolve_variant, verify_variant_token

COOKIE = "courselab_session"
PASSWORDS = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=2)


def token_hash(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def user_view(user: User) -> dict:
    return {"id": user.id, "email": user.email, "is_guest": user.is_guest}


def can_review(user: User) -> bool:
    """Only an operator-provisioned, registered account may adjudicate appeals."""
    return not user.is_guest and bool(user.email) and user.is_instructor


def appeal_view(appeal: Appeal, attempt: Attempt, review: AppealReview | None = None) -> dict:
    status = review.decision if review else "open"
    effective_score = (
        float(review.override_score)
        if review and review.decision == "adjusted"
        else float(attempt.score)
    )
    return {
        "id": appeal.id,
        "attempt_id": attempt.id,
        "course_id": attempt.course_id,
        "question_id": attempt.question_id,
        "reason": appeal.reason,
        "status": status,
        "decision": review.decision if review else None,
        "review_note": review.review_note if review else None,
        "original_score": float(attempt.score),
        "effective_score": effective_score,
        "max_score": float(attempt.max_score),
        "created_at": timestamp(appeal.created_at),
        "reviewed_at": timestamp(review.created_at) if review else None,
    }


def timestamp(value) -> str:
    """Expose naive database UTC as unambiguous ISO8601 UTC to browsers."""
    return value.isoformat(timespec="microseconds") + "Z"


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings.from_environment()
    app = FastAPI(title="uniStemCourseSimulators API", version="0.2.0", docs_url=None, redoc_url=None)
    engine, session_factory = database(settings.database_url)
    content = ContentRepository(settings.content_root)
    app.state.engine = engine
    app.state.sessions = session_factory
    app.state.content = content
    app.state.settings = settings
    app.add_middleware(CORSMiddleware, allow_origins=list(settings.allowed_origins), allow_credentials=True,
                       allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
                       allow_headers=["Content-Type", "X-CSRF-Token"])
    dummy_password_hash = PASSWORDS.hash(secrets.token_urlsafe(24))
    # In-memory throttling is appropriate to the single-worker development slice.
    # Production multi-worker deployment must put a shared rate limiter at the proxy.
    requests: dict[tuple[str, str], deque] = defaultdict(deque)

    @app.middleware("http")
    async def boundaries(request: Request, call_next):
        unsafe = request.method not in {"GET", "HEAD", "OPTIONS"}
        if unsafe:
            origin = request.headers.get("origin")
            if origin not in settings.allowed_origins:
                return JSONResponse({"detail": "A permitted Origin is required for mutations"}, status_code=403)
            try:
                if int(request.headers.get("content-length", "0")) > settings.body_limit:
                    return JSONResponse({"detail": "Submission too large"}, status_code=413)
            except ValueError:
                return JSONResponse({"detail": "Malformed content length"}, status_code=400)
            # Stream only up to the ceiling and replay the cached body to FastAPI.
            chunks, size = [], 0
            async for chunk in request.stream():
                size += len(chunk)
                if size > settings.body_limit:
                    return JSONResponse({"detail": "Submission too large"}, status_code=413)
                chunks.append(chunk)
            request._body = b"".join(chunks)
            # Security-sensitive path decisions use the router's raw ASGI path,
            # not URL reconstruction from caller-controlled Host values.
            category = "auth" if request.scope["path"].startswith("/api/v1/auth") else "write"
            key = (request.client.host if request.client else "unknown", category)
            bucket = requests[key]
            instant = time.monotonic()
            while bucket and instant - bucket[0] >= 60:
                bucket.popleft()
            limit = settings.auth_rate_limit if category == "auth" else settings.rate_limit
            if len(bucket) >= limit:
                return JSONResponse({"detail": "Try again later"}, status_code=429, headers={"Retry-After": "60"})
            bucket.append(instant)
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.exception_handler(ContentMissing)
    async def missing(_, exception):
        return JSONResponse({"detail": str(exception)}, status_code=404)

    @app.exception_handler(ContentInvalid)
    async def invalid(_, __):
        return JSONResponse({"detail": "Invalid server content package"}, status_code=503)

    @app.exception_handler(GradingUnavailable)
    async def grading_unavailable(_, exception):
        return JSONResponse({"detail": str(exception), "capability": "unavailable"}, status_code=422)

    @app.exception_handler(IntegrityError)
    async def conflict(_, __):
        # The yielded session is closed/rolled back after the request. Never return
        # SQL, parameter values, database connection strings or driver tracebacks.
        return JSONResponse({"detail": "Conflicting or concurrent update; reload and retry"}, status_code=409)

    def db_session():
        with session_factory() as session:
            yield session

    DB = Annotated[Session, Depends(db_session)]

    def optional_identity(request: Request, db: Session) -> tuple[User, SessionToken] | None:
        raw = request.cookies.get(COOKIE)
        if not raw or len(raw) > 128:
            return None
        stored = db.get(SessionToken, token_hash(raw))
        if not stored or stored.expires_at <= now():
            return None
        user = db.get(User, stored.user_id)
        return (user, stored) if user else None

    def require_identity(request: Request, db: Session) -> tuple[User, SessionToken]:
        identity = optional_identity(request, db)
        if not identity:
            raise HTTPException(401, "Start a guest session or sign in")
        return identity

    def require_csrf(request: Request, identity: tuple[User, SessionToken]):
        supplied = request.headers.get("x-csrf-token", "")
        if not supplied or not secrets.compare_digest(supplied, identity[1].csrf_token):
            raise HTTPException(403, "CSRF token missing or invalid")

    def enrolled(db: Session, user: User, course_id: str) -> Enrollment:
        enrollment = db.scalar(select(Enrollment).where(
            Enrollment.user_id == user.id, Enrollment.course_id == course_id
        ))
        if not enrollment:
            raise HTTPException(403, "Enroll in this course first")
        current_version = content.manifest(course_id)["version"]
        if enrollment.content_version != current_version:
            raise HTTPException(409, "The course version changed; a reviewed enrollment migration is required")
        return enrollment

    def assessment_policy(manifest: dict) -> dict:
        policy = dict(manifest.get("grading_policy") or {})
        policy.setdefault("mode", "formative-only")
        policy.setdefault("categories", [])
        policy.setdefault("category_aggregation", "points")
        policy.setdefault("late_submission_policy", "strict-deadline")
        policy.setdefault("attempt_policy", "No course grade is configured.")
        policy.setdefault("solution_release", "Not specified.")
        policy.setdefault("late_policy", "No course grade is configured.")
        policy.setdefault("appeals", "Use the supported formative attempt review workflow.")
        return policy

    def ensure_assessment_plan(db: Session, enrollment: Enrollment, manifest: dict) -> AssessmentPlan:
        existing = db.scalar(select(AssessmentPlan).where(
            AssessmentPlan.enrollment_id == enrollment.id,
            AssessmentPlan.content_version == enrollment.content_version,
        ))
        if existing:
            return existing
        if enrollment.content_version != manifest["version"]:
            raise HTTPException(409, "This historical enrollment has no assessment snapshot; review the current version first")

        source_assessments = manifest.get("assessments", [])
        policy = assessment_policy(manifest)
        normalized_assessments = []
        for source in source_assessments:
            item = dict(source)
            item["attempt_scoring"] = item.get("attempt_scoring", "highest")
            item["attempt_limit"] = item.get("attempt_limit")
            item["release_at"] = item.get("release_at")
            item["due_at"] = item.get("due_at")
            normalized_assessments.append(item)
        try:
            validate_assessment_configuration(normalized_assessments, policy)
        except (AttributeError, KeyError, TypeError, ValueError) as exc:
            raise HTTPException(409, "The course assessment configuration is invalid") from exc

        for item in normalized_assessments:
            try:
                source_file = content.assessment_source_file(enrollment.course_id, item["path"])
                item["_source_sha256"] = hashlib.sha256(source_file.read_bytes()).hexdigest()
            except (ContentInvalid, ContentMissing, KeyError, OSError) as exc:
                raise HTTPException(409, "An assessment source is missing or invalid") from exc

        snapshot = {
            "course_id": enrollment.course_id,
            "content_version": enrollment.content_version,
            "grading_policy": policy,
            "assessments": normalized_assessments,
        }
        plan = AssessmentPlan(
            enrollment_id=enrollment.id,
            content_version=enrollment.content_version,
            grading_mode=policy["mode"],
            policy_json=policy,
            snapshot_sha256=canonical_digest(snapshot),
        )
        db.add(plan)
        db.flush()
        for item in normalized_assessments:
            db.add(AssessmentInstance(
                plan_id=plan.id,
                assessment_id=item["id"],
                assessment_type=item["type"],
                mode=item["mode"],
                title=item.get("title"),
                category_id=item.get("category_id"),
                week=item.get("week"),
                points=float(item["points"]),
                source_path=item["path"],
                source_sha256=item["_source_sha256"],
                objective_ids=item.get("objective_ids", []),
                question_ids=item.get("question_ids", []),
                release_at=utc_datetime(item.get("release_at")),
                due_at=utc_datetime(item.get("due_at")),
                attempt_limit=item.get("attempt_limit"),
                attempt_scoring=item["attempt_scoring"],
            ))
        db.flush()
        return plan

    def graded_assessment(
        db: Session, enrollment: Enrollment, manifest: dict, assessment_id: str,
    ) -> tuple[AssessmentPlan, AssessmentInstance, list[dict], int, str]:
        """Load only an enrollment-pinned graded activity with verified source bytes."""
        plan = ensure_assessment_plan(db, enrollment, manifest)
        if plan.grading_mode != "graded-course":
            raise HTTPException(404, "No graded assessments are configured for this course")
        instance = db.scalar(select(AssessmentInstance).where(
            AssessmentInstance.plan_id == plan.id,
            AssessmentInstance.assessment_id == assessment_id,
        ))
        if not instance or instance.mode != "graded":
            raise HTTPException(404, "Graded assessment not found")
        try:
            source_path = content.assessment_source_file(enrollment.course_id, instance.source_path)
            source_bytes = source_path.read_bytes()
        except (ContentInvalid, ContentMissing, OSError) as exc:
            raise HTTPException(409, "The pinned assessment source is unavailable") from exc
        source_sha256 = hashlib.sha256(source_bytes).hexdigest()
        if not secrets.compare_digest(source_sha256, instance.source_sha256):
            raise HTTPException(409, "Assessment content changed after this enrollment version was pinned")
        try:
            package = json.loads(source_bytes.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise HTTPException(409, "The pinned assessment source is invalid") from exc
        if (
            not isinstance(package, dict)
            or package.get("course_id") != enrollment.course_id
            or not isinstance(package.get("questions"), list)
        ):
            raise HTTPException(409, "The pinned assessment source has an invalid course mapping")
        questions_by_id = {}
        for question in package["questions"]:
            question_id = question.get("id") if isinstance(question, dict) else None
            if not isinstance(question_id, str) or question_id in questions_by_id:
                raise HTTPException(409, "The pinned assessment has invalid question identifiers")
            questions_by_id[question_id] = question
        question_ids = instance.question_ids
        if (
            not isinstance(question_ids, list)
            or not question_ids
            or any(not isinstance(question_id, str) for question_id in question_ids)
            or len(question_ids) != len(set(question_ids))
            or any(question_id not in questions_by_id for question_id in question_ids)
        ):
            raise HTTPException(409, "The pinned assessment question mapping is invalid")
        questions = [questions_by_id[question_id] for question_id in question_ids]
        try:
            question_points = sum(float(question["points"]) for question in questions)
        except (KeyError, TypeError, ValueError) as exc:
            raise HTTPException(409, "The pinned assessment point mapping is invalid") from exc
        if not math.isclose(question_points, float(instance.points), rel_tol=0, abs_tol=1e-8):
            raise HTTPException(409, "Question points do not match the pinned assessment total")
        attempts_used = db.scalar(select(func.count()).select_from(GradedSubmission).where(
            GradedSubmission.enrollment_id == enrollment.id,
            GradedSubmission.assessment_instance_id == instance.id,
        )) or 0
        try:
            spec_digest = canonical_digest({
                "grader": [question_spec_digest(question) for question in questions],
                "source_sha256": instance.source_sha256,
            })
        except (TypeError, ValueError) as exc:
            raise HTTPException(409, "The pinned assessment grading specification is invalid") from exc
        return plan, instance, questions, int(attempts_used), spec_digest

    def graded_submission_appeal_view(
        appeal: GradedSubmissionAppeal,
        submission: GradedSubmission,
        instance: AssessmentInstance,
        course_id: str,
        review: GradedSubmissionAppealReview | None = None,
    ) -> dict:
        effective_score = (
            float(review.override_score)
            if review and review.decision == "adjusted"
            else float(submission.score)
        )
        return {
            "id": appeal.id,
            "submission_id": submission.id,
            "course_id": course_id,
            "assessment_id": instance.assessment_id,
            "attempt_number": submission.attempt_number,
            "reason": appeal.reason,
            "status": review.decision if review else "open",
            "decision": review.decision if review else None,
            "review_note": review.review_note if review else None,
            "original_score": float(submission.score),
            "effective_score": effective_score,
            "max_score": float(submission.max_score),
            "created_at": timestamp(appeal.created_at),
            "reviewed_at": timestamp(review.created_at) if review else None,
        }

    def graded_submission_view(
        item: GradedSubmission, instance: AssessmentInstance, course_id: str, db: Session,
    ) -> dict:
        appeal = db.scalar(select(GradedSubmissionAppeal).where(
            GradedSubmissionAppeal.submission_id == item.id
        ))
        review = (
            db.scalar(select(GradedSubmissionAppealReview).where(
                GradedSubmissionAppealReview.appeal_id == appeal.id
            ))
            if appeal else None
        )
        effective_score = (
            float(review.override_score)
            if review and review.decision == "adjusted"
            else float(item.score)
        )
        return {
            "id": item.id,
            "course_id": course_id,
            "assessment_id": instance.assessment_id,
            "content_version": item.content_version,
            "attempt_number": item.attempt_number,
            "responses": item.responses_json,
            "results": item.results_json,
            "score": float(item.score),
            "effective_score": effective_score,
            "max_score": float(item.max_score),
            "score_percent": round(float(item.score) / float(item.max_score) * 100, 2),
            "effective_score_percent": round(effective_score / float(item.max_score) * 100, 2),
            "submitted_at": timestamp(item.submitted_at),
            "appeal": graded_submission_appeal_view(appeal, item, instance, course_id, review) if appeal else None,
        }

    def verified_graded_review_questions(
        submission: GradedSubmission,
        enrollment: Enrollment,
        plan: AssessmentPlan,
        instance: AssessmentInstance,
    ) -> list[dict] | None:
        """Return exact answer-free question specs only while every saved digest matches."""
        try:
            if (
                submission.plan_id != plan.id
                or submission.assessment_instance_id != instance.id
                or instance.plan_id != plan.id
                or plan.enrollment_id != enrollment.id
                or plan.grading_mode != "graded-course"
                or plan.content_version != submission.content_version
                or enrollment.content_version != submission.content_version
            ):
                return None
            manifest = content.manifest(enrollment.course_id)
            if manifest.get("version") != submission.content_version:
                return None
            source_path = content.assessment_source_file(enrollment.course_id, instance.source_path)
            source_bytes = source_path.read_bytes()
            source_sha256 = hashlib.sha256(source_bytes).hexdigest()
            if (
                source_sha256 != instance.source_sha256
                or source_sha256 != submission.source_sha256
                or instance.mode != "graded"
                or instance.question_ids == []
            ):
                return None
            package = json.loads(source_bytes.decode("utf-8"))
            if package.get("course_id") != enrollment.course_id or not isinstance(package.get("questions"), list):
                return None
            by_id = {}
            for question in package["questions"]:
                question_id = question.get("id") if isinstance(question, dict) else None
                if not isinstance(question_id, str) or question_id in by_id:
                    return None
                by_id[question_id] = question
            question_ids = instance.question_ids
            if (
                not isinstance(question_ids, list)
                or not question_ids
                or len(question_ids) != len(set(question_ids))
                or any(question_id not in by_id for question_id in question_ids)
            ):
                return None
            questions = [by_id[question_id] for question_id in question_ids]
            points = sum(float(question["points"]) for question in questions)
            if not math.isclose(points, float(instance.points), rel_tol=0, abs_tol=1e-8):
                return None
            if not math.isclose(points, float(submission.max_score), rel_tol=0, abs_tol=1e-8):
                return None
            spec_digest = canonical_digest({
                "grader": [question_spec_digest(question) for question in questions],
                "source_sha256": instance.source_sha256,
            })
            if spec_digest != submission.question_spec_sha256:
                return None
            if set(submission.responses_json) != set(question_ids):
                return None
            if {result.get("question_id") for result in submission.results_json} != set(question_ids):
                return None
            return questions
        except (
            ContentInvalid, ContentMissing, OSError, UnicodeDecodeError, json.JSONDecodeError,
            AttributeError, KeyError, TypeError, ValueError, ArithmeticError,
        ):
            return None

    def graded_instructor_appeal_record(
        appeal: GradedSubmissionAppeal,
        submission: GradedSubmission,
        db: Session,
    ) -> dict:
        enrollment = db.get(Enrollment, submission.enrollment_id)
        instance = db.get(AssessmentInstance, submission.assessment_instance_id)
        plan = db.get(AssessmentPlan, submission.plan_id)
        review = db.scalar(select(GradedSubmissionAppealReview).where(
            GradedSubmissionAppealReview.appeal_id == appeal.id
        ))
        learner = db.get(User, appeal.user_id)
        questions = (
            verified_graded_review_questions(submission, enrollment, plan, instance)
            if enrollment and plan and instance else None
        )
        public_questions = None
        public_responses = {}
        if questions is not None:
            public_questions = [
                content.public_question(question)
                .model_copy(update={"assessment_role": "graded"})
                .model_dump()
                for question in questions
            ]
            question_by_id = {question["id"]: question for question in questions}
            try:
                for question_id, raw_response in submission.responses_json.items():
                    data = dict(raw_response)
                    value = data.get("response")
                    if question_by_id[question_id].get("type") == "file_upload":
                        encoded = value.get("content_base64") if isinstance(value, dict) else None
                        if not isinstance(encoded, str):
                            raise ValueError("Missing saved CSV upload")
                        decoded = base64.b64decode(encoded, validate=True).decode("utf-8-sig")
                        value = {"content_text": decoded}
                    data["response"] = value
                    public_responses[question_id] = AttemptRequest.model_validate(data).model_dump(exclude_none=True)
            except (AttributeError, binascii.Error, KeyError, TypeError, UnicodeDecodeError, ValueError):
                questions = None
                public_questions = None
                public_responses = {}
        view = graded_submission_appeal_view(
            appeal, submission, instance, enrollment.course_id, review
        ) if instance and enrollment else {
            "id": appeal.id,
            "submission_id": submission.id,
            "course_id": enrollment.course_id if enrollment else "",
            "assessment_id": "",
            "attempt_number": submission.attempt_number,
            "reason": appeal.reason,
            "status": review.decision if review else "open",
            "decision": review.decision if review else None,
            "review_note": review.review_note if review else None,
            "original_score": float(submission.score),
            "effective_score": float(review.override_score) if review and review.decision == "adjusted" else float(submission.score),
            "max_score": float(submission.max_score),
            "created_at": timestamp(appeal.created_at),
            "reviewed_at": timestamp(review.created_at) if review else None,
        }
        return {
            **view,
            "learner": learner.email if learner and learner.email else "Guest account",
            "content_is_current": questions is not None,
            "assessment_title": instance.title or instance.assessment_id if instance else "Unavailable assessment",
            "questions": public_questions,
            "responses": public_responses,
            "automatic_results": submission.results_json,
            "specification_pinned": bool(submission.question_spec_sha256),
        }

    def start_session(db: Session, user: User, response: Response, request: Request) -> dict:
        # Revoke the calling session when logging in or converting a guest.
        old = optional_identity(request, db)
        if old:
            db.delete(old[1])
        raw, csrf = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
        hours = settings.guest_hours if user.is_guest else settings.session_hours
        db.add(SessionToken(token_hash=token_hash(raw), user_id=user.id,
                            csrf_token=csrf, expires_at=now() + timedelta(hours=hours)))
        db.commit()
        response.set_cookie(COOKIE, raw, httponly=True, secure=settings.cookie_secure,
                            samesite="lax", max_age=hours * 3600, path="/api")
        return {
            "user": user_view(user), "csrf_token": csrf,
            "can_review": can_review(user),
        }

    def require_reviewer(request: Request, db: Session, mutation: bool = False) -> User:
        identity = require_identity(request, db)
        user = identity[0]
        if not can_review(user):
            raise HTTPException(403, "Instructor review access is not enabled for this account")
        if mutation:
            require_csrf(request, identity)
        return user

    @app.get("/api/v1/health")
    def health(db: DB):
        db.execute(select(1))
        return {"status": "ok", "programming_runner": "disabled", "llm_feedback": "disabled"}

    @app.get("/api/v1/auth/session")
    def session_info(request: Request, response: Response, db: DB):
        identity = optional_identity(request, db)
        if not identity:
            response.delete_cookie(COOKIE, path="/api")
            return {"user": None, "csrf_token": None, "can_review": False}
        user = identity[0]
        return {
            "user": user_view(user), "csrf_token": identity[1].csrf_token,
            "can_review": can_review(user),
        }

    @app.post("/api/v1/auth/guest")
    def guest(request: Request, response: Response, db: DB):
        identity = optional_identity(request, db)
        if identity:
            require_csrf(request, identity)
            user = identity[0]
            return {
                "user": user_view(user), "csrf_token": identity[1].csrf_token,
                "can_review": can_review(user),
            }
        user = User(is_guest=True)
        db.add(user)
        db.flush()
        return start_session(db, user, response, request)

    @app.post("/api/v1/auth/register", status_code=201)
    def register(body: Credentials, request: Request, response: Response, db: DB):
        if db.scalar(select(User).where(User.email == body.email)):
            raise HTTPException(409, "Account unavailable")
        identity = optional_identity(request, db)
        if identity:
            require_csrf(request, identity)
            if not identity[0].is_guest:
                raise HTTPException(409, "Sign out before registering another account")
            user = identity[0]
        else:
            user = User()
            db.add(user)
        user.email = body.email
        user.password_hash = PASSWORDS.hash(body.password)
        user.is_guest = False
        db.flush()
        return start_session(db, user, response, request)

    @app.post("/api/v1/auth/login")
    def login(body: Credentials, request: Request, response: Response, db: DB):
        identity = optional_identity(request, db)
        if identity:
            require_csrf(request, identity)
        user = db.scalar(select(User).where(User.email == body.email, User.is_guest.is_(False)))
        # Keep hash verification work similar for unknown accounts.
        candidate = user.password_hash if user else dummy_password_hash
        try:
            valid = PASSWORDS.verify(candidate, body.password)
        except (VerifyMismatchError, VerificationError, InvalidHashError):
            valid = False
        if not user or not valid:
            raise HTTPException(401, "Email or password incorrect")
        return start_session(db, user, response, request)

    @app.post("/api/v1/auth/logout", status_code=204)
    def logout(request: Request, response: Response, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        db.delete(identity[1])
        db.commit()
        response.delete_cookie(COOKIE, path="/api")

    @app.get("/api/v1/courses", response_model=list[CourseSummary])
    def courses():
        return content.catalog()

    @app.get("/api/v1/curriculum", response_model=PublicCurriculum)
    def curriculum():
        return content.curriculum()

    @app.get("/api/v1/sources")
    def sources():
        return content.sources()

    @app.get("/api/v1/courses/{course_id}", response_model=PublicCourse)
    def course(course_id: str):
        return content.course(course_id)

    @app.get("/api/v1/courses/{course_id}/lessons/{lesson_id}", response_model=PublicLesson)
    def lesson(course_id: str, lesson_id: str, request: Request, db: DB):
        version = content.manifest(course_id)["version"]
        identity = optional_identity(request, db)

        def public_question(question: dict):
            preferred_variant_id = None
            if identity:
                previous = db.scalar(
                    select(Attempt)
                    .where(
                        Attempt.user_id == identity[0].id,
                        Attempt.course_id == course_id,
                        Attempt.content_version == version,
                        Attempt.question_id == question["id"],
                    )
                    .order_by(Attempt.created_at.desc(), Attempt.id.desc())
                    .limit(1)
                )
                if previous and isinstance(previous.response, dict):
                    saved_variant_id = previous.response.get("variant_id")
                    if isinstance(saved_variant_id, str):
                        preferred_variant_id = saved_variant_id
            token, variant_id, resolved = issue_variant_token(
                question,
                course_id,
                version,
                settings.variant_token_secret,
                preferred_variant_id=preferred_variant_id,
            )
            return content.public_question(resolved, variant_id, token)

        return content.lesson(course_id, lesson_id, public_question)

    @app.post("/api/v1/enrollments", status_code=201)
    def enroll(body: EnrollmentRequest, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        manifest = content.manifest(body.course_id)
        if manifest["maturity"] in {"catalog-only", "outlined"} and not manifest["modules"]:
            raise HTTPException(409, "This course has no authored lessons yet")
        existing = db.scalar(select(Enrollment).where(
            Enrollment.user_id == identity[0].id, Enrollment.course_id == body.course_id
        ))
        if not existing:
            existing = Enrollment(user_id=identity[0].id, course_id=body.course_id,
                                  content_version=manifest["version"])
            db.add(existing)
            db.flush()
        if existing.content_version == manifest["version"]:
            ensure_assessment_plan(db, existing, manifest)
        db.commit()
        return {"course_id": existing.course_id, "content_version": existing.content_version,
                "created_at": timestamp(existing.created_at)}

    @app.put("/api/v1/enrollments/{course_id}/version")
    def upgrade_enrollment(course_id: str, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        manifest = content.manifest(course_id)
        enrollment = db.scalar(select(Enrollment).where(
            Enrollment.user_id == identity[0].id, Enrollment.course_id == course_id
        ))
        if not enrollment:
            raise HTTPException(403, "Enroll in this course before updating its version")
        # This explicit operation preserves every prior attempt and its original version.
        enrollment.content_version = manifest["version"]
        ensure_assessment_plan(db, enrollment, manifest)
        db.commit()
        return {"course_id": enrollment.course_id, "content_version": enrollment.content_version,
                "created_at": timestamp(enrollment.created_at)}

    @app.get("/api/v1/enrollments")
    def enrollments(request: Request, db: DB):
        user, _ = require_identity(request, db)
        return [{"course_id": item.course_id, "content_version": item.content_version,
                 "created_at": timestamp(item.created_at)}
                for item in db.scalars(select(Enrollment).where(Enrollment.user_id == user.id))]

    @app.get("/api/v1/assessments/{course_id}", response_model=AssessmentPlanResponse)
    def assessment_plan(course_id: str, request: Request, db: DB):
        user, _ = require_identity(request, db)
        enrollment = enrolled(db, user, course_id)
        manifest = content.manifest(course_id)
        plan = ensure_assessment_plan(db, enrollment, manifest)
        db.commit()
        policy = plan.policy_json
        instances = list(db.scalars(
            select(AssessmentInstance).where(AssessmentInstance.plan_id == plan.id)
            .order_by(AssessmentInstance.week, AssessmentInstance.assessment_id)
        ))
        submission_count = db.scalar(select(func.count()).select_from(GradedSubmission).where(
            GradedSubmission.enrollment_id == enrollment.id,
            GradedSubmission.plan_id == plan.id,
        )) or 0
        current = now()
        visible_assessments = []
        for item in instances:
            if item.mode != "graded":
                schedule_status = "practice"
            elif item.release_at and current < item.release_at:
                schedule_status = "upcoming"
            elif item.due_at and current > item.due_at:
                schedule_status = "closed"
            else:
                schedule_status = "open"
            visible_assessments.append({
                "id": item.assessment_id,
                "title": item.title or item.assessment_id.replace("-", " ").title(),
                "type": item.assessment_type,
                "mode": item.mode,
                "category_id": item.category_id,
                "week": item.week,
                "points": item.points,
                "item_count": len(item.question_ids),
                "objective_count": len(item.objective_ids),
                "release_at": timestamp(item.release_at) if item.release_at else None,
                "due_at": timestamp(item.due_at) if item.due_at else None,
                "attempt_limit": item.attempt_limit,
                "attempt_scoring": item.attempt_scoring,
                "schedule_status": schedule_status,
            })
        return {
            "course_id": course_id,
            "content_version": plan.content_version,
            "grading_mode": plan.grading_mode,
            "course_grade_status": (
                ("configured_with_submissions" if submission_count else "configured_no_submissions")
                if plan.grading_mode == "graded-course" else "not_configured"
            ),
            "categories": policy["categories"],
            "category_aggregation": policy.get("category_aggregation", "points"),
            "attempt_policy": policy["attempt_policy"],
            "solution_release": policy["solution_release"],
            "late_policy": policy["late_policy"],
            "appeals": policy["appeals"],
            "assessments": visible_assessments,
        }

    @app.get(
        "/api/v1/assessments/{course_id}/{assessment_id}/questions",
        response_model=AssessmentQuestionsResponse,
    )
    def graded_assessment_questions(course_id: str, assessment_id: str, request: Request, db: DB):
        user, _ = require_identity(request, db)
        enrollment = enrolled(db, user, course_id)
        manifest = content.manifest(course_id)
        _, instance, questions, attempts_used, _ = graded_assessment(
            db, enrollment, manifest, assessment_id,
        )
        current = now()
        if instance.release_at and current < instance.release_at:
            raise HTTPException(409, "This assessment has not been released")
        status = "closed" if instance.due_at and current > instance.due_at else "open"
        db.commit()
        return {
            "course_id": course_id,
            "assessment_id": instance.assessment_id,
            "title": instance.title or instance.assessment_id.replace("-", " ").title(),
            "content_version": enrollment.content_version,
            "points": float(instance.points),
            "questions": [
                content.public_question(question)
                .model_copy(update={"assessment_role": "graded"})
                .model_dump()
                for question in questions
            ],
            "attempts_used": attempts_used,
            "attempt_limit": instance.attempt_limit,
            "schedule_status": status,
        }

    @app.get(
        "/api/v1/assessments/{course_id}/{assessment_id}/practice-questions",
        response_model=PracticeAssessmentResponse,
    )
    def practice_assessment_questions(
        course_id: str, assessment_id: str, request: Request, db: DB,
    ):
        """Serve only enrollment-pinned, explicitly public formative questions."""
        user, _ = require_identity(request, db)
        enrollment = enrolled(db, user, course_id)
        manifest = content.manifest(course_id)
        plan = ensure_assessment_plan(db, enrollment, manifest)
        instance = db.scalar(select(AssessmentInstance).where(
            AssessmentInstance.plan_id == plan.id,
            AssessmentInstance.assessment_id == assessment_id,
        ))
        if (
            not instance
            or instance.mode != "practice"
            or instance.assessment_type != "practice"
            or instance.source_path != "question-banks/practice.json"
            or instance.points <= 0
            or not instance.question_ids
        ):
            raise HTTPException(404, "Public practice assessment not found")
        try:
            source_path = content.assessment_source_file(enrollment.course_id, instance.source_path)
            source_bytes = source_path.read_bytes()
        except (ContentInvalid, ContentMissing, OSError) as exc:
            raise HTTPException(409, "The pinned practice source is unavailable") from exc
        source_sha256 = hashlib.sha256(source_bytes).hexdigest()
        if not secrets.compare_digest(source_sha256, instance.source_sha256):
            raise HTTPException(409, "Practice content changed after this enrollment version was pinned")
        try:
            package = json.loads(source_bytes.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise HTTPException(409, "The pinned practice source is invalid") from exc
        if (
            not isinstance(package, dict)
            or package.get("course_id") != enrollment.course_id
            or not isinstance(package.get("questions"), list)
        ):
            raise HTTPException(409, "The pinned practice source has an invalid course mapping")
        questions_by_id = {}
        for question in package["questions"]:
            question_id = question.get("id") if isinstance(question, dict) else None
            if not isinstance(question_id, str) or question_id in questions_by_id:
                raise HTTPException(409, "The pinned practice bank has invalid question identifiers")
            questions_by_id[question_id] = question
        question_ids = instance.question_ids
        if (
            not isinstance(question_ids, list)
            or any(not isinstance(question_id, str) for question_id in question_ids)
            or len(question_ids) != len(set(question_ids))
            or any(
                question_id not in questions_by_id
                or questions_by_id[question_id].get("visibility") != "public-practice-authoring"
                for question_id in question_ids
            )
        ):
            raise HTTPException(409, "The practice assessment must reference only explicit public practice items")
        questions = [questions_by_id[question_id] for question_id in question_ids]
        try:
            question_points = sum(float(question["points"]) for question in questions)
        except (KeyError, TypeError, ValueError) as exc:
            raise HTTPException(409, "The pinned practice point mapping is invalid") from exc
        if not math.isclose(question_points, float(instance.points), rel_tol=0, abs_tol=1e-8):
            raise HTTPException(409, "Question points do not match the pinned practice total")
        public_questions = []
        for question in questions:
            try:
                token, variant_id, resolved = issue_variant_token(
                    question, course_id, enrollment.content_version, settings.variant_token_secret,
                )
            except VariantTokenError as exc:
                raise HTTPException(409, "The pinned practice variant configuration is invalid") from exc
            public_questions.append(content.public_question(resolved, variant_id, token).model_dump())
        db.commit()
        return {
            "course_id": course_id,
            "assessment_id": instance.assessment_id,
            "title": instance.title or instance.assessment_id.replace("-", " ").title(),
            "content_version": enrollment.content_version,
            "points": float(instance.points),
            "questions": public_questions,
        }

    @app.post(
        "/api/v1/assessments/{course_id}/{assessment_id}/submissions",
        status_code=201,
        response_model=AssessmentSubmissionResponse,
    )
    def submit_graded_assessment(
        course_id: str, assessment_id: str, body: AssessmentSubmissionRequest, request: Request, db: DB,
    ):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        enrollment = enrolled(db, identity[0], course_id)
        manifest = content.manifest(course_id)
        plan, instance, questions, attempts_used, spec_digest = graded_assessment(
            db, enrollment, manifest, assessment_id,
        )
        current = now()
        if instance.release_at and current < instance.release_at:
            raise HTTPException(409, "This assessment has not been released")
        if instance.due_at and current > instance.due_at:
            raise HTTPException(409, "The submission deadline has passed")
        if instance.attempt_limit is not None and attempts_used >= instance.attempt_limit:
            raise HTTPException(409, "The attempt limit has been reached")
        expected_ids = {question["id"] for question in questions}
        if set(body.responses) != expected_ids:
            raise HTTPException(422, "Submit exactly one response for every question in this assessment")

        item_results = []
        normalized_responses = {}
        earned = 0.0
        try:
            for question in questions:
                question_id = question["id"]
                answer = body.responses[question_id]
                result = grade(question, answer)
                earned += result.score
                normalized_responses[question_id] = answer.model_dump(exclude_none=True)
                item_results.append({
                    "question_id": question_id,
                    "score": result.score,
                    "max_score": result.max_score,
                    "feedback": result.feedback.model_dump(),
                })
        except (GradingUnavailable, ArithmeticError, KeyError, TypeError, ValueError) as exc:
            raise HTTPException(409, "This assessment contains an unsupported or invalid grading specification") from exc

        maximum = float(instance.points)
        if not math.isclose(sum(result["max_score"] for result in item_results), maximum, rel_tol=0, abs_tol=1e-8):
            raise HTTPException(409, "The assessment grading total does not match its pinned points")
        row = GradedSubmission(
            enrollment_id=enrollment.id,
            plan_id=plan.id,
            assessment_instance_id=instance.id,
            content_version=enrollment.content_version,
            attempt_number=attempts_used + 1,
            source_sha256=instance.source_sha256,
            question_spec_sha256=spec_digest,
            responses_json=normalized_responses,
            results_json=item_results,
            score=earned,
            max_score=maximum,
            submitted_at=current,
        )
        db.add(row)
        try:
            db.commit()
        except IntegrityError as exc:
            db.rollback()
            raise HTTPException(409, "A concurrent submission changed the attempt count; reload this assessment") from exc
        db.refresh(row)
        return graded_submission_view(row, instance, course_id, db)

    @app.get(
        "/api/v1/assessments/{course_id}/submissions",
        response_model=list[AssessmentSubmissionResponse],
    )
    def graded_submission_history(course_id: str, request: Request, db: DB):
        user, _ = require_identity(request, db)
        enrollment = enrolled(db, user, course_id)
        plan = db.scalar(select(AssessmentPlan).where(
            AssessmentPlan.enrollment_id == enrollment.id,
            AssessmentPlan.content_version == enrollment.content_version,
        ))
        if not plan:
            return []
        rows = list(db.scalars(
            select(GradedSubmission)
            .where(
                GradedSubmission.enrollment_id == enrollment.id,
                GradedSubmission.plan_id == plan.id,
            )
            .order_by(GradedSubmission.submitted_at, GradedSubmission.id)
        ))
        by_instance = {
            item.id: item
            for item in db.scalars(select(AssessmentInstance).where(AssessmentInstance.plan_id == plan.id))
        }
        return [
            graded_submission_view(row, by_instance[row.assessment_instance_id], course_id, db)
            for row in rows if row.assessment_instance_id in by_instance
        ]

    @app.post("/api/v1/graded-submissions/{submission_id}/appeals", status_code=201)
    def create_graded_submission_appeal(
        submission_id: str, body: AppealRequest, request: Request, db: DB,
    ):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        user = identity[0]
        submission = db.scalar(
            select(GradedSubmission)
            .join(Enrollment, Enrollment.id == GradedSubmission.enrollment_id)
            .where(GradedSubmission.id == submission_id, Enrollment.user_id == user.id)
        )
        if not submission:
            raise HTTPException(404, "Graded submission not found")
        if db.scalar(select(GradedSubmissionAppeal).where(
            GradedSubmissionAppeal.submission_id == submission.id
        )):
            raise HTTPException(409, "This submission already has a human-review request")
        appeal = GradedSubmissionAppeal(
            submission_id=submission.id,
            user_id=user.id,
            reason=body.reason,
        )
        db.add(appeal)
        try:
            db.commit()
        except IntegrityError as exc:
            db.rollback()
            raise HTTPException(409, "This submission already has a human-review request") from exc
        instance = db.get(AssessmentInstance, submission.assessment_instance_id)
        if not instance:
            raise HTTPException(409, "The assessment snapshot for this submission is unavailable")
        db.refresh(appeal)
        return graded_submission_appeal_view(
            appeal, submission, instance, db.get(Enrollment, submission.enrollment_id).course_id
        )

    @app.get("/api/v1/graded-appeals", response_model=list[GradedSubmissionAppealResponse])
    def learner_graded_submission_appeals(request: Request, db: DB):
        user, _ = require_identity(request, db)
        appeals = db.scalars(
            select(GradedSubmissionAppeal)
            .where(GradedSubmissionAppeal.user_id == user.id)
            .order_by(GradedSubmissionAppeal.created_at, GradedSubmissionAppeal.id)
        )
        records = []
        for appeal in appeals:
            submission = db.get(GradedSubmission, appeal.submission_id)
            instance = db.get(AssessmentInstance, submission.assessment_instance_id) if submission else None
            enrollment = db.get(Enrollment, submission.enrollment_id) if submission else None
            review = db.scalar(select(GradedSubmissionAppealReview).where(
                GradedSubmissionAppealReview.appeal_id == appeal.id
            ))
            if submission and instance and enrollment:
                records.append(graded_submission_appeal_view(
                    appeal, submission, instance, enrollment.course_id, review,
                ))
        return records

    @app.get(
        "/api/v1/instructor/graded-appeals",
        response_model=list[InstructorGradedSubmissionAppealResponse],
    )
    def instructor_graded_submission_appeals(
        request: Request,
        db: DB,
        status: str = "open",
        limit: int = Query(default=50, ge=1, le=100),
    ):
        reviewer = require_reviewer(request, db)
        if status not in {"open", "reviewed", "all"}:
            raise HTTPException(422, "Status must be open, reviewed, or all")
        review_exists = select(GradedSubmissionAppealReview.id).where(
            GradedSubmissionAppealReview.appeal_id == GradedSubmissionAppeal.id
        ).exists()
        statement = select(GradedSubmissionAppeal).where(
            GradedSubmissionAppeal.user_id != reviewer.id
        ).order_by(GradedSubmissionAppeal.created_at, GradedSubmissionAppeal.id)
        if status == "open":
            statement = statement.where(~review_exists)
        elif status == "reviewed":
            statement = statement.where(review_exists)
        appeals = db.scalars(statement.limit(limit))
        records = []
        for appeal in appeals:
            submission = db.get(GradedSubmission, appeal.submission_id)
            if submission:
                records.append(graded_instructor_appeal_record(appeal, submission, db))
        return records

    @app.post("/api/v1/instructor/graded-appeals/{appeal_id}/review")
    def review_graded_submission_appeal(
        appeal_id: str, body: AppealReviewRequest, request: Request, db: DB,
    ):
        reviewer = require_reviewer(request, db, mutation=True)
        appeal = db.get(GradedSubmissionAppeal, appeal_id)
        if not appeal:
            raise HTTPException(404, "Graded submission appeal not found")
        if appeal.user_id == reviewer.id:
            raise HTTPException(403, "An instructor cannot review their own submission")
        if db.scalar(select(GradedSubmissionAppealReview).where(
            GradedSubmissionAppealReview.appeal_id == appeal.id
        )):
            raise HTTPException(409, "This appeal already has a recorded review")
        submission = db.get(GradedSubmission, appeal.submission_id)
        if not submission:
            raise HTTPException(404, "Graded submission not found")
        instance = db.get(AssessmentInstance, submission.assessment_instance_id)
        enrollment = db.get(Enrollment, submission.enrollment_id)
        plan = db.get(AssessmentPlan, submission.plan_id)
        if not instance or not enrollment or not plan:
            raise HTTPException(409, "The original assessment snapshot is unavailable")
        if body.decision == "adjusted":
            if body.override_score is None or body.override_score > submission.max_score:
                raise HTTPException(422, "An adjusted decision needs a score from zero through the submission maximum")
        elif body.override_score is not None:
            raise HTTPException(422, "Only an adjusted decision can change the score")
        if body.decision != "declined" and verified_graded_review_questions(
            submission, enrollment, plan, instance,
        ) is None:
            raise HTTPException(
                409,
                "The original assignment specification cannot be verified; only a decline explaining this limitation can be recorded",
            )
        review = GradedSubmissionAppealReview(
            appeal_id=appeal.id,
            reviewer_user_id=reviewer.id,
            reviewer_email=reviewer.email,
            decision=body.decision,
            review_note=body.review_note,
            override_score=body.override_score,
        )
        db.add(review)
        try:
            db.commit()
        except IntegrityError as exc:
            db.rollback()
            raise HTTPException(409, "This appeal already has a recorded review") from exc
        db.refresh(review)
        return graded_instructor_appeal_record(appeal, submission, db)

    @app.patch("/api/v1/progress/{course_id}/{lesson_id}")
    def save_progress(course_id: str, lesson_id: str, body: ProgressRequest, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        enrolled(db, identity[0], course_id)
        content.lesson_record(course_id, lesson_id)
        record = db.scalar(select(Progress).where(Progress.user_id == identity[0].id,
                           Progress.course_id == course_id, Progress.lesson_id == lesson_id))
        if not record:
            record = Progress(user_id=identity[0].id, course_id=course_id, lesson_id=lesson_id)
            db.add(record)
        record.completed, record.updated_at = body.completed, now()
        db.commit()
        return {"lesson_id": lesson_id, "completed": record.completed, "evidence": "learner-marked"}

    @app.get("/api/v1/progress/{course_id}")
    def progress(course_id: str, request: Request, db: DB):
        user, _ = require_identity(request, db)
        enrolled(db, user, course_id)
        return [{"lesson_id": item.lesson_id, "completed": item.completed, "updated_at": timestamp(item.updated_at),
                 "evidence": "learner-marked"}
                for item in db.scalars(select(Progress).where(Progress.user_id == user.id,
                                       Progress.course_id == course_id))]

    @app.put("/api/v1/notes/{course_id}/{lesson_id}")
    def save_note(course_id: str, lesson_id: str, body: NoteRequest, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        enrolled(db, identity[0], course_id)
        content.lesson_record(course_id, lesson_id)
        note = db.scalar(select(Note).where(Note.user_id == identity[0].id, Note.course_id == course_id,
                                           Note.lesson_id == lesson_id))
        if not note:
            note = Note(user_id=identity[0].id, course_id=course_id, lesson_id=lesson_id)
            db.add(note)
        # Plain text storage: frontend must render as text, never unsanitized HTML.
        note.body, note.updated_at = body.body, now()
        db.commit()
        return {"lesson_id": lesson_id, "body": note.body, "updated_at": timestamp(note.updated_at)}

    @app.get("/api/v1/notes/{course_id}")
    def notes(course_id: str, request: Request, db: DB):
        user, _ = require_identity(request, db)
        enrolled(db, user, course_id)
        return [{"lesson_id": item.lesson_id, "body": item.body, "updated_at": timestamp(item.updated_at)}
                for item in db.scalars(select(Note).where(Note.user_id == user.id, Note.course_id == course_id))]

    @app.put("/api/v1/bookmarks/{course_id}")
    def save_bookmark(course_id: str, body: BookmarkRequest, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        content.manifest(course_id)
        bookmark = db.scalar(select(Bookmark).where(Bookmark.user_id == identity[0].id,
                                                  Bookmark.course_id == course_id))
        if body.saved and not bookmark:
            db.add(Bookmark(user_id=identity[0].id, course_id=course_id))
        elif not body.saved and bookmark:
            db.delete(bookmark)
        db.commit()
        return {"course_id": course_id, "saved": body.saved}

    @app.get("/api/v1/bookmarks")
    def bookmarks(request: Request, db: DB):
        user, _ = require_identity(request, db)
        return [item.course_id for item in db.scalars(select(Bookmark).where(Bookmark.user_id == user.id))]

    def attempt_view(item: Attempt, db: Session) -> dict:
        appeal = db.scalar(select(Appeal).where(Appeal.attempt_id == item.id))
        review = (
            db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id))
            if appeal else None
        )
        effective_score = (
            float(review.override_score)
            if review and review.decision == "adjusted"
            else float(item.score)
        )
        return {
            "id": item.id, "course_id": item.course_id, "question_id": item.question_id,
            "content_version": item.content_version, "response": item.response,
            "score": float(item.score), "effective_score": effective_score,
            "max_score": float(item.max_score), "result": item.result,
            "objective_ids": item.objective_ids, "created_at": timestamp(item.created_at),
            "appeal": appeal_view(appeal, item, review) if appeal else None,
        }

    @app.post("/api/v1/courses/{course_id}/questions/{question_id}/attempts", status_code=201)
    def submit(course_id: str, question_id: str, body: AttemptRequest, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        enrollment = enrolled(db, identity[0], course_id)
        question = content.question(course_id, question_id)
        try:
            resolved_question, variant_id = verify_variant_token(
                question, course_id, enrollment.content_version, body.variant_token,
                settings.variant_token_secret,
            )
        except VariantTokenError as exc:
            raise HTTPException(422, "Question variant token is invalid or expired") from exc
        result = grade(resolved_question, body)
        stored_response = {"response": body.response}
        if body.unit is not None:
            stored_response["unit"] = body.unit
        if variant_id is not None:
            stored_response["variant_id"] = variant_id
        item = Attempt(user_id=identity[0].id, course_id=course_id, question_id=question_id,
                       content_version=enrollment.content_version, response=stored_response,
                       grading_policy_version=result.grading_policy_version,
                       question_spec_sha256=question_spec_digest(resolved_question, variant_id),
                       score=result.score, max_score=result.max_score, result=result.model_dump(),
                       objective_ids=resolved_question.get("objective_ids", []))
        db.add(item)
        db.commit()
        return attempt_view(item, db)

    @app.post("/api/v1/attempts/{attempt_id}/appeals", status_code=201)
    def create_appeal(attempt_id: str, body: AppealRequest, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        attempt = db.scalar(select(Attempt).where(
            Attempt.id == attempt_id, Attempt.user_id == identity[0].id
        ))
        if not attempt:
            raise HTTPException(404, "Attempt not found")
        if db.scalar(select(Appeal).where(Appeal.attempt_id == attempt.id)):
            raise HTTPException(409, "This attempt already has a human-review request")
        appeal = Appeal(attempt_id=attempt.id, user_id=identity[0].id, reason=body.reason)
        db.add(appeal)
        db.commit()
        return appeal_view(appeal, attempt)

    @app.get("/api/v1/appeals")
    def learner_appeals(request: Request, db: DB):
        user, _ = require_identity(request, db)
        appeals = db.scalars(
            select(Appeal).where(Appeal.user_id == user.id).order_by(Appeal.created_at, Appeal.id)
        )
        result = []
        for appeal in appeals:
            attempt = db.get(Attempt, appeal.attempt_id)
            review = db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id))
            if attempt:
                result.append(appeal_view(appeal, attempt, review))
        return result

    def verified_review_question(attempt: Attempt) -> dict | None:
        """Resolve the submitted variant and require its saved spec digest to match."""
        if not attempt.question_spec_sha256 or not isinstance(attempt.response, dict):
            return None
        try:
            manifest = content.manifest(attempt.course_id)
            if manifest["version"] != attempt.content_version:
                return None
            question = content.question(attempt.course_id, attempt.question_id)
            variant_id = attempt.response.get("variant_id")
            resolved = resolve_variant(question, variant_id)
            digest = question_spec_digest(resolved, variant_id)
            return resolved if digest == attempt.question_spec_sha256 else None
        except (ContentMissing, ContentInvalid, VariantTokenError, KeyError, TypeError, ValueError):
            return None

    def instructor_appeal_record(appeal: Appeal, attempt: Attempt, db: Session) -> dict:
        learner = db.get(User, appeal.user_id)
        review = db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id))
        question = verified_review_question(attempt)
        content_is_current = question is not None
        review_question = (
            content.public_question(
                question,
                variant_id=attempt.response.get("variant_id"),
            ).model_dump()
            if question is not None
            else None
        )
        return {
            **appeal_view(appeal, attempt, review),
            "learner": learner.email if learner and learner.email else "Guest account",
            "content_is_current": content_is_current,
            "review_question": review_question,
            "question_prompt": question.get("prompt") if question else None,
            "question_options": question.get("options") if question else None,
            "response": attempt.response,
            "automatic_feedback": attempt.result,
            "specification_pinned": bool(attempt.question_spec_sha256),
        }

    @app.get("/api/v1/instructor/appeals")
    def instructor_appeals(
        request: Request, db: DB,
        status: str = "open",
        limit: int = Query(default=50, ge=1, le=100),
    ):
        reviewer = require_reviewer(request, db)
        if status not in {"open", "reviewed", "all"}:
            raise HTTPException(422, "Status must be open, reviewed, or all")
        statement = select(Appeal).where(Appeal.user_id != reviewer.id).order_by(Appeal.created_at, Appeal.id)
        if status == "open":
            statement = statement.where(~select(AppealReview.id).where(
                AppealReview.appeal_id == Appeal.id
            ).exists())
        elif status == "reviewed":
            statement = statement.where(select(AppealReview.id).where(
                AppealReview.appeal_id == Appeal.id
            ).exists())
        appeals = db.scalars(statement.limit(limit))
        result = []
        for appeal in appeals:
            attempt = db.get(Attempt, appeal.attempt_id)
            if attempt:
                result.append(instructor_appeal_record(appeal, attempt, db))
        return result

    @app.post("/api/v1/instructor/appeals/{appeal_id}/review")
    def review_appeal(
        appeal_id: str, body: AppealReviewRequest, request: Request, db: DB
    ):
        reviewer = require_reviewer(request, db, mutation=True)
        appeal = db.get(Appeal, appeal_id)
        if not appeal:
            raise HTTPException(404, "Appeal not found")
        if appeal.user_id == reviewer.id:
            raise HTTPException(403, "An instructor cannot review their own attempt")
        if db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id)):
            raise HTTPException(409, "This appeal already has a recorded review")
        attempt = db.get(Attempt, appeal.attempt_id)
        if not attempt:
            raise HTTPException(404, "Attempt not found")
        if body.decision == "adjusted":
            if body.override_score is None or body.override_score > attempt.max_score:
                raise HTTPException(422, "An adjusted decision needs a score from zero through the attempt maximum")
        elif body.override_score is not None:
            raise HTTPException(422, "Only an adjusted decision can change the score")
        if body.decision != "declined" and verified_review_question(attempt) is None:
            raise HTTPException(
                409,
                "The original question specification cannot be verified; only a decline explaining this limitation can be recorded",
            )
        review = AppealReview(
            appeal_id=appeal.id,
            reviewer_user_id=reviewer.id,
            reviewer_email=reviewer.email,
            decision=body.decision,
            review_note=body.review_note,
            override_score=body.override_score,
        )
        db.add(review)
        db.commit()
        return instructor_appeal_record(appeal, attempt, db)

    @app.get("/api/v1/attempts")
    def attempts(request: Request, db: DB, course_id: str | None = None):
        user, _ = require_identity(request, db)
        query = select(Attempt).where(Attempt.user_id == user.id).order_by(Attempt.created_at, Attempt.id)
        if course_id:
            query = query.where(Attempt.course_id == course_id)
        return [attempt_view(item, db) for item in db.scalars(query)]

    @app.get("/api/v1/gradebook/{course_id}", response_model=GradebookResponse)
    def gradebook(course_id: str, request: Request, db: DB):
        user, _ = require_identity(request, db)
        enrollment = enrolled(db, user, course_id)
        questions = content.questions(course_id)
        rows = list(
            db.scalars(
                select(Attempt)
                .where(
                    Attempt.user_id == user.id,
                    Attempt.course_id == course_id,
                    Attempt.content_version == enrollment.content_version,
                )
                .order_by(Attempt.created_at, Attempt.id)
            )
        )
        best = {}
        score_overrides = {}
        reviewed = db.execute(
            select(Appeal.attempt_id, AppealReview.override_score)
            .join(AppealReview, AppealReview.appeal_id == Appeal.id)
            .join(Attempt, Attempt.id == Appeal.attempt_id)
            .where(
                Attempt.user_id == user.id,
                Attempt.course_id == course_id,
                Attempt.content_version == enrollment.content_version,
                AppealReview.decision == "adjusted",
            )
        )
        score_overrides = {attempt_id: float(score) for attempt_id, score in reviewed}
        for item in rows:
            effective_score = score_overrides.get(item.id, float(item.score))
            best[item.question_id] = max(best.get(item.question_id, 0), effective_score)
        course_grade = None
        plan = db.scalar(select(AssessmentPlan).where(
            AssessmentPlan.enrollment_id == enrollment.id,
            AssessmentPlan.content_version == enrollment.content_version,
        ))
        if plan and plan.grading_mode == "graded-course":
            instances = list(db.scalars(select(AssessmentInstance).where(AssessmentInstance.plan_id == plan.id)))
            submissions = list(db.scalars(select(GradedSubmission).where(
                GradedSubmission.enrollment_id == enrollment.id,
                GradedSubmission.plan_id == plan.id,
            )))
            graded_submission_ids = [item.id for item in submissions]
            graded_score_overrides = {}
            if graded_submission_ids:
                override_rows = db.execute(
                    select(GradedSubmissionAppeal.submission_id, GradedSubmissionAppealReview.override_score)
                    .join(
                        GradedSubmissionAppealReview,
                        GradedSubmissionAppealReview.appeal_id == GradedSubmissionAppeal.id,
                    )
                    .where(
                        GradedSubmissionAppeal.submission_id.in_(graded_submission_ids),
                        GradedSubmissionAppealReview.decision == "adjusted",
                    )
                )
                graded_score_overrides = {
                    submission_id: float(score) for submission_id, score in override_rows
                }
            attempts_by_assessment = defaultdict(list)
            for submission in submissions:
                instance = next((item for item in instances if item.id == submission.assessment_instance_id), None)
                if instance:
                    attempts_by_assessment[instance.assessment_id].append({
                        "id": submission.id,
                        "score": graded_score_overrides.get(submission.id, submission.score),
                        "max_score": submission.max_score,
                        "submitted_at": timestamp(submission.submitted_at),
                    })
            try:
                calculated = calculate_weighted_grade(
                    [
                        {
                            "id": item.assessment_id,
                            "mode": item.mode,
                            "category_id": item.category_id,
                            "points": item.points,
                            "release_at": timestamp(item.release_at) if item.release_at else None,
                            "due_at": timestamp(item.due_at) if item.due_at else None,
                            "attempt_limit": item.attempt_limit,
                            "attempt_scoring": item.attempt_scoring,
                        }
                        for item in instances
                    ],
                    plan.policy_json,
                    dict(attempts_by_assessment),
                    now(),
                )
            except (KeyError, TypeError, ValueError) as exc:
                raise HTTPException(409, "Saved assessment results do not match the pinned grade policy") from exc
            course_grade = {
                **calculated,
                "manual_override_count": len(graded_score_overrides),
                "status": "in_progress" if submissions else "configured_no_submissions",
                "explanation": (
                    "This percentage follows the saved assessment weights, deterministic attempt rules, and any "
                    "recorded instructor adjustments. The original automatic score for every submission remains saved. "
                    "Only released work enters the current calculation; the active category weight shows "
                    "how much of the configured grade currently has evidence. It does not establish credit, "
                    "course equivalency, or completion."
                ),
            }
        return {"course_id": course_id, "assessment_role": "formative", "aggregation": "best reviewed practice result per question",
                "score": sum(best.values()), "max_score": sum(float(item.get("points", 1)) for item in questions),
                "attempt_count": len(rows),
                "manual_override_count": len(score_overrides),
                "course_grade": course_grade,
                "objective_evidence_policy": {"version": POLICY_VERSION,
                    "minimum_distinct_items": MIN_DISTINCT_ITEMS,
                    "minimum_item_coverage": MIN_ITEM_COVERAGE,
                    "minimum_performance": MIN_PERFORMANCE},
                "objective_evidence": objective_evidence(questions, rows, score_overrides),
                "limitations": "The provisional practice indicator requires at least 3 distinct tagged items, 80% of available tagged-item coverage, and 80% best points on attempted items. Instructor adjustments are audited separately from automatic scores. This remains a study signal from short formative checks; it does not establish reasoning, transfer, course mastery, credit, or course completion."}

    @app.get("/api/v1/learner/export")
    def export(request: Request, db: DB):
        user, _ = require_identity(request, db)
        user_enrollments = list(db.scalars(select(Enrollment).where(Enrollment.user_id == user.id)))
        enrollment_by_id = {item.id: item for item in user_enrollments}
        graded_rows = list(db.scalars(select(GradedSubmission).where(
            GradedSubmission.enrollment_id.in_(list(enrollment_by_id)) if enrollment_by_id else False
        )))
        return {"schema_version": "1.0", "exported_at": timestamp(now()), "user": user_view(user),
                "enrollments": [{"course_id": item.course_id, "content_version": item.content_version}
                                for item in user_enrollments],
                "attempts": [attempt_view(item, db) for item in db.scalars(select(Attempt).where(Attempt.user_id == user.id))],
                "graded_submissions": [
                    graded_submission_view(
                        item, db.get(AssessmentInstance, item.assessment_instance_id),
                        enrollment_by_id[item.enrollment_id].course_id, db,
                    )
                    for item in graded_rows
                    if item.assessment_instance_id and item.enrollment_id in enrollment_by_id
                ],
                "appeals": [appeal_view(
                    appeal, db.get(Attempt, appeal.attempt_id),
                    db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id)),
                ) for appeal in db.scalars(select(Appeal).where(Appeal.user_id == user.id))
                    if db.get(Attempt, appeal.attempt_id)],
                "graded_submission_appeals": [
                    graded_submission_appeal_view(
                        appeal,
                        submission,
                        instance,
                        enrollment_by_id[submission.enrollment_id].course_id,
                        db.scalar(select(GradedSubmissionAppealReview).where(
                            GradedSubmissionAppealReview.appeal_id == appeal.id
                        )),
                    )
                    for appeal in db.scalars(select(GradedSubmissionAppeal).where(
                        GradedSubmissionAppeal.user_id == user.id
                    ))
                    if (submission := db.get(GradedSubmission, appeal.submission_id))
                    and (instance := db.get(AssessmentInstance, submission.assessment_instance_id))
                    and submission.enrollment_id in enrollment_by_id
                ],
                "progress": [{"course_id": item.course_id, "lesson_id": item.lesson_id, "completed": item.completed}
                             for item in db.scalars(select(Progress).where(Progress.user_id == user.id))],
                "notes": [{"course_id": item.course_id, "lesson_id": item.lesson_id, "body": item.body}
                          for item in db.scalars(select(Note).where(Note.user_id == user.id))],
                "bookmarks": [item.course_id for item in db.scalars(select(Bookmark).where(Bookmark.user_id == user.id))]}

    @app.delete("/api/v1/learner", status_code=204)
    def delete_learner(request: Request, response: Response, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        # Explicit child deletion also protects SQLite test deployments.
        appeal_ids = select(Appeal.id).where(Appeal.user_id == identity[0].id)
        db.execute(delete(AppealReview).where(AppealReview.appeal_id.in_(appeal_ids)))
        db.execute(delete(Appeal).where(Appeal.user_id == identity[0].id))
        graded_appeal_ids = select(GradedSubmissionAppeal.id).where(
            GradedSubmissionAppeal.user_id == identity[0].id
        )
        db.execute(delete(GradedSubmissionAppealReview).where(
            GradedSubmissionAppealReview.appeal_id.in_(graded_appeal_ids)
        ))
        db.execute(delete(GradedSubmissionAppeal).where(
            GradedSubmissionAppeal.user_id == identity[0].id
        ))
        enrollment_ids = select(Enrollment.id).where(Enrollment.user_id == identity[0].id)
        db.execute(delete(GradedSubmission).where(GradedSubmission.enrollment_id.in_(enrollment_ids)))
        db.execute(update(AppealReview).where(
            AppealReview.reviewer_user_id == identity[0].id
        ).values(reviewer_user_id=None, reviewer_email="deleted instructor account"))
        db.execute(update(GradedSubmissionAppealReview).where(
            GradedSubmissionAppealReview.reviewer_user_id == identity[0].id
        ).values(reviewer_user_id=None, reviewer_email="deleted instructor account"))
        for model in (SessionToken, Attempt, Bookmark, Note, Progress, Enrollment):
            db.execute(delete(model).where(model.user_id == identity[0].id))
        db.delete(identity[0])
        db.commit()
        response.delete_cookie(COOKIE, path="/api")

    return app


app = create_app()
