"""Initial migration

Revision ID: 1ce0d4c92049
Revises: bdda1ab36c61
Create Date: 2024-06-12 07:10:11.330177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ce0d4c92049'
down_revision: Union[str, None] = 'bdda1ab36c61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('maps_url', sa.String(length=355), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'maps_url')
    # ### end Alembic commands ###
