"""Add an operator-provisioned account role for instructor review."""

import sqlalchemy as sa

from alembic import op

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        sa.Column("is_instructor", sa.Boolean(), server_default=sa.false(), nullable=False),
    )
    # Existing untrusted email-allowlisted accounts do not carry authority forward.


def downgrade():
    op.drop_column("users", "is_instructor")
