from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    # ...
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name')
    filter_horizontal = ()
    list_filter = ('groups',)
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)