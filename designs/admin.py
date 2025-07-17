# admin.py
from django.contrib import admin
from .models import Profile, Design

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['user__username']

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ['name', 'design_type', 'creator', 'created_at']
