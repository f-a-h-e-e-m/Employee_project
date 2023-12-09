from celery import Celery
import os
import redis

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_app.settings')

app = Celery('attendance_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))