"""empty message

Revision ID: 83656c6f8468
Revises: 6898f22d4043
Create Date: 2024-12-28 22:29:38.234365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83656c6f8468'
down_revision = '6898f22d4043'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('upload', schema=None) as batch_op:
        batch_op.add_column(sa.Column('process', sa.String(length=50), server_default='temp', nullable=True))
        batch_op.add_column(sa.Column('device', sa.String(length=50), server_default='temp', nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('upload', schema=None) as batch_op:
        batch_op.drop_column('device')
        batch_op.drop_column('process')

    # ### end Alembic commands ###
