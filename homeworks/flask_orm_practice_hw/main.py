from flask import Flask
from book_author_api import book_author_router
from config import Config
from database import db
from author_api import author_router
from book_api import book_router


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(author_router)
    app.register_blueprint(book_router)
    app.register_blueprint(book_author_router)
    return app


def setup_db():
    with app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, host='0.0.0.0', debug=True)