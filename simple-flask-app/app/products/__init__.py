from flask import jsonify, Blueprint

products_bp = Blueprint("products_bp", __name__)


@products_bp.route("/products")
def get_products():
    products = [
        {"name": "Banana", "price": 10},
        {"name": "Apple", "price": 35},
    ]
    return jsonify(products)
