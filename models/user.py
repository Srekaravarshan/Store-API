from db import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,_id, username,  password):
        self.username = username
        self.id = _id
        self.password = password

    @classmethod
    def findByUsername(cls, name):
        return cls.query.filter_by(username=name).first()


    @classmethod
    def findById(cls, _id):
        return cls.query.filter_by(id=_id).first() 
