import time

from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors

from pyApp.db_model import TableCoin, get_data_from_model_obj
from pyApp.flask_app import db_session


class CoinHandler:

    def __init__(self):
        self.db_session = db_session

    def get_all_coin_data(self):
        recs = self.db_session.query(TableCoin).order_by(TableCoin.id).all()
        ret_data = [get_data_from_model_obj(rec) for rec in recs]

        return {"data": ret_data}

    def bulk_update_data(self, data):
        try:
            self.db_session.bulk_update_mappings(TableCoin, data)
            self.db_session.commit()
            return {"msg": "Data Updated Successfully"}
        except Exception as e:
            self.db_session.rollback()
            return {"msg": "Data Format/Duplicate Issue Found", "err_detail": str(e)}

    def bulk_insert_data(self, data):
        try:
            self.db_session.bulk_insert_mappings(TableCoin, data)
            self.db_session.commit()
            return {"msg": "Data Inserted Successfully"}
        except Exception as e:
            self.db_session.rollback()
            return {"msg": "Data Format Issue Found", "err_detail": str(e)}

