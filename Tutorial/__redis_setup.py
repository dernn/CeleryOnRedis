# redislabs.com / registration in the cloud service (VPN required)
# Endpoint (database) --> Celery settings[.py]

"""Установка библиотеки и обновление (ключ -U) всех требований Celery / Redis"""
# pip install redis
# pip install -U "celery[redis]"

# В одном терминале запустить Django:
# python manage.py runserver
#
# А в другом — запустить Celery:
# celery --pool=solo -A proj_name worker -l INFO