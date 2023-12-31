"""Create HealthcareProfessional and Assignment tables

Revision ID: 32cf4d6f0332
Revises: bcbfada2d4aa
Create Date: 2023-09-08 12:07:20.590224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32cf4d6f0332'
down_revision: Union[str, None] = 'bcbfada2d4aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('healthcare_professional',
    sa.Column('professional_id', sa.Integer(), nullable=False),
    sa.Column('professional_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('professional_id')
    )
    op.create_table('assignment',
    sa.Column('assignment_id', sa.Integer(), nullable=False),
    sa.Column('professional_id', sa.Integer(), nullable=True),
    sa.Column('baby_id', sa.Integer(), nullable=True),
    sa.Column('assigned_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['baby_id'], ['baby.baby_id'], ),
    sa.ForeignKeyConstraint(['professional_id'], ['healthcare_professional.professional_id'], ),
    sa.PrimaryKeyConstraint('assignment_id')
    )
    op.alter_column('baby', 'baby_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('baby', 'baby_weight',
               existing_type=sa.FLOAT(),
               nullable=True)
    op.alter_column('baby', 'birth_date',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('baby', 'birth_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('baby', 'baby_weight',
               existing_type=sa.FLOAT(),
               nullable=False)
    op.alter_column('baby', 'baby_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_table('assignment')
    op.drop_table('healthcare_professional')
    # ### end Alembic commands ###
