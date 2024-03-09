from datetime import datetime

from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .models import Order
from .tasks import complete_order


# главная страница - таблица заказов
class IndexView(TemplateView):
    template_name = "board/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        return context


# форма нового заказа
class NewOrderView(CreateView):
    model = Order
    fields = ['products']  # единственное поле
    template_name = 'board/new.html'

    # после валидации формы, сохраняем объект,
    # считаем его общую стоимость
    # и вызываем задачу "завершить заказ" через минуту после вызова
    def form_valid(self, form):
        order = form.save()
        order.cost = sum([prod.price for prod in order.products.all()])
        order.save()
        # в аргументы задачи не рекомендуется передавать объекты модели напрямую
        complete_order.apply_async([order.pk], countdown=60)  # вместо этого ID или параметры
        # redirect без '/' перед GET-параметром (пр. 'board/') добавляет значение к текущей GET-позиции
        return redirect('/board/')


# представление для "кнопки", чтобы можно было забрать заказ
def take_order(request, oid):
    order = Order.objects.get(pk=oid)
    order.time_out = datetime.now()
    order.save()
    return redirect('/board/')
