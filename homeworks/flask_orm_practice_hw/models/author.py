from database import db


class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(300), nullable=False, unique=False)
    last_name = db.Column(db.String(300), nullable=False, unique=False)
