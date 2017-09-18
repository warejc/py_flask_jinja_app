from app.db import db, Profile
from app.generate_jwt_token import generate_jwt_token
from datetime import datetime
from flask import Blueprint, Flask, request, jsonify
from services.team_service import TeamService
from os import environ, path
from time import mktime

app = Flask(__name__)
accepted_image_mimetypes = ['application/x-yaml', 'text/yaml']
jinja = Environment(loader=FileSystemLoader(path.dirname(path.abspath(__file__))), trim_blocks=True)
team_service = TeamService()
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/')
def get_teams():
    #Go get all the teams in the db
    teams = team_service.get_teams()

    return jsonify({'teams': teams}), 200

@api_blueprint.route('/<team_id>')
def get_team(team_id):
    #get single team data
    team = team_service.get_teams(team_id=team_id)
    return jsonify({'team': team}), 200

# @api_blueprint.route('/upload_org')
# def upload():
# upload team to db
#     return jinja.get_template('upload_org.html.j2').render()

# @api_blueprint.route('/auth/<source_employee_id>')
# def login(source_employee_id):
#     redirect_to_index = redirect('{}?_dt={}'.format(environ['APP_URL'], mktime(datetime.now().timetuple())))

#     response = make_response(redirect_to_index)
#     response.set_cookie('token', value=generate_jwt_token(source_employee_id))

#     return response
