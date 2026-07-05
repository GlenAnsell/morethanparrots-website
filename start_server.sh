#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
# Use caffeinate to keep Mac awake while serving
exec caffeinate -i python manage.py runserver 0.0.0.0:8001
