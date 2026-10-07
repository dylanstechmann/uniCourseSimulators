"""Add append-only retrieval-card self-ratings and their spaced-review schedule."""

import sqlalchemy as sa

from alembic import op

revision = "0008"
down_revision = "0007"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "card_reviews",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("user_id", sa.String(36), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("course_id", sa.String(100), nullable=False),
        sa.Column("lesson_id", sa.String(100), nullable=False),
        sa.Column("card_id", sa.String(120), nullable=False),
        sa.Column("content_version", sa.String(100), nullable=False),
        sa.Column("card_sha256", sa.String(64), nullable=False),
        sa.Column("policy_version", sa.String(40), nullable=False),
        sa.Column("rating", sa.String(8), nullable=False),
        sa.Column("repetitions", sa.Integer(), nullable=False),
        sa.Column("ease", sa.Float(), nullable=False),
        sa.Column("interval_days", sa.Float(), nullable=False),
        sa.Column("due_at", sa.DateTime(), nullable=False),
        sa.Column("reviewed_at", sa.DateTime(), nullable=False),
        sa.CheckConstraint("rating IN ('again', 'hard', 'good', 'easy')", name="ck_card_review_rating"),
        sa.CheckConstraint("repetitions >= 0", name="ck_card_review_repetitions_nonnegative"),
        sa.CheckConstraint("ease > 0", name="ck_card_review_ease_positive"),
        sa.CheckConstraint("interval_days >= 0", name="ck_card_review_interval_nonnegative"),
    )
    op.create_index("ix_card_reviews_user_id", "card_reviews", ["user_id"])
    op.create_index("ix_card_reviews_user_course_card", "card_reviews", ["user_id", "course_id", "card_id"])


def downgrade():
    op.drop_index("ix_card_reviews_user_course_card", table_name="card_reviews")
    op.drop_index("ix_card_reviews_user_id", table_name="card_reviews")
    op.drop_table("card_reviews")
