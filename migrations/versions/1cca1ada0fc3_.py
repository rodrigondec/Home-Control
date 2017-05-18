"""empty message

Revision ID: 1cca1ada0fc3
Revises: 
Create Date: 2017-05-18 07:27:37.405311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cca1ada0fc3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('uso', sa.Column('leaf_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'uso', 'leaf', ['leaf_id'], ['id_leaf'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'uso', type_='foreignkey')
    op.drop_column('uso', 'leaf_id')
    # ### end Alembic commands ###
