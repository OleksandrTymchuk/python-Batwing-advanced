"""002_create_book_table

Revision ID: 002_create_book_table
Revises: 001_create_author_table
Create Date: 2022-09-02 00:02:21.482280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_book_table'
down_revision = '001_create_author_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("book_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(300), nullable=False, unique=True),
        sa.Column("description", sa.String(3000), nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_table("book")

