from django.contrib import admin
from core.models.users import *



class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email', 'phone', 'password','create', 'update')
    list_filter = ('first_name', 'last_name', 'create')

admin.site.register(Users, UsersAdmin)

