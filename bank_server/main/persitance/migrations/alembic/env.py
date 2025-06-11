import os
import sys

# Ajouter le dossier racine à sys.path pour que les imports fonctionnent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from bank_server.main.persitance.config.database_connection import DataBaseConnection, Base
import bank_server.main.domain.entities.user  # noqa: F401
import bank_server.main.domain.entities.account  # noqa: F401
import bank_server.main.domain.entities.transaction  # noqa: F401

# Import ta classe DataBaseConnection et ta Base SQLAlchemy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# this is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Setup Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Initialise la configuration et ta classe DataBaseConnection pour récupérer l’URL dynamique
db_conn = DataBaseConnection()

# Override la variable sqlalchemy.url avec l'URL de connexion dynamique
config.set_main_option("sqlalchemy.url", db_conn.url_db)

# Spécifie ton metadata ici pour l'autogénération des migrations
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
