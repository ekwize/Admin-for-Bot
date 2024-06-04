FROM python:3.12

RUN pip3 install poetry

WORKDIR /app/backend

COPY entrypoint.sh /entrypoint.sh

COPY pyproject.toml poetry.lock /app/backend/

RUN poetry install --no-dev

COPY . /app/backend

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]