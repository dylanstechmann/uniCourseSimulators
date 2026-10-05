from pathlib import Path

from sqlalchemy import inspect

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
        "alembic_version", "users", "sessions", "enrollments", "progress", "notes", "bookmarks", "attempts"
    }
    command.check(config)
    command.downgrade(config, "base")
    assert inspect(engine).get_table_names() == ["alembic_version"]
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
