from django.contrib import admin
from .models import *


class Cart_ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount','price')
    list_filter = ('name',)

admin.site.register(Cart_Item, Cart_ItemAdmin),


