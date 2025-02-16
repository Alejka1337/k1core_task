#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py loaddata app/fixtures/currencies_providers.json

if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py createsuperuser --noinput
fi

exec "$@"