"""001_create_author_table

Revision ID: 001_create_author_table
Revises: 
Create Date: 2022-09-01 23:23:15.823691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_author_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "author",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("first_name", sa.String(300), nullable=False, unique=True),
        sa.Column("last_name", sa.String(300), nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_table("author")
