from bank_server.main.persitance.config.database_connection import DataBaseConnection


class DbDependency:
    @staticmethod
    def get_db_session():
        db = DataBaseConnection()
        yield from db.get_session()
