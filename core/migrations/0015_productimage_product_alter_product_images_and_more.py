# Generated by Django 4.2.3 on 2023-07-31 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_productimage_remove_product_image_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_productimage', to='core.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='images_product', to='core.productimage'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_media'),
        ),
    ]