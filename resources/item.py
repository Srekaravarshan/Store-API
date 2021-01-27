from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = 'This field cannot be blank'
    )
    parser.add_argument('store_id',
        type = int,
        required = True,
        help = 'Every store must have a store id'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.findByName(name)
        if item:
            return item.json()
        return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.findByName(name):
            return {'message': 'The item \'{}\' is already exists'.format(name)}, 400


        data = Item.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.saveToDb()
        except:
            return {'message': 'error occoured on inserting item'}, 500
        
        return item.json(), 201

    def delete(cls, name):
        item = ItemModel.findByName(name)
        if item:
            item.deleteFromDb()
            return{'message': 'Item deleted'}
        
        return {'message': 'Item not found'}, 404

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.findByName(name)

        if item is None:
            item = ItemModel(name, **data)
            
        else:
            item.price = data['price']
            
        item.saveToDb()
        return item.json()
    

class Items(Resource):
    def get(self):
        # return {'items': [item.json() for item in ItemModel.query.all()]} 
        return {'items': list(map(lambda x: x.json(),ItemModel.query.all()))} 

