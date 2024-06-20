from flask import Flask
from app.views.author import author_pb
from app.views.book import book_pb
from app.views.library import library_pb


def create_app():
    app = Flask(__name__)
    app.register_blueprint(author_pb)
    app.register_blueprint(book_pb)
    app.register_blueprint(library_pb)

    return app
