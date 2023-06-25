from django.contrib import admin
from core.models.sub_category import *



class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'name','slug', 'image','create','update',)
    list_filter = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Sub_Category, Sub_CategoryAdmin)

