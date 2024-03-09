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
# флаг -A означает application
# флаг -l и его значение INFO указывает, что именно выводить в лог консоли
# параметр --concurrency=10 указывает количество процессов, которые могут запускаться на worker'е
# флаг -B для запуска периодических задач
# (!) [WINDOWS:] в разных окнах терминала:
#
# celery -A <project_name> worker -l INFO --pool=solo
# celery -A PROJECT beat -l INFO [--pool=solo(?)]
#
# Настройки Celery позволяют создавать несколько воркеров, несколько очередей с различными маршрутизациями.
#
# Start celery worker with --purge or --discard command how to remove task from queue
#
#
