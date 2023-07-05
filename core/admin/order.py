from django.contrib import admin
from core.models.order import *



class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity','price','address','phone','date',
                    'status')
    list_filter = ('name',)
admin.site.register(Order, OrderAdmin),

