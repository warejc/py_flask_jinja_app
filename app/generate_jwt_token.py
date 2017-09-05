import jwt
import os
from datetime import datetime, timedelta


def generate_jwt_token(user_id):
    """
    Generates a jwt token for use on each scenario
    Args:
        user_id: the user id (integrations) to be stored in the token
    Return:
        a jwt token with the valid fields in it
    """
    issue_time = datetime.utcnow()
    expiration = issue_time + timedelta(days=1)
    not_before = issue_time
    token = {'exp': expiration,
             'iat': issue_time,
             'nbf': not_before,
             'identity': user_id}
    return jwt.encode(token, os.environ['JWT_SECRET'], 'HS256').decode('utf-8')
