from django.contrib import admin
from core.models.category import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','update', 'create', 'slug',  'image',)    #
    list_filter = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Category, CategoryAdmin)

