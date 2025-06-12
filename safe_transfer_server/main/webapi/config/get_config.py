import json
import os

from dotenv import load_dotenv

load_dotenv()


class ConfigurationSafeTransfer:

    @staticmethod
    def get_config_var() -> dict:
        env = os.getenv("ENV")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_conf_path = os.path.join(current_directory, 'config.json')
        with open(json_conf_path, 'r') as file:
            json_conf_dict = json.load(file)
        return json_conf_dict[env]

    @staticmethod
    def get_db_config() -> dict:
        db_var = ConfigurationSafeTransfer.get_config_var()["DataBase"]
        db_var["user"] = os.getenv("DB_USER")
        db_var["password"] = os.getenv("DB_PASSWORD")
        return db_var

# docker run --name safe-transfer-db -e POSTGRES_DB=safe-transfer -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5434:5432 -v safe-transfer-pgdata:/var/lib/postgresql/data -d postgres:15
