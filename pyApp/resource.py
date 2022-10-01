from flask import request
from flask_restful import Resource

from pyApp.handler.coin_handler import CoinHandler


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}


class GetAllCoinData(Resource):
    def get(self):
        obj = CoinHandler()
        return obj.get_all_coin_data()


class UpdateCoinData(Resource):
    def post(self):
        payload = request.get_json()
        obj = CoinHandler()
        return obj.bulk_update_data(payload['data'])


class InsertCoinData(Resource):
    def post(self):
        payload = request.get_json()
        obj = CoinHandler()
        return obj.bulk_insert_data(payload['data'])

