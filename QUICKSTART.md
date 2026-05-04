# Django Student Portal - Quick Start Guide

## 🚀 Quick Start (5 minutes)

### 1. Activate Virtual Environment

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 2. Start Development Server

```bash
python manage.py runserver
```

### 3. Access the Application

- **Registration Form**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Student List**: http://127.0.0.1:8000/list/

---

## 📋 Admin Credentials

**Create admin account:**
```bash
python manage.py createsuperuser
```

**Default credentials (if already created):**
- Username: `admin`
- Email: `admin@example.com`
- Password: (as set during creation)

---

## 🔧 Common Tasks

### Create New Admin User
```bash
python manage.py createsuperuser
```

### View Database
```bash
python manage.py dbshell
```

### Create Test Data
```bash
python manage.py shell
# Then in Python shell:
>>> from students.models import Student
>>> Student.objects.create(name='John Doe', email='john@example.com', age=20)
```

### Reset Database (Development Only)
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Install Additional Packages
```bash
pip install package_name
pip freeze > requirements.txt
```

---

## 📁 File Structure Reference

```
Django-Based-Form/
├── .venv/                  # Virtual environment
├── manage.py              # Django CLI
├── db.sqlite3            # SQLite database
├── .env                  # Environment variables
├── .gitignore           # Git ignore rules
├── requirements.txt     # Project dependencies
├── README.md            # Main documentation
│
├── studentportal/       # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── students/            # Main app
    ├── models.py        # Database models
    ├── forms.py         # Form definitions
    ├── views.py         # View logic
    ├── urls.py          # URL patterns
    ├── admin.py         # Admin configuration
    ├── apps.py          # App config
    ├── migrations/      # Database migrations
    └── templates/       # HTML templates
```

---

## 🔗 URL Routes

| URL | Purpose |
|-----|---------|
| `/` | Student registration form |
| `/success/<id>/` | Success message |
| `/list/` | View all students |
| `/<id>/` | View student details |
| `/<id>/update/` | Edit student |
| `/<id>/delete/` | Delete student |
| `/admin/` | Django admin |

---

## ✅ Troubleshooting

### Server won't start
```bash
# Check if port 8000 is in use
python manage.py runserver 8001

# Restart virtual environment
deactivate
.venv\Scripts\activate
```

### Database errors
```bash
# Reset database
rm db.sqlite3
python manage.py migrate
```

### Import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Template not found
- Ensure templates are in `students/templates/students/`
- Check `TEMPLATES` setting in `settings.py`

---

## 🔐 Security Checklist

- [ ] Never share `.env` file
- [ ] Use strong SECRET_KEY in production
- [ ] Set `DEBUG=False` before deployment
- [ ] Validate all user inputs
- [ ] Use HTTPS in production
- [ ] Keep dependencies updated
- [ ] Use environment variables for secrets

---

## 📚 Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/)
- [Python Official Documentation](https://docs.python.org/3/)
- [HTML & CSS Reference](https://developer.mozilla.org/)

---

## 💡 Pro Tips

1. **Use Django Shell for testing:**
   ```bash
   python manage.py shell
   ```

2. **Pretty print Django models:**
   ```python
   from students.models import Student
   students = Student.objects.all()
   for student in students:
       print(f"{student.name} - {student.email}")
   ```

3. **Access admin from command line:**
   ```bash
   python manage.py createsuperuser --username admin --email admin@example.com
   ```

4. **View SQL queries (development):**
   ```python
   from django.db import connection
   from django.test.utils import CaptureQueriesContext
   
   with CaptureQueriesContext(connection) as context:
       students = Student.objects.all()
   print(context)
   ```

---

## 🚀 Next Steps

1. **Customize templates** - Edit HTML files in `students/templates/`
2. **Add more fields** - Update models.py and run migrations
3. **Create API endpoints** - Install Django REST Framework
4. **Add authentication** - Implement user login/registration
5. **Deploy to production** - Follow deployment guide in README.md

---

## 📞 Support

For issues or questions:
1. Check README.md for detailed documentation
2. Review Django documentation
3. Check terminal error messages
4. Verify `.env` configuration

---

**Last Updated**: 2026-05-04
**Version**: 1.0.0
**Django Version**: 5.0.1
**Python Version**: 3.14.3+
