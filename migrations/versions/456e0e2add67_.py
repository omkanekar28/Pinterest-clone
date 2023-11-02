"""empty message

Revision ID: 456e0e2add67
Revises: a86b0bc20174
Create Date: 2023-11-01 15:54:13.699221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '456e0e2add67'
down_revision = 'a86b0bc20174'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.alter_column('uploaded_on',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.alter_column('uploaded_on',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)

    # ### end Alembic commands ###
