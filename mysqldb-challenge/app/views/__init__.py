from flask import Blueprint, jsonify
from app.models import State


states_bp = Blueprint("states_bp", __name__)


@states_bp.route("/states", methods=["GET"])
def get_states():
    states = State().get_states()
    return jsonify({"states": states, "code": 200})


@states_bp.route("/states/filter", methods=["GET"])
def filter_by_starting_letter():
    states = State().filter()
    return jsonify({"states": states, "code": 200})


@states_bp.route("/states", methods=["POST"])
def create_state():
    state = State().create("Maryland", "ML", 20000, 1853)
    return jsonify({"state": state, "code": 201})
