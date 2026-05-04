"""
URL routing for the students application.

This module defines URL patterns for student-related views including
form submission, success page, and student management operations.
"""

from django.urls import path
from . import views

# App namespace for URL reversing
app_name = 'students'

urlpatterns = [
    # Student registration form
    path('', views.student_form, name='student_form'),
    path('success/<int:student_id>/', views.success, name='success'),
    
    # Student management (list, detail, update, delete)
    path('list/', views.StudentListView.as_view(), name='student_list'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
