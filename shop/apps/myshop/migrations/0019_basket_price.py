# Generated by Django 3.1.2 on 2020-12-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0018_auto_20201205_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Ціна'),
            preserve_default=False,
        ),
    ]
