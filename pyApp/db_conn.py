from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm.session import sessionmaker


class DbConn:

    def __init__(self):
        cnf = {'user': 'admin', 'password': 'postgres', 'host': 'localhost:5432', 'db': 'pace'}
        con_string = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(cnf['user'], cnf['password'],
                                                                    cnf['host'], cnf['db'])
        self._db_engine = create_engine(con_string, echo=False, pool_size=20, max_overflow=0)
        self._metadata = {}

    def get_db_engine(self):
        return self._db_engine

    def get_metadata(self, schema_name):
        return MetaData(bind=self._db_engine, schema=schema_name)

    def get_session(self):
        session = sessionmaker(bind=self._db_engine)
        return session()
