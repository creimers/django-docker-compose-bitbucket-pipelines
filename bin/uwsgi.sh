#!/bin/sh
python /project/manage.py collectstatic --noinput
/usr/local/bin/uwsgi /project/etc/uwsgi.ini
