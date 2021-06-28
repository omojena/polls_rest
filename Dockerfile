FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY pyproject.toml /code/
RUN poetry install
COPY . /code/