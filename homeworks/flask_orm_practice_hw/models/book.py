from database import db


class Book(db.Model):
    __tablename__ = "book"

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(3000), nullable=False)
