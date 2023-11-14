#!/bin/sh
chmod +x entrypoint.sh
python manage.py makemigrations --noinput
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '$DJANGO_SUPERUSER_PASSWORD')"
python manage.py runserver 0.0.0.0:7777