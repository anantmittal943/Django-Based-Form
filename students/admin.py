from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'age',
        'created_at',
        'updated_at',
    ]
    
    search_fields = [
        'name',
        'email',
    ]
    
    list_filter = [
        'age',
        'created_at',
        'updated_at',
    ]
    
    fields = [
        'name',
        'email',
        'age',
        'created_at',
        'updated_at',
    ]
    
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
    
    ordering = ['-created_at']
    
    list_per_page = 25
    
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def has_view_permission(self, request, obj=None):
        return True

