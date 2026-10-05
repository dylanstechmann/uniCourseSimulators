"""Configuration contains no checked-in database or provider credentials."""

import os
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
        return cls(
            database_url=database_url or "sqlite:///./courselab-development.db",
            content_root=Path(os.getenv("CONTENT_ROOT", "../content")).resolve(),
            allowed_origins=tuple(
                origin.strip() for origin in os.getenv(
                    "ALLOWED_ORIGINS", "http://localhost:8080,http://127.0.0.1:8080"
                ).split(",") if origin.strip()
            ),
            cookie_secure=os.getenv("COOKIE_SECURE", "true").lower() == "true",
        )
