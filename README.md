docker run --name bank-db -e POSTGRES_DB=bank -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5433:5432 -v
bk-pgdata:/var/lib/postgresql/data -d postgres:15

(venv) PS C:\Users\Cyril\workspace\transition-numérique\bank_server\main\persitance\migrations> alembic revision
--autogenerate -m "Create users table bis"

alembic upgrade head  