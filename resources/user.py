from flask_restful import Resource, reqparse
from models.user import User
from models.user import User

class RegisterUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "It cannot be blank, please enter your username"
    )
    
    parser.add_argument('password',
        type = str,
        required = True,
        help = "It cannot be blank, please enter your password"
    )

    @classmethod
    def post(cls):

        data = cls.parser.parse_args()

        if User.findByUsername(data['username']):
            return {'message': 'Already registered'}, 400

        user = User(data['username'], data['password'])
        user.saveToDb()

        return {'message': 'successfully registered'}, 201
