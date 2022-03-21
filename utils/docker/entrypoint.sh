#!/bin/sh
set -e

/wait-for-it.sh db:5432
python3 /api/src/manage.py migrate
exec python3 /api/src/manage.py runserver 0.0.0.0:8000