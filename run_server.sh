#!/bin/sh
sleep 5
python character_builder/manage.py migrate_schemas
DJANGO_READ_DOT_ENV_FILE=True python character_builder/manage.py runserver 0.0.0.0:8000
