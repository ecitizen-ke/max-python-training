from flask import Flask
from app.products import products_bp
from app.users import users_bp

app = Flask(__name__)
app.register_blueprint(products_bp)
app.register_blueprint(users_bp)


if __name__ == "__main__":
    app.run()
