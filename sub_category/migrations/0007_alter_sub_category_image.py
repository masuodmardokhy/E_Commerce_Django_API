# Generated by Django 4.2.2 on 2023-06-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_category', '0006_alter_sub_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='image',
            field=models.ImageField(upload_to='sub_category_media'),
        ),
    ]
