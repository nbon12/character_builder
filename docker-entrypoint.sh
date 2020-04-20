#!/bin/bash

# Collect static files
echo "Collect static files"
ls
#pipenv install --dev
pipenv shell
#python ./character_builder/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
#python ./character_builder/manage.py migrate

# Start server
echo "Starting server"

#python ./character_builder/manage.py runserver 0.0.0.0:8000