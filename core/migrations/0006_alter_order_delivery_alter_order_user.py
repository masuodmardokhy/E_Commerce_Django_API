# Generated by Django 4.2.3 on 2023-07-31 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_cart_item_product_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_order', to='core.delivery'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to='core.users'),
        ),
    ]
