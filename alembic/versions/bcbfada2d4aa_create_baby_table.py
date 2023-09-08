"""create_baby_table

Revision ID: bcbfada2d4aa
Revises: ba18784c48d2
Create Date: 2023-09-06 23:26:02.481196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bcbfada2d4aa'
down_revision: Union[str, None] = 'ba18784c48d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
