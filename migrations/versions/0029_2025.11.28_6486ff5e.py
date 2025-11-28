"""Add a tag field to revisions

Revision ID: 0029_2025.11.28_6486ff5e
Revises: 0028_2025.09.09_a0037268
Create Date: 2025-11-28 15:00:26.026695+00:00
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# Revision identifiers, used by Alembic
revision: str = "0029_2025.11.28_6486ff5e"
down_revision: str | None = "0028_2025.09.09_a0037268"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("revision", schema=None) as batch_op:
        batch_op.add_column(sa.Column("tag", sa.String(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("revision", schema=None) as batch_op:
        batch_op.drop_column("tag")
