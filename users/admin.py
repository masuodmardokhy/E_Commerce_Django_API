from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'password',)
    list_filter = ('first_name', 'last_name')

admin.site.register(Users, UsersAdmin)

