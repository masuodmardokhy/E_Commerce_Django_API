# Generated by Django 4.2.2 on 2023-06-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category_media'),
        ),
    ]
