from django.contrib import admin
from core.models.product import *



class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'amount','unit_price','discount','total_price',
                     'available', 'description', 'image')
    list_filter = ('name','available',)
    prepopulated_fields = {
        'slug': ('name',)
    }
    # readonly_fields = ('image_display',)

admin.site.register(Product, ProductAdmin),


