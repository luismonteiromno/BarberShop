release: python manage.py collectstatic --noinput
web: gunicorn barbershop.wsgi:application --log-file -
