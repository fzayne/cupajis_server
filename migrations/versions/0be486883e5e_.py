"""empty message

Revision ID: 0be486883e5e
Revises: 6d92803a3f26
Create Date: 2022-06-01 18:36:13.531512

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0be486883e5e'
down_revision = '6d92803a3f26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Users_token', table_name='Users')
    op.drop_column('Users', 'token_expiration')
    op.drop_column('Users', 'token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('token', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
    op.add_column('Users', sa.Column('token_expiration', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_Users_token', 'Users', ['token'], unique=False)
    # ### end Alembic commands ###