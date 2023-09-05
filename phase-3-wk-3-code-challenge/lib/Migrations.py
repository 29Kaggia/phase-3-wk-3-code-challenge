# migrations.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create restaurants table
    op.create_table(
        'restaurants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    # Create customers table
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    # Create reviews table
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=False),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customers.id')),
        sa.Column('restaurant_id', sa.Integer(), sa.ForeignKey('restaurants.id')),
        sa.PrimaryKeyConstraint('id'),
    )

def downgrade():
    op.drop_table('reviews')
    op.drop_table('customers')
    op.drop_table('restaurants')
