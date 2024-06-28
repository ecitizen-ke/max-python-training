from flask import Blueprint, request, jsonify
from app.models import User

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    # initialize the user object
    user = User()

    # Get data from the request object
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # invoke create user method

    user.create(username, password)
    return jsonify({"message": "user registered successfully", "status": 201})


@user_bp.route("/login", methods=["POST"])
def login():
    # initialize the user object
    user = User()
    # Invoke the user login method
    # Get data from the request object
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")
    login = user.user_login(username, password)
    if login:
        return jsonify({"message": "User login successful!", "status": 200})
    else:
        return jsonify({"message": "Wrong login credentials!", "status": 401})
