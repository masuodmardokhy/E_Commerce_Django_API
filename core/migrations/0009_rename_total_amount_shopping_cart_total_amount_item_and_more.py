# Generated by Django 4.2.2 on 2023-07-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_shopping_cart_user_alter_cart_item_shopping_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopping_cart',
            old_name='total_amount',
            new_name='total_amount_item',
        ),
        migrations.AddField(
            model_name='shopping_cart',
            name='total_amount_product',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
