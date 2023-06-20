# Generated by Django 4.2.2 on 2023-06-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('image', models.ImageField(upload_to='gallery/sub_category')),
            ],
        ),
    ]