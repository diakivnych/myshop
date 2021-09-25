# Generated by Django 3.1.2 on 2020-10-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20201004_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название товара')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('country', models.CharField(max_length=40, verbose_name='Страна-производитель товара')),
                ('warranty', models.CharField(max_length=40, verbose_name='Гарантия')),
                ('color', models.CharField(max_length=40, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Смартфон',
                'verbose_name_plural': 'Смартфоны',
            },
        ),
        migrations.AlterModelOptions(
            name='laptop',
            options={'verbose_name': 'Ноутбук', 'verbose_name_plural': 'Ноутбуки'},
        ),
    ]
