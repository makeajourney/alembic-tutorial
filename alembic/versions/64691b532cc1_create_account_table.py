"""create account table

Revision ID: 64691b532cc1
Revises: 
Create Date: 2019-05-14 14:30:54.843911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64691b532cc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account') 
