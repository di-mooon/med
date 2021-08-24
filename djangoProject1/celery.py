import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')



app = Celery('djangoProject1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


