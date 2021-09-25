# Generated by Django 3.1.2 on 2020-10-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_auto_20201004_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='battery_characteristics',
            field=models.CharField(default=0, max_length=30, verbose_name='Характеристики батареи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laptop',
            name='network_adapters',
            field=models.CharField(default=0, max_length=40, verbose_name='Сетевые адаптеры'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laptop',
            name='processor',
            field=models.CharField(default=0, max_length=40, verbose_name='Процесор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laptop',
            name='scr_diagonal',
            field=models.FloatField(default=0, max_length=10, verbose_name='Диагональ экрана'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laptop',
            name='scr_refresh',
            field=models.CharField(default=0, max_length=20, verbose_name='Частота обновления экрана'),
            preserve_default=False,
        ),
    ]