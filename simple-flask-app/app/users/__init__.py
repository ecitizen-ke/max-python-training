from flask import jsonify


def users_view(app):
    @app.route("/users")
    def get_users():
        users = [
            {"name": "Nigel", "role": "admin"},
            {"name": "Naomi", "price": "customer"},
        ]
        return jsonify(users)
