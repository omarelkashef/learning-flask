"""removed redundant description column from posts

Revision ID: fd699a5ce38f
Revises: 0db006ef5874
Create Date: 2023-07-03 22:07:58.045624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd699a5ce38f'
down_revision = '0db006ef5874'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
