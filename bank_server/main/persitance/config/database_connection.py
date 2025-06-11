from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base

from bank_server.main.webapi.config.get_config import Configuration

Base = declarative_base()


class DataBaseConnection:
    def __init__(self):
        db_var = Configuration.get_db_config()
        self.url_db = f"postgresql://{db_var['user']}:{db_var['password']}@{db_var['db_host']}:{db_var['db_port']}/{db_var['db_name']}"
        engine = create_engine(self.url_db)
        self.local_session_creation = sessionmaker(autoflush=False, autocommit=False, bind=engine)

    def get_session(self):
        local_session = self.local_session_creation()
        try:
            local_session.execute(text('select 1'))
            yield local_session
        except OperationalError as e:
            raise e
        finally:
            if local_session:
                local_session.close()
