# Product
cap = Product(name='Cappuccino 0.3', price=99.0)
cap.save()

# objects.create() создаёт и сохраняет объект в БД
# objects - менеджер модели
cap_big = Product.objects.create(name='Cappuccino 0.4', price=109.0)

# 5.7.1
fries_small = Product(name='Fries Small', price=93.0)
fries_small.save()

fries_mid = Product.objects.create(name='Fries Medium', price=106.0)

# Staff + Django Shell
cashier1 = Staff.objects.create(full_name='Ivanov Ivan Ivanovich',
                                position='CA',
                                labor_contract=1754)
cashier2 = Staff.objects.create(full_name="Petrov Petr Petrovich",
                                position=cashier,
                                labor_contract=4355)
direct = Staff.objects.create(full_name='Maximov Maxim Maximovich',
                              position=director,
                              labor_contract=1254)
admin = Staff.objects.create(full_name='Egorov Egor Egorovich',
                             position=admin,
                             labor_contract=5755)

# Search: получение объектов модели, метод get
# python manage.py shell

from mc_donalds.resources import *
from mc_donalds.models import Staff
from mc_donalds.models import Product

person = Staff.objects.get(labor_contract=1254)
Staff.objects.get(pk=4).full_name
person.full_name  # 5.7.2
person.position  # 5.7.3

# get_<название поля>_display()
person.get_position_display()  # 5.7.4: возвращает значение ячейки

# get, filter, all(), __gt == (greater than): аналоги SELECT * FROM WHERE
Staff.objects.get(position=Staff.cashier)  # get() returned more than one Staff
Staff.objects.filter(position='CA')  # возвращает <QuerySet>
Product.objects.filter(price__gt=100)
Product.objects.filter(price__gt=90.0).values('name')
Product.objects.all()  # возвращает <QuerySet> всех объектов
# возвращает <QuerySet> объектов-словарей с ключами [values]
Product.objects.all().values('name', 'price')  # 5.7.7

# QuerySet to list of dict [{}, {}, ...] / values()
Staff.objects.get(position=Staff.cashier)
Staff.objects.get(position='DI')
cashiers = Staff.objects.filter(position=Staff.cashier)  # запись в переменную
cashiers.values('full_name', 'labor_contract')

from mc_donalds.models import Order

Order.objects.create(staff=cashier1, take_away=False)
Order.objects.create(staff=cashier2, take_away=True)
Order.objects.create(staff=cashier1, take_away=True)

cashier1 = Staff.objects.get(pk=1)
cashier2 = Staff.objects.get(pk=2)

# Фильтр по полям связанной модели
# staff__labor_contract: <model>__<название поля>

# Используя двойное подчёркивание [__, 'дандр'], можно выводить поле связанного объекта модели.
# В многоступенчатых связях можно создавать цепочки связанных фильтров, используя '__' между полями моделей.
Order.objects.filter(staff__labor_contract=1754).values("staff__full_name", "take_away")

# exists()
# Returns True if the QuerySet contains any results, and False if not.
from mc_donalds.models import ProductOrder

ProductOrder.objects.all()
ProductOrder.objects.all().exists()
Product.objects.all().exists()

# order_by()
Product.objects.all().order_by('price').values('name', 'price')  # ASC: возрастание
Product.objects.all().order_by('-price').values('name', 'price')  # ('-price') / DESC: убывание

# 5.7.8
Author.objects.filter(age__lt=25)  # фильтр модели Author, где age меньше (__lt) 25

# Practice 18.06 D5.7
Staff.objects.all().first()
ca = Staff.objects.all().first()
order = Order.objects.create(staff=ca)  # готовую сущность модели Order можно получить через get()
order.get_duration()  # возвращает время в секундах от создания заказа
order.finish_order()

Product.objects.all()
prod1 = Product.objects.all()[0]
prod2 = Product.objects.all()[2]
# products - поле ManyToManyField модели Order
order.products.add(prod1)  # добавляем объект prod1 в таблицу (модель) ProductOrder через поле products
order.products.add(prod2)  # создаёт новую запись в таблице PoductOrder
order.products.all()  # возвращет <QuerySet> всех связанных объектов из таблицы PoductOrder
order.products.all().values('name', 'price')
ca.order_set.all()  # автоматически созданный атрибут order_set к связи "один-ко-многим" модели Order
ca.orders.all()  # переписали related_name в Order.staff (ForeignKey)

# 5.8.5
Author.objects.filter(age=32).values("name")  # обязательно двойные кавычки для <name>

from django.db import models
type(ca.orders.all().values('cost').aggregate(models.Sum('cost')))  # dict: доступны все методы словаря
ca.orders.all().values('cost').aggregate(models.Sum('cost'))  # возвращает сумму всех костов
ca.orders.all().values('cost').aggregate(models.Sum('cost')).get('cost__sum')  # возвращает value ключа 'cost__sum'
type(ca.orders.all().values('cost').aggregate(models.Sum('cost')).get('cost__sum'))  # float
ca.orders.all().values('cost').aggregate(models.Sum('cost'))['cost__sum']  # то же, что и get('cost__sum')
type(ca.orders.all().values('cost').aggregate(models.Sum('cost'))['cost__sum'])  # float
ca.orders.all().aggregate(models.Sum('cost')).get('cost__sum')  # можно и без values()
ca.orders.all().aggregate(models.Sum('cost'))['cost__sum']
dir(ca)  # dir: возвращает все атрибуты объекта и связанные с ним атрибуты в виде списка
dict.fromkeys()  # можно сделать словарь из dir(ca)
