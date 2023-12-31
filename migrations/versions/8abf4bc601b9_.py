"""empty message

Revision ID: 8abf4bc601b9
Revises: b3b71585d0a3
Create Date: 2023-10-31 15:56:14.847625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8abf4bc601b9'
down_revision = 'b3b71585d0a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_username')
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.create_index('ix_users_username', ['username'], unique=False)

    # ### end Alembic commands ###
