"""create hero table

Revision ID: 8d97d561d7fe
Revises: 337efe5fd9ee
Create Date: 2022-03-19 18:10:03.859284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d97d561d7fe'
down_revision = '337efe5fd9ee'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'hero',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('pathos', sa.String(200), nullable=False),
        sa.Column('force', sa.Integer),
        sa.Column('player', sa.Integer),
    )


def downgrade():
    op.drop_table('hero')
