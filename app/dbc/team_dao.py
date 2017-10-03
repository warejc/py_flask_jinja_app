from pymongo import MongoClient

#put this string in a config file
client = pymongo.MongoClient('mongodb://adm:<dbpassword>@ds141454.mlab.com:41454/')
db = client.dev_jw #replace test wiht name of acutal db or cluster

class TeamDBC:

    def get_team(self, team_id):
        return db.teams.find({'id': ObjectId(team_id)})


    def get_teams(self, team_ids):
        return db.team.find({})
