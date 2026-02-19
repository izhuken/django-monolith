#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn server.wsgi:application --bind 0.0.0.0:4000 --workers 4