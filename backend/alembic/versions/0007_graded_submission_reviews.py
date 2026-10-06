"""Add auditable human-review decisions for graded submissions."""

import sqlalchemy as sa

from alembic import op

revision = "0007"
down_revision = "0006"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "graded_submission_appeals",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column(
            "submission_id",
            sa.String(36),
            sa.ForeignKey("graded_submissions.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("user_id", sa.String(36), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint("submission_id", name="uq_graded_submission_appeal_submission"),
    )
    op.create_index("ix_graded_submission_appeals_submission_id", "graded_submission_appeals", ["submission_id"])
    op.create_index("ix_graded_submission_appeals_user_id", "graded_submission_appeals", ["user_id"])

    op.create_table(
        "graded_submission_appeal_reviews",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column(
            "appeal_id",
            sa.String(36),
            sa.ForeignKey("graded_submission_appeals.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "reviewer_user_id",
            sa.String(36),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("reviewer_email", sa.String(254), nullable=False),
        sa.Column("decision", sa.String(20), nullable=False),
        sa.Column("review_note", sa.Text(), nullable=False),
        sa.Column("override_score", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint("appeal_id", name="uq_graded_submission_appeal_review_appeal"),
        sa.CheckConstraint(
            "decision IN ('adjusted', 'upheld', 'declined')",
            name="ck_graded_submission_appeal_review_decision",
        ),
        sa.CheckConstraint(
            "(decision = 'adjusted' AND override_score IS NOT NULL) OR "
            "(decision IN ('upheld', 'declined') AND override_score IS NULL)",
            name="ck_graded_submission_appeal_review_score_matches_decision",
        ),
        sa.CheckConstraint(
            "override_score IS NULL OR override_score >= 0",
            name="ck_graded_submission_appeal_review_score_nonnegative",
        ),
    )
    op.create_index(
        "ix_graded_submission_appeal_reviews_appeal_id",
        "graded_submission_appeal_reviews",
        ["appeal_id"],
    )
    op.create_index(
        "ix_graded_submission_appeal_reviews_reviewer_user_id",
        "graded_submission_appeal_reviews",
        ["reviewer_user_id"],
    )


def downgrade():
    op.drop_table("graded_submission_appeal_reviews")
    op.drop_table("graded_submission_appeals")
