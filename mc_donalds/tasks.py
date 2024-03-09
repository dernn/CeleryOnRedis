from celery import shared_task
import time

from mc_donalds.models import Order


@shared_task
def complete_order(oid):
    order = Order.objects.get(pk=oid)
    order.complete = True
    order.save()


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i + 1)
