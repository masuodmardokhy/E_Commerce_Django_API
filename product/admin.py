from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'amount','unit_price','discount','total_price',
                     'available', 'description', 'image')  # 'name','update','create',
    list_filter = ('available',)
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Product, ProductAdmin),


