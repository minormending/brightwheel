FROM python:3.11-slim

RUN pip install poetry
RUN poetry config virtualenvs.create false

RUN mkdir /app
COPY pyproject.toml /app
WORKDIR /app

COPY README.md /app 
RUN mkdir /app/brightwheel
COPY brightwheel /app/brightwheel
RUN poetry install --no-dev

ENTRYPOINT [ "brightwheel-export" ]