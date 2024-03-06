from django.test import TestCase

# Create your tests here.

fullName = 'Ivanov Ivan Ivanovich'
lastName = fullName.split()[0]
print(lastName)
# trigger = True
camelCase = ''.join()


if fullName:
    lastName = fullName.split()[1]
    lastName.isalpha()

print(lastName)


class Product:
    _amount = 1

    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0


testProduct = Product(5)
print(testProduct.amount)

testProduct.amount = 7
print(testProduct.amount)

print(Product.amount)