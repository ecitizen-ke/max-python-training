from flask import jsonify, Blueprint

users_bp = Blueprint("users_bp", __name__)


@users_bp.route("/users")
def get_users():
    users = [
        {"name": "Nigel", "role": "admin"},
        {"name": "Naomi", "price": "customer"},
    ]
    return jsonify(users)
