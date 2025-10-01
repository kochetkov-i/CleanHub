#!/usr/bin/env bash

source .venv/bin/activate
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 app.wsgi:application
