from flask import Blueprint, jsonify
from ..models.Book import Book

book_pb = Blueprint("book_pb", __name__)


@book_pb.route("/books", methods=["POST"])
def create_book():
    book = Book()
    result = book.save("0000000000001", "Introduction to GraphQL", 1)
    if not isinstance(result, str):
        return jsonify(
            {
                "code": 201,
                "status": "Created",
                "book": result,
            }
        )
    else:
        return jsonify({"code": 400, "status": "Bad Request", "message": result})
