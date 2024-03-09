import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tutorial.settings')

app = Celery('Tutorial')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

#
app.conf.beat_schedule = {
    'print_every_5_seconds': {  # <действие>_<периодичность>
        'task': 'mc_donalds.tasks.printer',  # вызываем таску printer
        'schedule': 5,  # каждые 5 секунд
        'args': (5,),  # передаем аргумент в таску (длина счёта)
    },
    # здесь может быть ещё одна таска
}
