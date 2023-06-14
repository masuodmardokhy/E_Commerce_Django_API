from django.contrib import admin
from .models import *


class Shapping_CartAdmin(admin.ModelAdmin):
    list_display = ('total_price', 'total_amount')


admin.site.register(Shopping_Cart, Shapping_CartAdmin),


