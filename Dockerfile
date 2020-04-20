FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./Pipfile /code
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev

COPY . /code/
ENTRYPOINT ["/code/docker-entrypoint.sh"]