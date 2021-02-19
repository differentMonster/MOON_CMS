#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    RETRIES=5

    until psql -h $SQL_HOST -U $SQL_USER -d $DATABASE -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
        echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
        sleep 1
    done

    echo "PostgreSQL started"
fi

exec "$@"
