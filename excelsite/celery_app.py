from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excelsite.settings')
app=Celery('excelsite')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()

