"""
Student model for the students application.

This module defines the Student model for storing student information
including name, email, and age with timestamp tracking.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Student(models.Model):
    """
    Student model to store student information.
    
    Attributes:
        name: Student's full name (max 100 characters)
        email: Student's email address (unique)
        age: Student's age (between 5 and 100)
        created_at: Timestamp when student record was created
        updated_at: Timestamp when student record was last updated
    """
    
    name = models.CharField(
        max_length=100,
        verbose_name='Full Name',
        help_text='Enter the student\'s full name'
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name='Email Address',
        help_text='Enter a valid email address'
    )
    
    age = models.IntegerField(
        validators=[
            MinValueValidator(5, 'Age must be at least 5'),
            MaxValueValidator(100, 'Age cannot exceed 100')
        ],
        verbose_name='Age',
        help_text='Enter student\'s age (between 5 and 100)'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )
    
    class Meta:
        """
        Meta options for the Student model.
        """
        ordering = ['-created_at']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        """Return the string representation of the student."""
        return f"{self.name} ({self.email})"
    
    def __repr__(self):
        """Return the developer-friendly representation of the student."""
        return f"<Student: {self.name} - {self.email}>"

