from pyApp.resource import *
from pyApp.flask_app import *

# Hello World API
api.add_resource(HelloWorld, '/')

# Coin APIs
api.add_resource(GetAllCoinData, '/coin/get_all')
api.add_resource(UpdateCoinData, '/coin/update')
api.add_resource(InsertCoinData, '/coin/insert')
