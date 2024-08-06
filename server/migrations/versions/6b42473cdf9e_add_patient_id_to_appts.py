"""add patient_id to appts

Revision ID: 6b42473cdf9e
Revises: 939d53e0a7c4
Create Date: 2024-08-06 11:39:25.036452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b42473cdf9e'
down_revision = '939d53e0a7c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('patient_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_appointments_table_patient_id_patients_table'), 'patients_table', ['patient_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments_table', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_appointments_table_patient_id_patients_table'), type_='foreignkey')
        batch_op.drop_column('patient_id')

    # ### end Alembic commands ###