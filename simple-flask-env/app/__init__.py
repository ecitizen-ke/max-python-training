from flask import Flask


def create_app(config_name):
    """This function returns a flask object"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    print(app.config)

    return app
