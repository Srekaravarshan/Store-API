import sqlite3
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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        if row:
            user = cls(*row) 
        else:
            user = None

        connection.close()
        return user 


    @classmethod
    def findById(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row) 
        else:
            user = None

        connection.close()
        return user 
