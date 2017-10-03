import pymongo
from pymongo import MongoClient

#put this string in a config file
client = pymongo.MongoClient("mongodb://adm:dbpass@ds141454.mlab.com:41454/dev_jw")
db = client['dev_jw'] #replace test wiht name of acutal db or cluster

class TeamDBC:

    def get_team(self, team_id):
        return db.teams.find({'id': ObjectId(team_id)})


    def get_teams(self, team_ids=None):
        teams = [team for team in db.team.find({})]
        import ipdb; from pprint import pprint; ipdb.set_trace();
        return teams
