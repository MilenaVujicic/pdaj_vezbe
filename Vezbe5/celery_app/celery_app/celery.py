from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_app.settings')
app = Celery('celery_test', broker='amqp://admin:admin@queue:5672', CELERY_RESULT_BACKEND='redis://redis_db:6379')

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()