"""empty message

Revision ID: 38af435d701f
Revises: cf9a951985ae
Create Date: 2019-08-17 13:32:26.262994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38af435d701f'
down_revision = 'cf9a951985ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###