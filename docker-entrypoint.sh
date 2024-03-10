#!/bin/bash
db_password_from_file=`awk 'NR==1' $DB_PASSWORD_FILE`
export DB_PASSWORD=$db_password_from_file
if [ $DEBUG == "True" ]; 
then
  python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
else
  echo "to be implemented"
fi