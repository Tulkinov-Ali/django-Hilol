from django.db import models

types = (('ichimlik', 'ichimlik'),
         ('oziq-ovqat', 'oziq-ovqat'),
         ('shirinlik', 'shirinlik'),
         ('sut-maxsulotlari', 'sut-maxsulotlari')
         )
turlari = (('1-Dona', '1-Dona'),
           ('Kg', 'Kg'),
           ('Ltr', 'Ltr'),
           ('blok', 'blok')
           )


class Foods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    category = models.CharField(max_length=100, choices=types, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    type = models.CharField(max_length=100, choices=turlari, verbose_name='Тип')
    img = models.ImageField(upload_to='images/', default=None, verbose_name='Картина', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Продукты'



class Merchant(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    debt = models.FloatField(verbose_name='Долг')

    class Meta:
        verbose_name_plural = 'Заведение'


class Orders(models.Model):
    place = models.CharField(max_length=255)
    courier = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    order_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Заказы'

