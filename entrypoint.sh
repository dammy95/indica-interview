#!/bin/sh

python manage.py makemigrations

python manage.py migrate --noinput

python manage.py collectstatic --noinput

gunicorn --config gunicorn_config.py api.wsgi:application
