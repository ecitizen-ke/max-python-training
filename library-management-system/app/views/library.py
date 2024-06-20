from flask import Blueprint, jsonify
from ..models.Library import Library

library_pb = Blueprint("library_pb", __name__)


@library_pb.route("/library", methods=["GET"])
def get_library():
    results = Library().get_books()
    if results:
        return jsonify({"code": 200, "status": "OK", "library": results})
    else:
        return jsonify(
            {
                "code": 204,
                "status": "No Content",
                "message": "Such a book does not exist in our library",
            }
        )


@library_pb.route("/library", methods=["POST"])
def add_book_to_library():
    result = Library().add_book("Introduction to GraphQL")
    if not isinstance(result, str):
        return jsonify({"code": 201, "status": "Created", "book": result})
    else:
        return jsonify({"code": 400, "status": "Bad Request", "message": result})


@library_pb.route("/library/search", methods=["GET"])
def search_book_in_library():
    result = Library().search("Introduction to GraphQL")
    if result:
        return jsonify({"code": 201, "status": "Created", "book": result})
    else:
        return jsonify(
            {
                "code": 204,
                "status": "No Content",
                "message": "Such a book does not exist in our library",
            }
        )


@library_pb.route("/library/checkout", methods=["PATCH"])
def borrow_book_from_library():
    result = Library().checkout("Introduction to GraphQL")
    if result:
        return jsonify({"code": 200, "status": "OK", "message": result})


@library_pb.route("/library/checkin", methods=["PATCH"])
def return_book_to_library():
    result = Library().checkin("Introduction to GraphQL")
    if result:
        return jsonify({"code": 200, "status": "OK", "message": result})
