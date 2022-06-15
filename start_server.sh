#!/usr/bin/env bash
export DEBUG=false
python manage.py migrate
python manage.py loaddata seeddata.json
chmod -R 777 db
chown -R www-data:www-data db
python ./manage.py collectstatic
mkdir /home/staticfiles
mv static_root/* /home/staticfiles
rm -rf static_root/
gunicorn app.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3 --timeout 300
