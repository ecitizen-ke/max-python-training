from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")


print(app.config)


if __name__ == "__main__":
    app.run()
