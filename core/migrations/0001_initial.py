# Generated by Django 4.2.3 on 2023-07-30 08:25

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_media')),
                ('sub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='core.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=20)),
                ('send_price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('unit_price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(null=True, upload_to='product_media')),
                ('color', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('user_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(11)])),
                ('password', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('user_image', models.ImageField(null=True, upload_to='user_image_media')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wish_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('wishDate', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('cart_items', models.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('rate', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.users'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('total_price', models.PositiveIntegerField()),
                ('total_amount_product', models.PositiveIntegerField(default=0)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(11)])),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('delivery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='core.delivery')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('comment', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=40)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField()),
                ('cart_image', models.ImageField(null=True, upload_to='cart_item_media')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='core.order')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items_user', to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='core.users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
                ('stat', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('zipCode', models.CharField(max_length=20)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='core.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
