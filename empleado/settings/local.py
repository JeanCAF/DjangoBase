from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempledo',
        'USER': 'juano',
        'PASSWORD': '3M44r4ll4',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


STATIC_URL = '/static/'
