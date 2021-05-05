FROM python:3.6.6-alpine3.7

RUN pip install poetry

COPY ../. /home/project

WORKDIR /home/project
RUN poetry install
