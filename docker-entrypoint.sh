#!/bin/bash
db_password_from_file=`awk 'NR==1' $DB_PASSWORD_FILE`
export DB_PASSWORD=$db_password_from_file
python3 manage.py migrate
python manage.py collectstatic --noinput
if [ $DEBUG == "True" ]; 
then
   python3 manage.py runserver 0.0.0.0:8000
else
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