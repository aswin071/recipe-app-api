from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ('id', 'email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')  # Ensure these fields exist in your User model
    # Optionally, you can add these if your User model has them:
    # filter_horizontal = ()  # If you're not using groups and permissions, this can be empty
admin.site.register(User, UserAdmin)
