from django.contrib import admin
from .models import *


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'courier', 'status', 'order_time']


class FoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'type', 'img']


class MerchantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'debt']


admin.site.register(Foods, FoodsAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Orders, OrdersAdmin)
