FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir "/rochwintest"

WORKDIR /rochwintest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate