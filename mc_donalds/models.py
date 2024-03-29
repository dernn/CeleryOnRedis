# импорт
from django.db import models
from datetime import datetime


class Order(models.Model):  # наследуемся от класса Model
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='orders', default=4)
    products = models.ManyToManyField('Product', through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    # 5.6.2
    def get_duration(self):
        if self.complete:  # если завершён, возвращаем разность объектов
            return (self.time_out - self.time_in).total_seconds()  # // 60
        else:  # если ещё нет, то сколько длится выполнение
            return (datetime.now() - self.time_in).total_seconds()  # // 60
            # USE_TZ, settings: сохраняет таймзону для DateTimeField (self.time_in, self.time_out), если True
            # datetime.now() не возвращает таймзону, USE_TZ лучше взять False


class Product(models.Model):
    name = models.CharField(max_length=255)  # NOT NULL по умолчанию, иначе null=True
    price = models.FloatField(default=0.0)
    composition = models.TextField(default="Composition not specified")

    def __str__(self):
        return self.name + "/" + str(self.price)


class Staff(models.Model):
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    POSITIONS = [
        (director, 'Director'),
        (admin, 'Administrator'),
        (cook, 'Cook'),
        (cashier, 'Cashier'),
        (cleaner, 'Cleaner')
    ]

    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)
    labor_contract = models.IntegerField()

    # 5.6.1
    def get_last_name(self):
        # возвращает фамилию сотрудника (если маска ФИО)
        return self.full_name.split()[0]


class ProductOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    _amount = models.IntegerField(default=1, db_column='amount')

    def product_sum(self):
        product_price = self.product.price
        return product_price * self._amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()
