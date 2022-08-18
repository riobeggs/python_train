"""Add a column

Revision ID: 67d3cf47d75b
Revises: 37ae6c2c6006
Create Date: 2022-06-30 13:25:58.102435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67d3cf47d75b'
down_revision = '37ae6c2c6006'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')
