from flask import Flask, jsonify
from app.products import products_view
from app.users import users_view

app = Flask(__name__)

products_view(app)
users_view(app)


if __name__ == "__main__":
    app.run()
