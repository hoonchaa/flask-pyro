"""empty message

Revision ID: 6898f22d4043
Revises: 221f6b40168d
Create Date: 2024-12-28 22:15:04.812570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6898f22d4043'
down_revision = '221f6b40168d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_upload')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_upload',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('subject', sa.VARCHAR(length=200), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('modify_date', sa.DATETIME(), nullable=True),
    sa.Column('filename', sa.VARCHAR(length=150), nullable=False),
    sa.Column('file_path', sa.VARCHAR(length=500), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_upload_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pk_upload')
    )
    # ### end Alembic commands ###
