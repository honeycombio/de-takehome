#!/bin/bash
echo "Waiting for PostgreSQL to be ready..."
while ! pg_isready -h db -p 5432 -U postgres; do
  sleep 2
done
echo "PostgreSQL is ready!"

echo "Starting Flask application..."
echo "Running compiled Python application..."
cd /app && python run_app.py 