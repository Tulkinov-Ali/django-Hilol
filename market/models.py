from django.db import models
from django_jsonform.models.fields import JSONField


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Названия')
    ParentName = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = "Категория"


class Foods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена', blank=True, null=True, default=0)
    type = models.CharField(max_length=100, verbose_name='Тип')
    img = models.ImageField(upload_to='images/', default=None, verbose_name='Картина', blank=True, null=True)

    ITEMS_SCHEMA = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'in_price': {'type': 'integer'},
                'out_price': {'type': 'integer'},
            },
            "required": ["name", "price"]
        }
    }
    items = JSONField(schema=ITEMS_SCHEMA, blank=True, null=True, verbose_name='Дополнительный')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Продукты'


class Merchant(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    debt = models.FloatField(verbose_name='Долг')

    class Meta:
        verbose_name_plural = 'Заведение'


class Orders(models.Model):
    ClientId = models.IntegerField(verbose_name='ID-клиента')
    place = models.CharField(max_length=255, verbose_name='Адресс')
    courier = models.CharField(max_length=60, verbose_name='Курьер')
    status = models.CharField(max_length=60, verbose_name='Статус')
    order_price = models.IntegerField('Стоимость заказа')
    order_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Заказы'


class Couriers(models.Model):
    name = models.CharField(max_length=56, verbose_name='Имя')
    contact = models.IntegerField(verbose_name='Контакт: (+998)')

    class Meta:
        verbose_name_plural = 'Курьеры'


class Clients(models.Model):
    name = models.CharField(max_length=60, verbose_name='Имя')
    contact = models.IntegerField(verbose_name='Контакт: (+998)')
    location = models.CharField(max_length=256, verbose_name='Адресс')
    ChatId = models.IntegerField(verbose_name='ID-чата')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name
