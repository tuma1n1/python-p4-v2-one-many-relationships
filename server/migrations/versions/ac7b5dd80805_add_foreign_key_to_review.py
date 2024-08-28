"""add foreign key to Review

Revision ID: ac7b5dd80805
Revises: eb2875433728
Create Date: 2024-08-28 20:58:44.021803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac7b5dd80805'
down_revision = 'eb2875433728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_reviews_employee_id_employees'), 'employees', ['employee_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_reviews_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')

    # ### end Alembic commands ###
