from flask import Blueprint, jsonify, request
from ..models.Author import Author

author_pb = Blueprint("author_pb", __name__)


@author_pb.route("/authors", methods=["POST"])
def create_author():
    author = Author().create(1, "John", "Doe")
    if author:
        return jsonify(
            {
                "code": 201,
                "status": "Created",
                "message": "Author created successfully!",
            }
        )
    else:
        return jsonify(
            {
                "code": 400,
                "status": "Bad Request",
                "message": "Could not create user",
            }
        )


@author_pb.route("/authors", methods=["GET"])
def get_authors():
    authors = Author().get_authors()

    if authors:
        return jsonify(
            {
                "code": 200,
                "authors": authors,
                "message": "Success!",
                "status": "OK",
            }
        )

    else:
        return jsonify(
            {
                "code": 204,
                "message": "No authors Found!",
                "status": "No Content",
            }
        )


@author_pb.route("/authors/update", methods=["PATCH"])
def update_authors():
    data = {"first_name": "Jane", "last_name": "Dotty"}
    updated_author = Author().update(1, data)

    return jsonify(
        {
            "code": 200,
            "author": updated_author,
            "message": "Success!",
        }
    )
