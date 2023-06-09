from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class OrdersAdmin(admin.ModelAdmin):
    search_fields = ['id', 'place', 'courier', 'status']
    list_display = ['id', 'place', 'courier', 'status', 'order_time']


class MerchantAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', 'debt']
    list_display = ['id', 'name', 'debt']


class CtgAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ParentName']
    list_display = ['id', 'name', 'ParentName']


class CourierAdmin(admin.ModelAdmin):
    search_fields = ['name', 'contact']
    list_display = ['id', 'name', 'contact']


class ClientsAdmin(admin.ModelAdmin):
    search_fields = ['name', 'contact', 'ChatId']
    list_display = ['id', 'name', 'contact', 'location', 'ChatId', 'date']


class FoodsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReportResource
    search_fields = ['id', 'name', 'category', 'price', 'type', 'img']
    list_display = ['id', 'name', 'category', 'price', 'type', 'img', 'items']


admin.site.register(Foods, FoodsAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Couriers, CourierAdmin)
admin.site.register(Category, CtgAdmin)
