#!/bin/bash

poetry run alembic upgrade head

poetry run python3 createsuperadmin.py &

poetry run python3 admin/main.py &

poetry run python3 bot/main.py

