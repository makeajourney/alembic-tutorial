"""Add a column

Revision ID: 61b5ecbc4ded
Revises: 64691b532cc1
Create Date: 2019-05-14 15:57:54.502612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61b5ecbc4ded'
down_revision = '64691b532cc1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime)) 


def downgrade():
    op.drop_column('account', 'last_transaction_date')
 
