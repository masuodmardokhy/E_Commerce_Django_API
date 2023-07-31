# Generated by Django 4.2.3 on 2023-07-31 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_cart_item_order_alter_cart_item_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_category', to='core.users'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='core.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to='core.users'),
        ),
    ]
