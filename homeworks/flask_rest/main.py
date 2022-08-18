from flask import Flask

from user_api import user_router
from book_api import book_router
app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(book_router)
status_code_created = 404


@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
