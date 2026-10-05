"""Pin new attempts to the public practice specification that was graded."""

import sqlalchemy as sa

from alembic import op

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade():
    # Historical attempts remain intact and NULL transparently means the
    # pre-digest grader version could not pin a question specification.
    op.add_column("attempts", sa.Column("question_spec_sha256", sa.String(64), nullable=True))


def downgrade():
    op.drop_column("attempts", "question_spec_sha256")
