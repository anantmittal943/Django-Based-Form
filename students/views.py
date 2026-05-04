import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Student
from .forms import StudentForm

logger = logging.getLogger(__name__)


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                student = form.save()
                logger.info(f"Student created successfully: {student.email}")
                messages.success(
                    request,
                    f'Welcome, {student.name}! Your information has been recorded.'
                )
                return redirect('success', student_id=student.id)
            except Exception as e:
                logger.error(f"Error saving student form: {str(e)}")
                messages.error(
                    request,
                    'An error occurred while saving your information. Please try again.'
                )
        else:
            logger.warning(f"Form validation errors: {form.errors}")
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    
    context = {
        'form': form,
        'page_title': 'Student Registration Form',
    }
    return render(request, 'students/form.html', context)


def success(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        context = {
            'student': student,
            'page_title': 'Registration Successful',
        }
        return render(request, 'students/success.html', context)
    except Student.DoesNotExist:
        logger.error(f"Student with ID {student_id} not found")
        messages.error(request, 'Student record not found.')
        return redirect('student_form')


class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10
    
    def get_queryset(self):
        return Student.objects.all().order_by('-created_at')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'pk'


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    pk_url_kwarg = 'pk'
    success_message = "Student information updated successfully!"
    
    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.pk})


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('student_list')
    success_message = "Student record deleted successfully!"

