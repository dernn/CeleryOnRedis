from django.urls import path
from .views import IndexView

urlpatterns = [
    # добавлять в конфигурацию проекта ('Tutorial/urls.py') не будем
    path('', IndexView.as_view()),  # путь ссылается на корень
]