#!/bin/bash
python manage.py makemigrations users
echo "initializing django migration"
python manage.py migrate
echo "django migration finished"
python ./add_userdata.py
echo "data migration finished"
gunicorn core_backend.wsgi --bind 0.0.0.0:8000
