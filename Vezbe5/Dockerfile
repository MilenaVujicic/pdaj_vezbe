FROM python:3.8

WORKDIR /usr/src

RUN apt update
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY celery_app/ .

CMD python manage.py runserver 0.0.0.0:8000