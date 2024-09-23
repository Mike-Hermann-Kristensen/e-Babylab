#!/usr/bin/env bash
set -e

echo "Waiting for the database to be ready..."
./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up"

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec "$@"
