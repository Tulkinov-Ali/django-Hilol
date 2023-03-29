from django.db import models

turlari = (('1-Dona', '1-Dona'),
           ('Kg', 'Kg'),
           ('Ltr', 'Ltr'),
           ('blok', 'blok')
           )


class AllCategories(models.Model):
    name = models.CharField(max_length=60, verbose_name='Названия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ' Родительская-Категория'


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Названия')
    ParentName = models.ForeignKey(AllCategories, verbose_name='Родитель', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Дочерная-Категория'


class Foods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
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
