# base image
FROM python:3.9.5-slim


# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#  work directory
WORKDIR /code

COPY poetry.lock pyproject.toml /code/

RUN pip3 install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction


# Copy project
COPY . /code/
