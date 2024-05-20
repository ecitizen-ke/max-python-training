from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/products")
def get_products():
    products = [
        {"name": "Banana", "price": 10},
        {"name": "Apple", "price": 35},
    ]
    return jsonify(products)


@app.route("/users")
def get_users():
    users = [
        {"name": "Nigel", "role": "admin"},
        {"name": "Naomi", "price": "customer"},
    ]
    return jsonify(users)


if __name__ == "__main__":
    app.run()
