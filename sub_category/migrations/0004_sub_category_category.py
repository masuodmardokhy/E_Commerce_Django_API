# Generated by Django 4.2.2 on 2023-06-17 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_category_id'),
        ('sub_category', '0003_alter_sub_category_id_alter_sub_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_category',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]