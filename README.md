# Django Student Portal

A professional Django-based web application for managing student registration and information. This project follows Django best practices and the Model-View-Template (MVT) architectural pattern.

## Features

- **Student Registration**: Easy-to-use form for registering new students
- **Data Validation**: Comprehensive validation for all form fields
- **Student Management**: View, edit, and delete student records
- **Admin Interface**: Django admin panel for administrative tasks
- **Responsive Design**: Mobile-friendly user interface
- **Professional Code Structure**: Clean, well-documented codebase
- **Database**: SQLite (development) with PostgreSQL support for production
- **Security**: CSRF protection, input validation, and secure form handling

## Project Structure

```
Django-Based-Form/
├── .venv/                    # Python virtual environment
├── .env                      # Environment variables (local)
├── .gitignore               # Git ignore rules
├── manage.py                # Django management script
├── requirements.txt         # Project dependencies
├── README.md               # This file
│
├── studentportal/          # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   ├── asgi.py            # ASGI configuration
│   └── wsgi.py            # WSGI configuration
│
└── students/              # Main application
    ├── models.py          # Student model definition
    ├── forms.py           # Student registration form
    ├── views.py           # Views for handling requests
    ├── urls.py            # App-specific URL routing
    ├── admin.py           # Admin interface configuration
    ├── apps.py            # App configuration
    ├── migrations/        # Database migrations
    └── templates/         # HTML templates
        └── students/
            ├── form.html                # Registration form template
            ├── success.html             # Success page template
            ├── student_list.html        # Student list template
            ├── student_detail.html      # Student detail template
            ├── student_form.html        # Update form template
            └── student_confirm_delete.html # Deletion confirmation
```

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
cd Django-Based-Form
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Copy `.env` file contents or create a `.env` file with:

```env
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
SECRET_KEY=your-secret-key-here
```

2. Generate a new SECRET_KEY:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Apply Migrations

```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account with username, email, and password.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Registration Form

Navigate to `http://127.0.0.1:8000/` to access the student registration form.

**Form Fields:**
- **Name**: Student's full name (required)
- **Email**: Valid email address (required, must be unique)
- **Age**: Student's age (5-100 years)

### Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/`

**Features:**
- View all registered students
- Add new students
- Edit student information
- Delete student records
- Search by name or email
- Filter by age and registration date

### Student List

View all registered students at `http://127.0.0.1:8000/students/list/`

### Student Management

- **View Details**: Click "View" button in the student list
- **Edit**: Click "Edit" button or use `/students/update/<id>/`
- **Delete**: Click "Delete" button or use `/students/delete/<id>/`

## API Endpoints

```
GET  /                          # Registration form
POST /                          # Submit registration
GET  /success/<student_id>/     # Success page
GET  /students/list/            # Student list
GET  /students/detail/<id>/     # Student details
GET  /students/update/<id>/     # Edit form
POST /students/update/<id>/     # Submit changes
GET  /students/delete/<id>/     # Delete confirmation
POST /students/delete/<id>/     # Confirm deletion
GET  /admin/                    # Admin panel
```

## Models

### Student Model

```python
class Student(models.Model):
    name: CharField        # Full name (max 100 chars)
    email: EmailField      # Unique email address
    age: IntegerField      # Age (5-100)
    created_at: DateTime   # Creation timestamp
    updated_at: DateTime   # Last update timestamp
```

## Form Validation

The StudentForm includes comprehensive validation:

- **Name**: Non-empty, minimum 2 characters
- **Email**: Valid format, must be unique
- **Age**: Between 5 and 100 years

## Database

### SQLite (Development)

Default configuration. Database file: `db.sqlite3`

### PostgreSQL (Production)

Update `settings.py` or `.env`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'studentportal',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Running Migrations

```bash
# Create migrations for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Show migration history
python manage.py showmigrations

# Revert to specific migration
python manage.py migrate students 0001
```

## Common Commands

```bash
# Create superuser
python manage.py createsuperuser

# Create test data
python manage.py shell

# Check for issues
python manage.py check

# Collect static files (production)
python manage.py collectstatic

# Empty database (use with caution)
python manage.py flush
```

## Security Best Practices

1. **Never commit `.env` file** to version control
2. **Change SECRET_KEY** in production
3. **Set DEBUG=False** in production
4. **Use HTTPS** in production
5. **Use environment variables** for sensitive data
6. **Validate all user inputs** (already implemented)
7. **Keep dependencies updated**: `pip install --upgrade -r requirements.txt`

## Deployment

### Preparation Checklist

- [ ] Set `DEBUG = False` in settings
- [ ] Generate new `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database
- [ ] Configure email backend for notifications
- [ ] Set up HTTPS/SSL certificate
- [ ] Configure static files serving
- [ ] Set up logging
- [ ] Create `.env` file with production variables

### Deploying to Production

Options:
- **Gunicorn** + **Nginx**: Recommended for production
- **Apache** + **mod_wsgi**
- **PaaS platforms**: Heroku, PythonAnywhere, etc.

## Troubleshooting

### Port Already in Use

```bash
# Run on different port
python manage.py runserver 8001
```

### Migration Issues

```bash
# Recreate migrations
python manage.py migrate students zero
python manage.py makemigrations students
python manage.py migrate students
```

### Database Locked

Delete `db.sqlite3` and run migrations again (development only):

```bash
rm db.sqlite3
python manage.py migrate
```

### Admin Not Working

Ensure superuser exists:

```bash
python manage.py createsuperuser
```

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test students

# Run with verbose output
python manage.py test --verbosity=2
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is provided as-is for educational purposes.

## Support & Documentation

- Django Official Docs: https://docs.djangoproject.com/
- Django Best Practices: https://docs.djangoproject.com/en/stable/
- Django REST Framework: https://www.django-rest-framework.org/

## Version History

- **v1.0.0** (2026-05-04): Initial release
  - Student registration form
  - CRUD operations
  - Admin interface
  - Responsive templates

---

**Happy Coding!** 🚀
