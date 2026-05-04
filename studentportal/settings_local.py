"""
Local development settings for Django Student Portal.

This file overrides settings for local development with:
- Debug enabled
- SQLite database
- Local development server
- Email console backend

To use these settings, add to your .env file:
DJANGO_SETTINGS_MODULE=studentportal.settings.local
"""

from studentportal.settings import *

# Development settings
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*.localhost']

# Development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email console output (for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable HTTPS requirement for local development
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# Enable SQL query logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

# Static files development
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files for development
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
