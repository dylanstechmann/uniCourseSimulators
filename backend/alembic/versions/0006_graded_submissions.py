"""Persist enrollment-scoped attempts for protected graded activities."""

import sqlalchemy as sa

from alembic import op

revision = "0006"
down_revision = "0005"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "graded_submissions",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("enrollment_id", sa.String(36), sa.ForeignKey("enrollments.id", ondelete="CASCADE"), nullable=False),
        sa.Column("plan_id", sa.String(36), sa.ForeignKey("assessment_plans.id", ondelete="CASCADE"), nullable=False),
        sa.Column(
            "assessment_instance_id", sa.String(36),
            sa.ForeignKey("assessment_instances.id", ondelete="CASCADE"), nullable=False,
        ),
        sa.Column("content_version", sa.String(100), nullable=False),
        sa.Column("attempt_number", sa.Integer(), nullable=False),
        sa.Column("source_sha256", sa.String(64), nullable=False),
        sa.Column("question_spec_sha256", sa.String(64), nullable=False),
        sa.Column("responses_json", sa.JSON(), nullable=False),
        sa.Column("results_json", sa.JSON(), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.Column("max_score", sa.Float(), nullable=False),
        sa.Column("submitted_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint(
            "enrollment_id", "assessment_instance_id", "attempt_number",
            name="uq_graded_submission_attempt",
        ),
        sa.CheckConstraint("attempt_number >= 1", name="ck_graded_submission_attempt_positive"),
        sa.CheckConstraint("score >= 0", name="ck_graded_submission_score_nonnegative"),
        sa.CheckConstraint("max_score > 0", name="ck_graded_submission_max_score_positive"),
        sa.CheckConstraint("score <= max_score", name="ck_graded_submission_score_lte_max"),
    )
    for column in ("enrollment_id", "plan_id", "assessment_instance_id"):
        op.create_index(f"ix_graded_submissions_{column}", "graded_submissions", [column])


def downgrade():
    op.drop_table("graded_submissions")
