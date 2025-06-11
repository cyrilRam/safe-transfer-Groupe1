#!/bin/sh
ls -al /app
echo "⏳ Attente de la base PostgreSQL..."
while ! nc -z bank-db 5432; do
  sleep 1
done

echo "✅ Base de données prête."

cd /app/bank_server/main/persitance/migrations
alembic upgrade head
python user_data_init.py
python account_data_init.py
python transaction_data_init.py

cd /app/bank_server/

uvicorn main.webapi.main:app --host 0.0.0.0 --port 8080
