from django.contrib import admin
from core.models.delivery import *



class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('send_with_post', 'products_price','send_price',
                    'total_cost', 'create', 'update')
    list_filter = ('send_with_post',)


admin.site.register(Delivery, DeliveryAdmin),


