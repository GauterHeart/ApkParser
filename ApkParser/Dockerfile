FROM python:3.10


WORKDIR /code


COPY ./pyproject.toml /code/pyproject.toml


RUN pip install poetry

RUN poetry install --only main

COPY . /code
