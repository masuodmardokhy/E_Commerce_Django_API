from django.contrib import admin
from .models import *


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('send', 'products_price','send_price','send_price_and_total_price',)
    list_filter = ('send_price',)


admin.site.register(Delivery, DeliveryAdmin),


