from flask import Flask
from flask_session import Session
from flask_cors import CORS

from flask_restful import Api
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from pyApp.db_model import _dbengine

app = Flask(__name__)
app.debug = True


app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'


DBSession = sessionmaker(bind=_dbengine)
db_session = scoped_session(DBSession)
Session(app)

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)






