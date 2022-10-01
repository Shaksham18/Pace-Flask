from pyApp.resource import *
from pyApp.flask_app import *

# Hello World API
api.add_resource(HelloWorld, '/')

# Get All Coin API
api.add_resource(GetAllCoinData, '/coin/get_all')