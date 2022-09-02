"""003_many_to_many_relation

Revision ID: 003_many_to_many_relation
Revises: 002_create_book_table
Create Date: 2022-09-02 01:07:26.388259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_many_to_many_relation'
down_revision = '002_create_book_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book_author",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("book_id", sa.Integer, sa.ForeignKey("book.id")),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("author.id"))
    )


def downgrade() -> None:
    op.drop_table("book_author")
