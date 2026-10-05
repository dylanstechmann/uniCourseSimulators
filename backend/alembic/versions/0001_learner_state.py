"""Server-owned learner state and immutable formative attempt records."""

import sqlalchemy as sa

from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def user_column():
    return sa.Column("user_id", sa.String(36), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


def row_id():
    return sa.Column("id", sa.String(36), primary_key=True)


def course_column():
    return sa.Column("course_id", sa.String(100), nullable=False)


def upgrade():
    op.create_table("users", row_id(), sa.Column("email", sa.String(254), unique=True),
                    sa.Column("password_hash", sa.Text()), sa.Column("is_guest", sa.Boolean(), nullable=False),
                    sa.Column("created_at", sa.DateTime(), nullable=False))
    op.create_table("sessions", sa.Column("token_hash", sa.String(64), primary_key=True), user_column(),
                    sa.Column("csrf_token", sa.String(64), nullable=False),
                    sa.Column("expires_at", sa.DateTime(), nullable=False))
    op.create_table("enrollments", row_id(), user_column(), course_column(),
                    sa.Column("content_version", sa.String(100), nullable=False),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.UniqueConstraint("user_id", "course_id", name="uq_enrollment_user_course"))
    op.create_table("progress", row_id(), user_column(), course_column(),
                    sa.Column("lesson_id", sa.String(100), nullable=False),
                    sa.Column("completed", sa.Boolean(), nullable=False),
                    sa.Column("updated_at", sa.DateTime(), nullable=False),
                    sa.UniqueConstraint("user_id", "course_id", "lesson_id", name="uq_progress_lesson"))
    op.create_table("notes", row_id(), user_column(), course_column(),
                    sa.Column("lesson_id", sa.String(100), nullable=False), sa.Column("body", sa.Text(), nullable=False),
                    sa.Column("updated_at", sa.DateTime(), nullable=False),
                    sa.UniqueConstraint("user_id", "course_id", "lesson_id", name="uq_note_lesson"))
    op.create_table("bookmarks", row_id(), user_column(), course_column(),
                    sa.UniqueConstraint("user_id", "course_id", name="uq_bookmark_course"))
    op.create_table("attempts", row_id(), user_column(), course_column(),
                    sa.Column("question_id", sa.String(100), nullable=False),
                    sa.Column("content_version", sa.String(100), nullable=False),
                    sa.Column("grading_policy_version", sa.String(100), nullable=False),
                    sa.Column("response", sa.JSON(), nullable=False), sa.Column("score", sa.Float(), nullable=False),
                    sa.Column("max_score", sa.Float(), nullable=False), sa.Column("result", sa.JSON(), nullable=False),
                    sa.Column("objective_ids", sa.JSON(), nullable=False), sa.Column("created_at", sa.DateTime(), nullable=False))
    for table in ("sessions", "enrollments", "progress", "notes", "bookmarks", "attempts"):
        op.create_index(f"ix_{table}_user_id", table, ["user_id"])
    op.create_index("ix_sessions_expires_at", "sessions", ["expires_at"])


def downgrade():
    for table in ("attempts", "bookmarks", "notes", "progress", "enrollments", "sessions", "users"):
        op.drop_table(table)
