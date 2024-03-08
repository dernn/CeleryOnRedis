# redislabs.com / registration in the cloud service (VPN required)
# Endpoint (database) --> Celery settings[.py]

"""Установка библиотеки и обновление (ключ -U) всех требований Celery / Redis"""
# pip install redis
# pip install -U "celery[redis]"

# В одном терминале запустить Django:
# python manage.py runserver
#
# А в другом — запустить Celery:
# celery -A <project_name> worker -l INFO --pool=solo
# (!) <project_name> здесь каталог конфигурации проекта (где settings.py etc.)
#
# Start celery worker with --purge or --discard command how to remove task from queue
#
#
