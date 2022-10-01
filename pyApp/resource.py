from flask_restful import Resource

from pyApp.handler.coin_handler import CoinHandler


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}


class GetAllCoinData(Resource):
    def get(self):
        obj = CoinHandler()
        return obj.get_all_coin_data()

