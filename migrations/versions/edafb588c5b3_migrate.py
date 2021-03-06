"""migrate

Revision ID: edafb588c5b3
Revises: 74e7b2d6e460
Create Date: 2021-06-03 21:54:20.450477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edafb588c5b3'
down_revision = '74e7b2d6e460'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=500), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('mouseline', sa.String(length=500), nullable=True),
    sa.Column('setup_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('cage', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_cage_setup_date'), ['setup_date'], unique=False)

    op.create_table('mouse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('genotype', sa.String(length=500), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.Column('cage', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['cage'], ['cage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('mouse', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_mouse_dob'), ['dob'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mouse', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mouse_dob'))

    op.drop_table('mouse')
    with op.batch_alter_table('cage', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_cage_setup_date'))

    op.drop_table('cage')
    # ### end Alembic commands ###
