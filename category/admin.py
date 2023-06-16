from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','update', 'create', 'slug',  'image',)    #
    list_filter = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Category, CategoryAdmin)

