"""
Admin configuration for the students application.

This module customizes the Django admin interface for managing Student records.
"""

from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Student model.
    
    Provides enhanced interface for viewing and managing student records
    with list display, search, filtering, and readonly fields.
    """
    
    # Columns displayed in the list view
    list_display = [
        'name',
        'email',
        'age',
        'created_at',
        'updated_at',
    ]
    
    # Enable searching by name and email
    search_fields = [
        'name',
        'email',
    ]
    
    # Enable filtering by age and creation date
    list_filter = [
        'age',
        'created_at',
        'updated_at',
    ]
    
    # Fields to display in the detailed view
    fields = [
        'name',
        'email',
        'age',
        'created_at',
        'updated_at',
    ]
    
    # Read-only fields (cannot be edited)
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
    
    # Order students by creation date (newest first)
    ordering = ['-created_at']
    
    # Items per page in list view
    list_per_page = 25
    
    # Date hierarchy for quick filtering
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        """Allow adding new students through admin."""
        return True
    
    def has_change_permission(self, request, obj=None):
        """Allow editing existing students through admin."""
        return True
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting students through admin."""
        return True
    
    def has_view_permission(self, request, obj=None):
        """Allow viewing students through admin."""
        return True

