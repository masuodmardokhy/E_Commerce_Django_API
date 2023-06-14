from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'slug', 'update', 'image',)
    list_filter = ('name',)

admin.site.register(Category, CategoryAdmin)

