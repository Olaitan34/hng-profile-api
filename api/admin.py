from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'stack', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'stack')
    list_filter = ('stack', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
