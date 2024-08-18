release: python manage.py collectstatic --noinput
web: gunicorn barbershop.wsgi:application --bind 0.0.0.0:$PORT

