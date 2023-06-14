from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount','unit_price','discount','total_price','create',
                    'update', 'available', 'description', 'image')
    list_filter = ('available',)
admin.site.register(Product, ProductAdmin),


