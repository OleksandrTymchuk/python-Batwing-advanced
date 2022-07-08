import http
from flask import Blueprint, Response, request
from db.bookdb import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    books = db.get_all()
    return Response(str(books))


@book_router.route('/<string:id>')
def retrieve(id):
    book = db.retrieve(id)
    return book


@book_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    author = request.json.get("author")
    genre = request.json.get("genre")
    id = request.json.get('id')
    new_book = db.add(name, author, genre, id)
    if not new_book:
        return "This book is already exists", http.HTTPStatus.BAD_REQUEST
    else:
        return new_book, http.HTTPStatus.CREATED


@book_router.route('/<id>', methods=['PUT'])
def update(id):
    name = request.json.get("name")
    author = request.json.get("author")
    genre = request.json.get("genre")
    update_book = db.update(name, author, genre, id)

    if not update_book:
        return "This book doesn't exists", http.HTTPStatus.BAD_REQUEST
    else:
        return "Books data has been changed", http.HTTPStatus.CREATED


@book_router.route('/<string:id>', methods=['DELETE'])
def delete(id):
    dlt = db.delete(id)
    return dlt
