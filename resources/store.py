from flask_restful import Resource
from models.storeModel import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.findByName(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.findByName(name):
            return {'message': "Store with name '{}' already exists".format(name)}
        
        store = StoreModel(name)
        try:
            store.saveToDb()
        except:
            return {'message': 'An error occured on storing'}, 500
        
        return store.json(), 201
        

    def delete(self, name):
        store = StoreModel.findByName(name)
        if store:
            store.deleteFromDb()
        return {'message': 'store is deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}