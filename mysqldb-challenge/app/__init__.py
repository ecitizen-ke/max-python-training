from flask import Flask
from app.views import states_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")
    app.register_blueprint(states_bp)
    return app
