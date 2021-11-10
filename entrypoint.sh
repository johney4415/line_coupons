#!/bin/bash

# echo "Collect Static Files"
# python3 manage.py collectstatic --noinput

echo "Collect Static Files"
python3 manage.py collectstatic --noinput

echo "Apply Database Migrations"
python3 manage.py migrate

echo "compile language translation messages"
python3 manage.py compilemessages

echo "kill celery worker"
pkill -9 -f 'celery worker'

echo "Start Server"
nginx -g "daemon on;" && uwsgi --ini /etc/uwsgi/uwsgi.ini