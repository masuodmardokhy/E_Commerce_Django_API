# Generated by Django 4.2.3 on 2023-08-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_users_create_users_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]