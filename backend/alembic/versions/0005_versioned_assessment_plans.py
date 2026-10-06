"""Persist enrollment-scoped assessment policy and assignment snapshots."""

import sqlalchemy as sa

from alembic import op

revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "assessment_plans",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("enrollment_id", sa.String(36), sa.ForeignKey("enrollments.id", ondelete="CASCADE"), nullable=False),
        sa.Column("content_version", sa.String(100), nullable=False),
        sa.Column("grading_mode", sa.String(32), nullable=False),
        sa.Column("policy_json", sa.JSON(), nullable=False),
        sa.Column("snapshot_sha256", sa.String(64), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint("enrollment_id", "content_version", name="uq_assessment_plan_version"),
    )
    op.create_index("ix_assessment_plans_enrollment_id", "assessment_plans", ["enrollment_id"])
    op.create_table(
        "assessment_instances",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("plan_id", sa.String(36), sa.ForeignKey("assessment_plans.id", ondelete="CASCADE"), nullable=False),
        sa.Column("assessment_id", sa.String(120), nullable=False),
        sa.Column("assessment_type", sa.String(32), nullable=False),
        sa.Column("mode", sa.String(24), nullable=False),
        sa.Column("title", sa.String(240), nullable=True),
        sa.Column("category_id", sa.String(100), nullable=True),
        sa.Column("week", sa.Integer(), nullable=True),
        sa.Column("points", sa.Float(), nullable=False),
        sa.Column("source_path", sa.Text(), nullable=False),
        sa.Column("source_sha256", sa.String(64), nullable=False),
        sa.Column("objective_ids", sa.JSON(), nullable=False),
        sa.Column("question_ids", sa.JSON(), nullable=False),
        sa.Column("release_at", sa.DateTime(), nullable=True),
        sa.Column("due_at", sa.DateTime(), nullable=True),
        sa.Column("attempt_limit", sa.Integer(), nullable=True),
        sa.Column("attempt_scoring", sa.String(16), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint("plan_id", "assessment_id", name="uq_assessment_instance_id"),
        sa.CheckConstraint("mode IN ('practice', 'graded', 'self-assessment')", name="ck_assessment_instance_mode"),
        sa.CheckConstraint("points >= 0", name="ck_assessment_instance_points_nonnegative"),
        sa.CheckConstraint("attempt_limit IS NULL OR attempt_limit >= 1", name="ck_assessment_instance_attempt_limit"),
    )
    op.create_index("ix_assessment_instances_plan_id", "assessment_instances", ["plan_id"])


def downgrade():
    op.drop_table("assessment_instances")
    op.drop_table("assessment_plans")
