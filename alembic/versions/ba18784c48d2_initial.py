
"""initial

Revision ID: ba18784c48d2
Revises: 
Create Date: 2023-09-06 23:13:07.906084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba18784c48d2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the 'baby' table
    op.create_table(
        'baby',
        sa.Column('baby_id', sa.Integer, primary_key=True),
        sa.Column('baby_name', sa.String, nullable=False),
        sa.Column('baby_weight', sa.Float, nullable=False),
        sa.Column('birth_date', sa.Date, nullable=False),
        sa.Column('sickness_details', sa.Text),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
    )


def downgrade() -> None:
    # Drop the 'baby' table if needed
    op.drop_table('baby')
