# Generated by Django 4.2.2 on 2023-06-22 09:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(11)]),
        ),
    ]
