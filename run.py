from app.db import db, Profile
from app.generate_jwt_token import generate_jwt_token
from datetime import datetime
from flask import Flask, redirect, make_response, request
from integration_client.employee import employee as employee_client
from jinja2 import Environment, FileSystemLoader
from os import environ, path
from time import mktime

app = Flask(__name__)

if __name__ == '__main__':
    # TODO: Remove when micro-services for Account exist
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    app.run(debug=True, host='0.0.0.0')
