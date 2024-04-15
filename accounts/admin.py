from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'status', 'is_superuser']
