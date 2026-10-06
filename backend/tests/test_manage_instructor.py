import pytest

from courselab.db import Base, User, database
from courselab.manage_instructor import set_instructor_role


def test_operator_can_grant_and_revoke_role_without_an_http_path(tmp_path):
    engine, session_factory = database(f"sqlite:///{tmp_path}/roles.db")
    Base.metadata.create_all(engine)
    with session_factory() as db:
        account = User(email="reviewer@example.org", password_hash="test", is_guest=False)
        db.add(account)
        db.commit()
        user_id = account.id

    set_instructor_role(session_factory, user_id, True)
    with session_factory() as db:
        assert db.get(User, user_id).is_instructor is True
    set_instructor_role(session_factory, user_id, False)
    with session_factory() as db:
        assert db.get(User, user_id).is_instructor is False
    engine.dispose()


def test_operator_cannot_assign_roles_to_guests_or_missing_users(tmp_path):
    engine, session_factory = database(f"sqlite:///{tmp_path}/guests.db")
    Base.metadata.create_all(engine)
    with session_factory() as db:
        guest = User(is_guest=True)
        db.add(guest)
        db.commit()
        guest_id = guest.id
    with pytest.raises(ValueError, match="registered"):
        set_instructor_role(session_factory, guest_id, True)
    with pytest.raises(ValueError, match="registered"):
        set_instructor_role(session_factory, "missing-account", True)
    engine.dispose()
