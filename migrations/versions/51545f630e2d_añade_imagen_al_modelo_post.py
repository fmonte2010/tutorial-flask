"""añade imagen al modelo post

Revision ID: 51545f630e2d
Revises: 4a099e24babf
Create Date: 2021-01-01 14:22:35.150944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51545f630e2d'
down_revision = '4a099e24babf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image_name', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image_name')
    # ### end Alembic commands ###
