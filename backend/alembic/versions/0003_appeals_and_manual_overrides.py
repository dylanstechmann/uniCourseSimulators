"""Add immutable appeal requests and audited instructor review decisions."""

import sqlalchemy as sa

from alembic import op

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "appeals",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("attempt_id", sa.String(length=36), nullable=False),
        sa.Column("user_id", sa.String(length=36), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["attempt_id"], ["attempts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("attempt_id", name="uq_appeal_attempt"),
    )
    op.create_index("ix_appeals_attempt_id", "appeals", ["attempt_id"])
    op.create_index("ix_appeals_user_id", "appeals", ["user_id"])
    op.create_table(
        "appeal_reviews",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("appeal_id", sa.String(length=36), nullable=False),
        sa.Column("reviewer_user_id", sa.String(length=36), nullable=True),
        sa.Column("reviewer_email", sa.String(length=254), nullable=False),
        sa.Column("decision", sa.String(length=20), nullable=False),
        sa.Column("review_note", sa.Text(), nullable=False),
        sa.Column("override_score", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.CheckConstraint(
            "decision IN ('adjusted', 'upheld', 'declined')",
            name="ck_appeal_review_decision",
        ),
        sa.CheckConstraint(
            "(decision = 'adjusted' AND override_score IS NOT NULL) OR "
            "(decision IN ('upheld', 'declined') AND override_score IS NULL)",
            name="ck_appeal_review_score_matches_decision",
        ),
        sa.CheckConstraint(
            "override_score IS NULL OR override_score >= 0",
            name="ck_appeal_review_score_nonnegative",
        ),
        sa.ForeignKeyConstraint(["appeal_id"], ["appeals.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["reviewer_user_id"], ["users.id"], ondelete="SET NULL"),
        sa.UniqueConstraint("appeal_id", name="uq_appeal_review_appeal"),
    )
    op.create_index("ix_appeal_reviews_appeal_id", "appeal_reviews", ["appeal_id"])
    op.create_index("ix_appeal_reviews_reviewer_user_id", "appeal_reviews", ["reviewer_user_id"])


def downgrade():
    op.drop_index("ix_appeal_reviews_reviewer_user_id", table_name="appeal_reviews")
    op.drop_index("ix_appeal_reviews_appeal_id", table_name="appeal_reviews")
    op.drop_table("appeal_reviews")
    op.drop_index("ix_appeals_user_id", table_name="appeals")
    op.drop_index("ix_appeals_attempt_id", table_name="appeals")
    op.drop_table("appeals")
