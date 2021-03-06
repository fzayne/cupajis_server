"""empty message

Revision ID: 6383ab21cf30
Revises: cb28e66d16d7
Create Date: 2022-06-07 21:55:36.523697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6383ab21cf30'
down_revision = 'cb28e66d16d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Items', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Items', sa.Column('type', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
