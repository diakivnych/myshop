# Generated by Django 3.1.2 on 2020-11-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0010_auto_20201018_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='count_in_stock',
            field=models.IntegerField(default=1, verbose_name='Количество на складе'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphone',
            name='count_in_stock',
            field=models.IntegerField(default=1, verbose_name='Количество на складе'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laptop',
            name='battery_characteristics',
            field=models.CharField(max_length=50, verbose_name='Характеристики батареи'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='color',
            field=models.CharField(max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Страна-производитель товара'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='network_adapters',
            field=models.CharField(max_length=50, verbose_name='Сетевые адаптеры'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='processor',
            field=models.CharField(max_length=50, verbose_name='Процесор'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='scr_refresh',
            field=models.CharField(max_length=50, verbose_name='Частота обновления экрана'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='warranty',
            field=models.CharField(max_length=50, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='color',
            field=models.CharField(max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Страна-производитель товара'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='display_res',
            field=models.CharField(max_length=50, verbose_name='Разрешение экрана'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='os',
            field=models.CharField(max_length=50, verbose_name='Операционная система'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='scr_material',
            field=models.CharField(max_length=50, verbose_name='Материал экрана'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='warranty',
            field=models.CharField(max_length=50, verbose_name='Гарантия'),
        ),
    ]
