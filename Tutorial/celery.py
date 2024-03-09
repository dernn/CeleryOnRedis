import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tutorial.settings')

app = Celery('Tutorial')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

#
app.conf.beat_schedule = {
    'clear_board_every_minute': {
        'task': 'mc_donalds.tasks.clear_old',
        'schedule': crontab(),  # execute every minute
    },
    # здесь может быть ещё одна таска (или несколько)
}
