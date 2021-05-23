"""Added Auditing Table

Revision ID: ed87977a61af
Revises: c43467470fd5
Create Date: 2021-05-23 16:20:39.941547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed87977a61af'
down_revision = 'c43467470fd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditing',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auditing_created_date'), 'auditing', ['created_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auditing_created_date'), table_name='auditing')
    op.drop_table('auditing')
    # ### end Alembic commands ###
