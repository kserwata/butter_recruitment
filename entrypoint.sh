#!/bin/bash
service postgresql start
service nginx start
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn --config gunicorn-cfg.py butter_recruitment.wsgi