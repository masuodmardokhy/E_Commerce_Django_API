# Generated by Django 4.2.2 on 2023-06-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0005_alter_shopping_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]