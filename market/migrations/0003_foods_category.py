# Generated by Django 4.1.7 on 2023-03-29 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_allcategories_clients_couriers_merchant_orders_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='market.category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]