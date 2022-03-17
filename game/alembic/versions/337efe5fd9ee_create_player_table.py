"""create player table

Revision ID: 337efe5fd9ee
Revises: 
Create Date: 2022-03-17 01:31:45.450407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '337efe5fd9ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'player',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(200), nullable=False),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('gold', sa.Integer),
    )


def downgrade():
    op.drop_table('player')
