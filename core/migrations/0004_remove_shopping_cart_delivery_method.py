# Generated by Django 4.2.3 on 2023-07-25 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_delivery_id_shopping_cart_delivery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='delivery_method',
        ),
    ]
