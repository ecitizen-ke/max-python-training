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


@states_bp.route("/states/update", methods=["PATCH"])
def update_state_by_id():
    update = State().update(12, 150000)
    return jsonify({"state": update, "code": 200})


@states_bp.route("/states/delete", methods=["DELETE"])
def delete_state_by_id():
    update = State().delete(13)
    return jsonify({"state": update, "code": 200})


@states_bp.route("/states/search", methods=["GET"])
def search_state_by_name():
    state = State().search("delaware")
    return jsonify({"state": state, "code": 200})


@states_bp.route("/capitals", methods=["GET"])
def get_all_capitals():
    capitals = State().get_capitals()
    return jsonify({"capitals": capitals, "code": 200})


@states_bp.route("/states/populous", methods=["GET"])
def get_populous_state():
    state = State().get__most_populous()
    return jsonify({"state": state, "code": 200})


@states_bp.route("/states_with_capitals", methods=["GET"])
def get_states_with_capitals():
    states = State().get_states_capitals()
    return jsonify({"state": states, "code": 200})
