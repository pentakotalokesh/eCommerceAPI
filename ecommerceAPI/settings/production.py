from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER':'root',
        'PASSWORD': 'Lokesh@123',
        'HOST':'localhost',
        'PORT':'3306'
    }
}