"""FastAPI learner service with server ownership and formative-only assessment."""

import hashlib
import secrets
import time
from collections import defaultdict, deque
from datetime import timedelta
from typing import Annotated

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .config import Settings
from .content import ContentInvalid, ContentMissing, ContentRepository
from .db import Attempt, Bookmark, Enrollment, Note, Progress, SessionToken, User, database, now
from .grading import GradingUnavailable, grade
from .schemas import (
    AttemptRequest,
    BookmarkRequest,
    CourseSummary,
    Credentials,
    EnrollmentRequest,
    NoteRequest,
    ProgressRequest,
    PublicCourse,
    PublicLesson,
)

COOKIE = "courselab_session"
PASSWORDS = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=2)


def token_hash(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def user_view(user: User) -> dict:
    return {"id": user.id, "email": user.email, "is_guest": user.is_guest}


def timestamp(value) -> str:
    """Expose naive database UTC as unambiguous ISO8601 UTC to browsers."""
    return value.isoformat(timespec="microseconds") + "Z"


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings.from_environment()
    app = FastAPI(title="Lattice CourseLab API", version="0.2.0", docs_url=None, redoc_url=None)
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
        return {"user": user_view(user), "csrf_token": csrf}

    @app.get("/api/v1/health")
    def health(db: DB):
        db.execute(select(1))
        return {"status": "ok", "programming_runner": "disabled", "llm_feedback": "disabled"}

    @app.get("/api/v1/auth/session")
    def session_info(request: Request, response: Response, db: DB):
        identity = optional_identity(request, db)
        if not identity:
            response.delete_cookie(COOKIE, path="/api")
            return {"user": None, "csrf_token": None}
        return {"user": user_view(identity[0]), "csrf_token": identity[1].csrf_token}

    @app.post("/api/v1/auth/guest")
    def guest(request: Request, response: Response, db: DB):
        identity = optional_identity(request, db)
        if identity:
            require_csrf(request, identity)
            return {"user": user_view(identity[0]), "csrf_token": identity[1].csrf_token}
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

    @app.get("/api/v1/sources")
    def sources():
        return content.sources()

    @app.get("/api/v1/courses/{course_id}", response_model=PublicCourse)
    def course(course_id: str):
        return content.course(course_id)

    @app.get("/api/v1/courses/{course_id}/lessons/{lesson_id}", response_model=PublicLesson)
    def lesson(course_id: str, lesson_id: str):
        return content.lesson(course_id, lesson_id)

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
            db.commit()
        return {"course_id": existing.course_id, "content_version": existing.content_version,
                "created_at": timestamp(existing.created_at)}

    @app.get("/api/v1/enrollments")
    def enrollments(request: Request, db: DB):
        user, _ = require_identity(request, db)
        return [{"course_id": item.course_id, "content_version": item.content_version,
                 "created_at": timestamp(item.created_at)}
                for item in db.scalars(select(Enrollment).where(Enrollment.user_id == user.id))]

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

    def attempt_view(item: Attempt) -> dict:
        return {"id": item.id, "course_id": item.course_id, "question_id": item.question_id,
                "content_version": item.content_version, "response": item.response,
                "score": item.score, "max_score": item.max_score, "result": item.result,
                "objective_ids": item.objective_ids, "created_at": timestamp(item.created_at)}

    @app.post("/api/v1/courses/{course_id}/questions/{question_id}/attempts", status_code=201)
    def submit(course_id: str, question_id: str, body: AttemptRequest, request: Request, db: DB):
        identity = require_identity(request, db)
        require_csrf(request, identity)
        enrollment = enrolled(db, identity[0], course_id)
        question = content.question(course_id, question_id)
        result = grade(question, body)
        item = Attempt(user_id=identity[0].id, course_id=course_id, question_id=question_id,
                       content_version=enrollment.content_version, response=body.model_dump(),
                       score=result.score, max_score=result.max_score, result=result.model_dump(),
                       objective_ids=question.get("objective_ids", []))
        db.add(item)
        db.commit()
        return attempt_view(item)

    @app.get("/api/v1/attempts")
    def attempts(request: Request, db: DB, course_id: str | None = None):
        user, _ = require_identity(request, db)
        query = select(Attempt).where(Attempt.user_id == user.id).order_by(Attempt.created_at, Attempt.id)
        if course_id:
            query = query.where(Attempt.course_id == course_id)
        return [attempt_view(item) for item in db.scalars(query)]

    @app.get("/api/v1/gradebook/{course_id}")
    def gradebook(course_id: str, request: Request, db: DB):
        user, _ = require_identity(request, db)
        enrolled(db, user, course_id)
        questions = content.questions(course_id)
        rows = list(db.scalars(select(Attempt).where(Attempt.user_id == user.id,
                              Attempt.course_id == course_id).order_by(Attempt.created_at, Attempt.id)))
        best, objectives = {}, defaultdict(lambda: {"attempts": 0, "correct_results": 0})
        for item in rows:
            best[item.question_id] = max(best.get(item.question_id, 0), item.score)
            for objective_id in item.objective_ids:
                objectives[objective_id]["attempts"] += 1
                objectives[objective_id]["correct_results"] += int(item.result["correct"])
        return {"course_id": course_id, "assessment_role": "formative", "aggregation": "best practice result per question",
                "score": sum(best.values()), "max_score": sum(float(item.get("points", 1)) for item in questions),
                "attempt_count": len(rows), "objective_evidence": dict(objectives),
                "limitations": "Correct results on short practice items do not establish reasoning, mastery, credit, or course completion."}

    @app.get("/api/v1/learner/export")
    def export(request: Request, db: DB):
        user, _ = require_identity(request, db)
        return {"schema_version": "1.0", "exported_at": timestamp(now()), "user": user_view(user),
                "enrollments": [{"course_id": item.course_id, "content_version": item.content_version}
                                for item in db.scalars(select(Enrollment).where(Enrollment.user_id == user.id))],
                "attempts": [attempt_view(item) for item in db.scalars(select(Attempt).where(Attempt.user_id == user.id))],
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
        for model in (SessionToken, Attempt, Bookmark, Note, Progress, Enrollment):
            db.execute(delete(model).where(model.user_id == identity[0].id))
        db.delete(identity[0])
        db.commit()
        response.delete_cookie(COOKIE, path="/api")

    return app


app = create_app()
