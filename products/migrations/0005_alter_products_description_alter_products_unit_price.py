# Generated by Django 4.2.11 on 2024-04-26 06:37

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_products_basecolour_remove_products_inventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name=builtins.max),
        ),
        migrations.AlterField(
            model_name='products',
            name='unit_price',
            field=models.IntegerField(),
        ),
    ]