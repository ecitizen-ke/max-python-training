import os
from dotenv import load_dotenv
from app import create_app
from instance.config import config

# Automatically load env variables on system startup
config_name = config.get(os.environ.get("ENV"))

app = create_app(config_name)


if __name__ == "__main__":
    app.run(debug=True)
