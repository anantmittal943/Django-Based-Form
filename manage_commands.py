"""
Management commands for Django Student Portal.

This file provides utility functions for data management and maintenance.

Usage:
    python manage.py shell
    >>> exec(open('manage_commands.py').read())
"""

from students.models import Student
from django.utils import timezone
import random
import string


def generate_sample_data(count=10):
    """Generate sample student data for testing."""
    first_names = ['John', 'Jane', 'Michael', 'Sarah', 'David', 'Emily', 'James', 'Jessica', 'Robert', 'Lisa']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    
    created_count = 0
    for i in range(count):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        
        # Generate unique email
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        email = f"{first_name.lower()}.{last_name.lower()}.{random_suffix}@example.com"
        
        age = random.randint(18, 30)
        
        try:
            student = Student.objects.create(
                name=name,
                email=email,
                age=age
            )
            created_count += 1
            print(f"✓ Created: {name} ({email}) - Age: {age}")
        except Exception as e:
            print(f"✗ Failed to create {name}: {str(e)}")
    
    print(f"\n✓ Successfully created {created_count} student records.")


def list_all_students():
    """List all registered students."""
    students = Student.objects.all()
    
    if not students.exists():
        print("No students found.")
        return
    
    print(f"\nTotal Students: {students.count()}\n")
    print("=" * 80)
    print(f"{'Name':<25} {'Email':<30} {'Age':<5} {'Registered':<20}")
    print("=" * 80)
    
    for student in students:
        print(f"{student.name:<25} {student.email:<30} {student.age:<5} {student.created_at.strftime('%Y-%m-%d %H:%M'):<20}")
    
    print("=" * 80)


def get_student_by_email(email):
    """Get student by email address."""
    try:
        student = Student.objects.get(email=email)
        print(f"\nStudent Found:")
        print(f"  Name: {student.name}")
        print(f"  Email: {student.email}")
        print(f"  Age: {student.age}")
        print(f"  Registered: {student.created_at}")
        print(f"  Updated: {student.updated_at}")
        return student
    except Student.DoesNotExist:
        print(f"Student with email '{email}' not found.")
        return None


def delete_student_by_email(email):
    """Delete student by email address."""
    try:
        student = Student.objects.get(email=email)
        name = student.name
        student.delete()
        print(f"✓ Deleted student: {name}")
    except Student.DoesNotExist:
        print(f"Student with email '{email}' not found.")


def get_students_by_age(age):
    """Get all students of a specific age."""
    students = Student.objects.filter(age=age)
    
    if not students.exists():
        print(f"No students found with age {age}.")
        return []
    
    print(f"\nStudents with age {age}:")
    for student in students:
        print(f"  - {student.name} ({student.email})")
    
    return list(students)


def get_average_age():
    """Get average age of all students."""
    from django.db.models import Avg
    
    avg_age = Student.objects.aggregate(Avg('age'))['age__avg']
    
    if avg_age is None:
        print("No students found.")
        return None
    
    print(f"Average age of students: {avg_age:.2f} years")
    return avg_age


def get_statistics():
    """Get statistics about registered students."""
    from django.db.models import Count, Avg, Min, Max
    
    stats = Student.objects.aggregate(
        total=Count('id'),
        avg_age=Avg('age'),
        min_age=Min('age'),
        max_age=Max('age')
    )
    
    print("\n" + "=" * 50)
    print("STUDENT STATISTICS")
    print("=" * 50)
    print(f"Total Students: {stats['total']}")
    
    if stats['total'] > 0:
        print(f"Average Age: {stats['avg_age']:.2f} years")
        print(f"Minimum Age: {stats['min_age']} years")
        print(f"Maximum Age: {stats['max_age']} years")
    
    print("=" * 50)
    
    return stats


def export_students_to_csv(filename='students.csv'):
    """Export all students to CSV file."""
    import csv
    
    students = Student.objects.all()
    
    if not students.exists():
        print("No students to export.")
        return
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Email', 'Age', 'Registered Date', 'Updated Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for student in students:
                writer.writerow({
                    'Name': student.name,
                    'Email': student.email,
                    'Age': student.age,
                    'Registered Date': student.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'Updated Date': student.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                })
        
        print(f"✓ Exported {students.count()} students to {filename}")
    except Exception as e:
        print(f"✗ Error exporting to CSV: {str(e)}")


def clear_all_students():
    """Delete all student records (use with caution!)."""
    count = Student.objects.count()
    
    if count == 0:
        print("No students to delete.")
        return
    
    confirmation = input(f"Are you sure you want to delete {count} students? (yes/no): ")
    if confirmation.lower() == 'yes':
        Student.objects.all().delete()
        print(f"✓ Deleted {count} student records.")
    else:
        print("Deletion cancelled.")


# Usage Examples:
# ===============
# In Django shell (python manage.py shell):
#
# exec(open('manage_commands.py').read())
#
# # Generate sample data
# generate_sample_data(15)
#
# # List all students
# list_all_students()
#
# # Get student by email
# get_student_by_email('john.smith@example.com')
#
# # Get students by age
# get_students_by_age(20)
#
# # Get statistics
# get_statistics()
#
# # Export to CSV
# export_students_to_csv('students_export.csv')
#
# # Get average age
# get_average_age()
#
# # Delete specific student
# delete_student_by_email('john.smith@example.com')
#
# # Clear all (dangerous!)
# clear_all_students()
