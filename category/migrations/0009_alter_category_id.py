# Generated by Django 4.2.2 on 2023-06-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
