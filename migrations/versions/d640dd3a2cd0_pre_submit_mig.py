"""pre submit mig

Revision ID: d640dd3a2cd0
Revises: 8f1d15b4bb33
Create Date: 2024-03-09 10:36:16.060083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd640dd3a2cd0'
down_revision: Union[str, None] = '8f1d15b4bb33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Item', 'id',
               existing_type=sa.INTEGER(),
               comment='Unique identifier for each item',
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text('nextval(\'"Item_id_seq"\'::regclass)'))
    op.alter_column('Item', 'title',
               existing_type=sa.VARCHAR(),
               comment='Title of the item',
               existing_nullable=True)
    op.alter_column('Item', 'content',
               existing_type=sa.VARCHAR(),
               comment='Content or description of the item',
               existing_nullable=True)
    op.alter_column('Item', 'status',
               existing_type=sa.VARCHAR(),
               comment="Status of the item, defaults to 'active'",
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Item', 'status',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment="Status of the item, defaults to 'active'",
               existing_nullable=True)
    op.alter_column('Item', 'content',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Content or description of the item',
               existing_nullable=True)
    op.alter_column('Item', 'title',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Title of the item',
               existing_nullable=True)
    op.alter_column('Item', 'id',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='Unique identifier for each item',
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text('nextval(\'"Item_id_seq"\'::regclass)'))
    # ### end Alembic commands ###
