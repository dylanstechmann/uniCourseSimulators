"""Configuration contains no checked-in database or provider credentials."""

import os
import secrets
from dataclasses import dataclass, field
from pathlib import Path

from sqlalchemy import URL


@dataclass(frozen=True)
class Settings:
    database_url: str = field(repr=False)
    content_root: Path
    allowed_origins: tuple[str, ...] = ("http://localhost:8080", "http://127.0.0.1:8080")
    cookie_secure: bool = True
    session_hours: int = 168
    guest_hours: int = 720
    body_limit: int = 65536
    rate_limit: int = 120
    auth_rate_limit: int = 30
    # Instructor access is disabled unless deployment operators explicitly
    # allowlist registered account emails. This is authorization metadata,
    # never a credential.
    instructor_emails: tuple[str, ...] = ()
    # An ephemeral default is sufficient for local development. Deployments can
    # set VARIANT_TOKEN_SECRET to keep active practice variants valid on restart.
    variant_token_secret: bytes = field(default_factory=lambda: secrets.token_bytes(32), repr=False)

    @classmethod
    def from_environment(cls) -> "Settings":
        database_url = os.getenv("DATABASE_URL")
        password_file = os.getenv("DATABASE_PASSWORD_FILE")
        if not database_url and password_file:
            password = Path(password_file).read_text(encoding="utf-8").strip()
            if not password:
                raise ValueError("Database password file is empty")
            database_url = URL.create(
                "postgresql+psycopg", username=os.getenv("DB_USER", "courselab"), password=password,
                host=os.getenv("DB_HOST", "db"), port=int(os.getenv("DB_PORT", "5432")),
                database=os.getenv("DB_NAME", "courselab"),
            ).render_as_string(hide_password=False)
        variant_secret = os.getenv("VARIANT_TOKEN_SECRET") or None
        if variant_secret is not None and len(variant_secret.encode("utf-8")) < 32:
            raise ValueError("VARIANT_TOKEN_SECRET must contain at least 32 bytes")
        return cls(
            database_url=database_url or "sqlite:///./courselab-development.db",
            content_root=Path(os.getenv("CONTENT_ROOT", "../content")).resolve(),
            allowed_origins=tuple(
                origin.strip() for origin in os.getenv(
                    "ALLOWED_ORIGINS", "http://localhost:8080,http://127.0.0.1:8080"
                ).split(",") if origin.strip()
            ),
            instructor_emails=tuple(
                email.strip().lower()
                for email in os.getenv("INSTRUCTOR_EMAILS", "").split(",")
                if email.strip()
            ),
            cookie_secure=os.getenv("COOKIE_SECURE", "true").lower() == "true",
            variant_token_secret=(
                variant_secret.encode("utf-8") if variant_secret is not None else secrets.token_bytes(32)
            ),
        )
