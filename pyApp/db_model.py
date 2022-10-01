from sqlalchemy import Column
from sqlalchemy import Integer
from pyApp.db_conn import DbConn
from sqlalchemy.ext.automap import automap_base

conn = DbConn()
_dbengine = conn.get_db_engine()
_meta = conn.get_metadata('pace')
_meta.reflect(views=True)

Base = automap_base(metadata=_meta)


class TableCoin(Base):
    __tablename__ = 'coin'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)


Base.prepare()


def get_data_from_model_obj(model_obj):
    return {column.name: getattr(model_obj, column.name) for column in model_obj.__table__.columns}