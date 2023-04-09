# Generated by Django 4.1.7 on 2023-04-08 17:31

from django.db import migrations, models
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_delete_shoppinglist_foods_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='foods',
            name='items',
            field=django_jsonform.models.fields.JSONField(blank=True, null=True, verbose_name='Дополнительный'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Цена'),
        ),
    ]