# Generated by Django 4.2.2 on 2023-06-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send', models.BooleanField(default=False)),
                ('products_price', models.PositiveIntegerField()),
                ('send_price', models.PositiveIntegerField()),
                ('send_price_and_total_price', models.PositiveIntegerField()),
            ],
        ),
    ]