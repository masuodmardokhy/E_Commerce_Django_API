# Generated by Django 4.2.2 on 2023-06-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_shopping_cart_create_shopping_cart_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]