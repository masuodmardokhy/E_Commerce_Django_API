from django.contrib import admin
from .models import *


class Wish_ListAdmin(admin.ModelAdmin):
    list_display = ('name','create', 'update')
    list_filter = ('name', 'create')

admin.site.register(Wish_List, Wish_ListAdmin)

