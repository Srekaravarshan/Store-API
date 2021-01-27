from werkzeug.security import safe_str_cmp
from models.user import User

def authenticate(username, password):
    data = User.findByUsername(username)
    if data and safe_str_cmp(data.password, password) :
            return data

def identity(payload):
    userId = payload['identity']
    return User.findById(userId)