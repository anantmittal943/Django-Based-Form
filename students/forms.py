"""
Forms for the students application.

This module defines forms used for collecting and validating student information.
"""

from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    """
    Form for creating and updating Student records.
    
    This form is based on the Student model and provides fields for
    entering student information with Django-provided validation.
    """
    
    class Meta:
        """
        Meta options for StudentForm.
        """
        model = Student
        fields = ['name', 'email', 'age']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter valid email address',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age (5-100)',
                'type': 'number',
                'min': 5,
                'max': 100,
                'required': True
            }),
        }
        
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'age': 'Age',
        }
        
        help_texts = {
            'name': 'Enter the student\'s full name',
            'email': 'Enter a valid email address',
            'age': 'Age must be between 5 and 100',
        }
    
    def clean_name(self):
        """Validate that name is not empty and remove extra whitespace."""
        name = self.cleaned_data.get('name', '').strip()
        
        if not name:
            raise forms.ValidationError('Name cannot be empty.')
        
        if len(name) < 2:
            raise forms.ValidationError('Name must be at least 2 characters long.')
        
        return name
    
    def clean_age(self):
        """Validate age range."""
        age = self.cleaned_data.get('age')
        
        if age is not None:
            if age < 5:
                raise forms.ValidationError('Age must be at least 5.')
            if age > 100:
                raise forms.ValidationError('Age cannot exceed 100.')
        
        return age
    
    def clean_email(self):
        """Validate email uniqueness for new instances."""
        email = self.cleaned_data.get('email', '').lower()
        
        # Check if email already exists (excluding current instance in update)
        if self.instance.pk:
            # Update case: exclude current instance
            if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('This email address is already in use.')
        else:
            # Create case
            if Student.objects.filter(email=email).exists():
                raise forms.ValidationError('This email address is already in use.')
        
        return email
