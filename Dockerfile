FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir "/rochwintest"

WORKDIR /rochwintest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "migrate"]

# Запускаем Django-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:7777"]
