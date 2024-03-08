from datetime import datetime, timedelta, timezone

from django.http import HttpResponse
from django.views import View
from .tasks import hello, printer


class IndexView(View):
    def get(self, request):
        # передаем аргумент для функции-задачи через apply_async()
        printer.apply_async([10],
                            # now() required timezone.utc for correct working
                            eta=datetime.now(timezone.utc) + timedelta(seconds=10)
                            # убирает задачу из очереди по прошествии какого-то времени
                            # expires=<datetime.object or number>
                            )
        hello.delay()
        return HttpResponse('Hello!')
