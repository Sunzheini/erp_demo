web: gunicorn erp_demo.wsgi
release: python manage.py migrate
release: python manage.py collectstatic --noinput
