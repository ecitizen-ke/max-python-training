from flask import Blueprint, make_response
from app.models import State


states_bp = Blueprint("states_bp", __name__)


@states_bp.route("/states", methods=["GET"])
def get_states():
    res = State().get_states()
    if res:
        return make_response({"data": res, "status": 200}, 200)
    else:
        return make_response(
            {"message": "No States found in the database", "status": 404}, 404
        )


@states_bp.route("/states/filter", methods=["GET"])
def filter_by_starting_letter():
    res = State().filter()
    if res:
        return make_response({"data": res, "status": 200}, 200)
    else:
        return make_response(
            {"message": "No States found in the database", "status": 404}, 404
        )


@states_bp.route("/states", methods=["POST"])
def create_state():
    try:
        res = State().create("Auckland", "AU", 150000, 1898)
        return make_response({"data": res, "code": 201}, 201)
    except TypeError as e:
        return make_response({"message": str(e), "status": 400}, 400)


@states_bp.route("/states/update", methods=["PATCH"])
def update_state_by_id():
    try:
        res = State().update(2, 7278717)
        return make_response({"data": res, "code": 200}, 200)
    except TypeError as e:
        return make_response({"message": str(e), "status": 400}, 400)


@states_bp.route("/states/delete", methods=["DELETE"])
def delete_state_by_id():
    try:
        res = State().delete(12)
        if res:
            return make_response(
                {"message": "State deleted successfully!", "code": 200}, 200
            )
        else:
            return make_response(
                {"message": "Such a State does not exist", "code": 400}, 400
            )
    except TypeError as e:
        return make_response({"message": str(e), "status": 400}, 400)


@states_bp.route("/states/search", methods=["GET"])
def search_state_by_name():
    res = State().search("delaware")

    if res:
        return make_response({"data": res, "status": 200}, 200)
    else:
        return make_response(
            {"message": "No such State exists in the database", "status": 404}, 404
        )


@states_bp.route("/capitals", methods=["GET"])
def get_all_capitals():
    res = State().get_capitals()
    if res:
        return make_response({"data": res, "status": 200}, 200)
    else:
        return make_response(
            {"message": "No Capitals found in the database", "status": 404}, 404
        )


@states_bp.route("/states/populous", methods=["GET"])
def get_populous_state():
    res = State().get__most_populous()
    if res:
        return make_response({"data": res, "status": 200}, 200)
    else:
        return make_response(
            {"message": "No States found in the database", "status": 404}, 404
        )


@states_bp.route("/states_with_capitals", methods=["GET"])
def get_states_with_capitals():
    res = State().get_states_capitals()
    if res:
        return make_response({"data": res, "status": 200}, 200)
    else:
        return make_response(
            {"message": "No States found in the database", "status": 404}, 404
        )
