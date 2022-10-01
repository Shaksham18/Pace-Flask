from pyApp.db_model import TableCoin, get_data_from_model_obj
from pyApp.flask_app import db_session


class CoinHandler:

    def __init__(self):
        self.db_session = db_session

    def get_all_coin_data(self):
        recs = self.db_session.query(TableCoin).all()
        ret_data = [get_data_from_model_obj(rec) for rec in recs]

        return {"data": ret_data}

