from database import db


class BookAuthor(db.Model):
    __tablename__ = 'book_author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String, nullable=False)
    book = db.Column(db.String, nullable=False)