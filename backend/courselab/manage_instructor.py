"""Provision or revoke an instructor role from an operator shell only.

There is deliberately no HTTP role-assignment endpoint. Verify the person's
identity and authority outside the application before granting this role.
"""

import argparse
import sys

from sqlalchemy.orm import sessionmaker

from .config import Settings
from .db import User, database


def set_instructor_role(session_factory: sessionmaker, user_id: str, grant: bool) -> None:
    """Change an existing registered account's role through an operator DB session."""
    with session_factory() as db:
        account = db.get(User, user_id)
        if account is None or account.is_guest or not account.email:
            raise ValueError("The account must exist, be registered, and have an email address")
        if account.is_instructor == grant:
            return
        account.is_instructor = grant
        db.commit()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("user_id", help="User ID from the authenticated account's session")
    parser.add_argument("action", choices=("grant", "revoke"))
    arguments = parser.parse_args(argv)
    settings = Settings.from_environment()
    engine, session_factory = database(settings.database_url)
    try:
        set_instructor_role(session_factory, arguments.user_id, arguments.action == "grant")
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    finally:
        engine.dispose()
    status = "granted" if arguments.action == "grant" else "revoked"
    print(f"Instructor access {status} for account {arguments.user_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
