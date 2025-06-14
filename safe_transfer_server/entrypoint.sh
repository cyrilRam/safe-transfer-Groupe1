#!/bin/sh
ls -al /app
echo "⏳ Attente de la base PostgreSQL..."
while ! nc -z safe-transfer-db 5432; do
  sleep 1
done

echo "✅ Base de données prête."

cd /app/safe_transfer_server/main/persistance/migrations
alembic upgrade head
python user_data_init.py
python transaction_data_init.py

cd /app/safe_transfer_server/

uvicorn main.webapi.main:app --host 0.0.0.0 --port 8080
