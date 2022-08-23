from main import db
from models.book import Book

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(Book(author="sapkowski"))
    db.session.commit()
    print('created tables')
