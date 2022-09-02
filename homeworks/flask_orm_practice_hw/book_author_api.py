import http
from flask import Blueprint, jsonify, request
from models.book_author import BookAuthor
from models.book import Book
from models.author import Author
from database import db
from serializers.book_author import BookAuthorSchema


book_author_router = Blueprint("book_author", __name__, url_prefix='/book_author')


@book_author_router.route('')
def get():
    data = BookAuthor.query.all()
    data_json = BookAuthorSchema().dump(data, many=True)
    return jsonify(data_json)


@book_author_router.route('/<int:id_>')
def retrieve(id_):
    data = BookAuthor.query.filter_by(id=id_).first()
    data_json = BookAuthorSchema().dump(data)
    return jsonify(data_json)


@book_author_router.route('/<int:book_id>/<int:author_id>')
def create(book_id, author_id):
    if Book.query.filter(
            Book.id == book_id).first() and Author.query.filter(
            Author.id == author_id).first():
        data = BookAuthor(book_id=book_id, author_id=author_id)
        db.session.add(data)
        db.session.commit()
        data_json = BookAuthorSchema().dump(data)
        return jsonify(data_json), http.HTTPStatus.CREATED
    else:
        return 'error', http.HTTPStatus.BAD_REQUEST


@book_author_router.route('', methods=['PUT'])
def update():
    data = request.get_json(force=True)

    if book_author_data := BookAuthor.query.filter_by(id=data["id"]).first():
        book_author_data.book_id, book_author_data.author_id = data["book_id"], data["author_id"]
        db.session.add(book_author_data)
        db.session.commit()
        b_a_update = BookAuthorSchema().dump(book_author_data)
        return jsonify(b_a_update)
    else:
        return 'error', http.HTTPStatus.BAD_REQUEST


@book_author_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    BookAuthor.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
