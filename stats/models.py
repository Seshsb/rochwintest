from datetime import datetime

from django.db import models
from django.utils import timezone


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=200)
    birthdate = models.DateField('Дата Рождения', blank=True, null=True)

    def __str__(self):
        return f'Сотрудник - {self.full_name}'


class Client(models.Model):
    full_name = models.CharField('ФИО', max_length=200)
    birthdate = models.DateField('Дата Рождения', blank=True, null=True)

    def __str__(self):
        return f'Клиент - {self.full_name}'


class Product(models.Model):
    name = models.CharField('Наименование продукта', max_length=200)
    quantity = models.IntegerField('Количество')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='order')
    products = models.ManyToManyField(Product, through='OrderM2M', related_name='order_products')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='order')
    price = models.IntegerField('Общая цена', default=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.client}: {self.employee}: Дата: {self.date}'


class OrderM2M(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_m2m')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_m2m')

    def __str__(self):
        return f'{self.order} - {self.product}'
