"""minutes migrate

Revision ID: 5d3646f3af71
Revises: 
Create Date: 2023-03-27 00:32:35.939532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d3646f3af71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_temperature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('_alembic_tmp_daily_temperature')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_daily_temperature',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('temperature', sa.FLOAT(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('daily_temperature')
    # ### end Alembic commands ###
