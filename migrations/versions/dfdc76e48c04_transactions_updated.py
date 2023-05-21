"""transactions_updated

Revision ID: dfdc76e48c04
Revises: 03965ce91c5d
Create Date: 2023-05-21 20:14:58.511354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfdc76e48c04'
down_revision = '03965ce91c5d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('card_id', sa.BigInteger(), nullable=True))
    op.create_foreign_key(None, 'transactions', 'cards', ['card_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.drop_column('transactions', 'card_id')
    # ### end Alembic commands ###