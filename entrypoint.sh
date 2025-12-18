#!/usr/bin/env bash

# Wait for DB to be ready (optional)
# python manage.py wait_for_db

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start server (or let docker-compose command override)
exec "$@"