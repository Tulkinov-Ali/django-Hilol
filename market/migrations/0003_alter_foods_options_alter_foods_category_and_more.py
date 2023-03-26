# Generated by Django 4.1.7 on 2023-03-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_foods_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foods',
            options={'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterField(
            model_name='foods',
            name='category',
            field=models.CharField(choices=[('ichimlik', 'ichimlik'), ('oziq-ovqat', 'oziq-ovqat'), ('shirinlik', 'shirinlik'), ('sut-maxsulotlari', 'sut-maxsulotlari')], max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='img',
            field=models.ImageField(default=None, upload_to='images/', verbose_name='Картина'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='type',
            field=models.CharField(choices=[('1-Dona', '1-Dona'), ('Kg', 'Kg'), ('Ltr', 'Ltr'), ('blok', 'blok')], max_length=100, verbose_name='Тип'),
        ),
    ]