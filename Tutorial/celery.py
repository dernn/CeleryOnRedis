import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tutorial.settings')

app = Celery('Tutorial')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_30_seconds': {  # имя периодической задачи
        # параметры периодической задачи
        'task': 'tasks.action',  # задачу вызываем из файла 'tasks.py', как и прежде
        'schedule': 30,  # периодичность
        'args': ("some_arg"),
    },
}
