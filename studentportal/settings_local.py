from studentportal.settings import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*.localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable HTTPS requirement for local development
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

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

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
