from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_form, name='student_form'),
    path('success/<int:student_id>/', views.success, name='success'),
    
    path('list/', views.StudentListView.as_view(), name='student_list'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
