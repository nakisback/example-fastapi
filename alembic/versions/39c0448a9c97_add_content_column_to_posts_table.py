"""add content column to posts table

Revision ID: 39c0448a9c97
Revises: 7bbd71ae8cd8
Create Date: 2024-04-19 22:13:16.182633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39c0448a9c97'
down_revision: Union[str, None] = '7bbd71ae8cd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
