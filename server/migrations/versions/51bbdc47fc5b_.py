"""empty message

Revision ID: 51bbdc47fc5b
Revises: 
Create Date: 2024-08-06 10:27:36.266872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51bbdc47fc5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctors_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publications_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video_games_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_games_table')
    op.drop_table('reviews_table')
    op.drop_table('publications_table')
    op.drop_table('patients_table')
    op.drop_table('doctors_table')
    op.drop_table('appointments_table')
    # ### end Alembic commands ###
