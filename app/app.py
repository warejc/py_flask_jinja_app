# from api.api import api_blueprint
# import app.api
from flask import Flask
from app.api.api import api_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)

    return app
