#!/bin/bash
ARG SECRET_KEY
RUN mkdir /code
ADD Pipfile /code/Pipfle
ADD Pipfile.lock /code/Pipfile.lock
WORKDIR /code
# Collect static files
echo "Collect static files"
echo "begin ls"
ls
echo "end ls"
#echo "start the pipenv shell"
#pipenv shell
#cat Pipfile
echo "pipenv install begin"
pipenv install --system
echo "pipenv install end"
#export SECRET_KEY=$SECRET_KEY
echo "Starting server"

python ./character_builder/manage.py runserver 0.0.0.0:8000
