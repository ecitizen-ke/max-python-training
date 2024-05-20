from flask import jsonify


def products_view(app):
    @app.route("/products")
    def get_products():
        products = [
            {"name": "Banana", "price": 10},
            {"name": "Apple", "price": 35},
        ]
        return jsonify(products)
