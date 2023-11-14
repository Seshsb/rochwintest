FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir "/rochwintest"

WORKDIR /rochwintest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '$DJANGO_SUPERUSER_PASSWORD')"

CMD ["python", "manage.py", "runserver", "0.0.0.0:7777"]
