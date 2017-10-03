from app.db import db, Profile
from app.generate_jwt_token import generate_jwt_token
from datetime import datetime
from flask import Blueprint, Flask, request, jsonify
from app.dbc.team_dbc import TeamDBC
from os import environ, path
from time import mktime

team_dbc = TeamDBC()
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/', methods=['GET'])
def get_teams():
    #Go get all the teams in the db
    teams = team_dbc.get_teams()

    return jsonify({'teams': teams}), 200

@api_blueprint.route('/<team_id>', methods=['GET'])
def get_team(team_id):
    #get single team data
    team = team_dbc.get_teams(team_id=team_id)
    return jsonify({'team': team}), 200
