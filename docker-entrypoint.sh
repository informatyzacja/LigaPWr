#!/bin/bash
db_password_from_file=`awk 'NR==1' $DB_PASSWORD_FILE`
export DB_PASSWORD=$db_password_from_file
python manage.py collectstatic --noinput
cp -R -f ligapwr/static/ /var/www/static
cp -R -f staticfiles/. /var/www/static/static
if [ $DEBUG == "True" ]; 
then
  python3 manage.py add_dummy_data
  python3 manage.py migrate
  python3 manage.py runserver 0.0.0.0:8000
else
  python3 manage.py migrate
  exec gunicorn \
      --preload \
      --bind 0.0.0.0:8000 \
      --name app \
      --workers 3 \
      -k uvicorn.workers.UvicornWorker \
      --forwarded-allow-ips="*" \
      --log-level=debug \
      --capture-output --enable-stdio-inheritance \
      --access-logfile '-' --error-logfile '-' \
      ligapwrproject.asgi:application
fi