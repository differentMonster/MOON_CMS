#!/bin/bash

echo $DATABASE
echo $SQL_HOST
echo $SQL_PORT

if [ "$DATABASE" = "postgres" ]
then
    RETRIES=5

    until psql -h $SQL_HOST -U $SQL_USER -d $DATABASE -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
        echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
        sleep 1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
