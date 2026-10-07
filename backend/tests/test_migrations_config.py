import json
from pathlib import Path

import pytest
from sqlalchemy import create_engine, inspect, text

from alembic import command
from alembic.config import Config
from courselab.config import Settings
from courselab.db import database


def test_alembic_upgrade_matches_metadata(tmp_path, monkeypatch):
    url = f"sqlite:///{tmp_path}/migrated.db"
    monkeypatch.setenv("DATABASE_URL", url)
    backend = Path(__file__).resolve().parents[1]
    config = Config(str(backend / "alembic.ini"))
    config.set_main_option("script_location", str(backend / "alembic"))
    command.upgrade(config, "head")
    engine, _ = database(url)
    assert set(inspect(engine).get_table_names()) == {
        "alembic_version", "users", "sessions", "enrollments", "progress", "notes", "bookmarks",
        "attempts", "appeals", "appeal_reviews", "assessment_plans", "assessment_instances",
        "graded_submissions", "graded_submission_appeals", "graded_submission_appeal_reviews",
    }
    command.check(config)
    command.downgrade(config, "base")
    assert inspect(engine).get_table_names() == ["alembic_version"]
    engine.dispose()


def test_digest_migration_preserves_unpinned_existing_attempts(tmp_path, monkeypatch):
    url = f"sqlite:///{tmp_path}/legacy-attempt.db"
    monkeypatch.setenv("DATABASE_URL", url)
    backend = Path(__file__).resolve().parents[1]
    config = Config(str(backend / "alembic.ini"))
    config.set_main_option("script_location", str(backend / "alembic"))
    command.upgrade(config, "0001")
    engine = create_engine(url)
    with engine.begin() as connection:
        connection.execute(text(
            "INSERT INTO users (id, email, password_hash, is_guest, created_at) "
            "VALUES ('u1', NULL, NULL, 1, '2026-10-05 00:00:00')"
        ))
        connection.execute(text(
            "INSERT INTO attempts (id, user_id, course_id, question_id, content_version, "
            "grading_policy_version, response, score, max_score, result, objective_ids, created_at) "
            "VALUES ('a1', 'u1', 'cell-biology', 'cell-biology-1:check', '0.1.0', "
            "'practice-v1', :response, 1, 1, :result, :objectives, '2026-10-05 00:00:00')"
        ), {
            "response": json.dumps({"response": 0}),
            "result": json.dumps({"score": 1}),
            "objectives": json.dumps(["outcome"]),
        })
    command.upgrade(config, "head")
    with engine.connect() as connection:
        old = connection.execute(text(
            "SELECT content_version, grading_policy_version, question_spec_sha256 "
            "FROM attempts WHERE id='a1'"
        )).one()
        instructor_role = connection.execute(text(
            "SELECT is_instructor FROM users WHERE id='u1'"
        )).scalar_one()
    assert old == ("0.1.0", "practice-v1", None)
    assert not instructor_role
    assert "question_spec_sha256" in {column["name"] for column in inspect(engine).get_columns("attempts")}
    command.downgrade(config, "base")
    engine.dispose()


def test_password_file_url_is_escaped_and_not_in_repr(tmp_path, monkeypatch):
    secret = tmp_path / "db-secret"
    secret.write_text("fixture:@/?#%value\n")
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("DATABASE_PASSWORD_FILE", str(secret))
    monkeypatch.setenv("DB_HOST", "db")
    settings = Settings.from_environment()
    from sqlalchemy.engine import make_url
    url = make_url(settings.database_url)
    assert url.password == "fixture:@/?#%value"
    assert url.drivername == "postgresql+psycopg" and url.host == "db"
    assert "fixture" not in repr(settings)


def test_database_url_wins_for_ci(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    monkeypatch.setenv("DATABASE_PASSWORD_FILE", "/not/read/when/url/provided")
    assert Settings.from_environment().database_url == "sqlite:///:memory:"


def test_variant_token_secret_is_private_and_has_a_minimum_length(monkeypatch):
    secret = "a" * 32
    monkeypatch.setenv("VARIANT_TOKEN_SECRET", secret)
    settings = Settings.from_environment()
    assert settings.variant_token_secret == secret.encode()
    assert secret not in repr(settings)
    monkeypatch.setenv("VARIANT_TOKEN_SECRET", "too-short")
    with pytest.raises(ValueError, match="at least 32 bytes"):
        Settings.from_environment()


def test_private_assessment_root_is_optional_and_resolved(tmp_path, monkeypatch):
    private_root = tmp_path / "protected" / "keys"
    monkeypatch.setenv("PRIVATE_ASSESSMENTS_ROOT", str(private_root))
    assert Settings.from_environment().private_assessments_root == private_root.resolve()
    monkeypatch.delenv("PRIVATE_ASSESSMENTS_ROOT")
    assert Settings.from_environment().private_assessments_root is None


def test_self_declared_email_environment_is_not_authorization(monkeypatch):
    monkeypatch.setenv("INSTRUCTOR_EMAILS", "reviewer@example.org")
    settings = Settings.from_environment()
    assert not hasattr(settings, "instructor_emails")
