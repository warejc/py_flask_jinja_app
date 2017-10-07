import pymongo
from pymongo import MongoClient
from bson.json_util import loads, dumps
import configparser

conf = configparser.ConfigParser()
conf.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../', 'config.ini'))

db_pass = conf.get('Creds', 'db_pass')
connection_uri = "mongodb://adm:{0}@2ds141454.mlab.com:41454/dev_jw".format(db_pass)
client = pymongo.MongoClient(connection_uri)

db = client['dev_jw']

class TeamDBC:

    def get_team(self, team_id):

        return db.teams.find({'id': team_id})


    def get_teams(self, team_ids=None):
        teams = dumps([team for team in db.team.find().sort('name', pymongo.ASCENDING)])
        import ipdb; from pprint import pprint; ipdb.set_trace();
        return teams
