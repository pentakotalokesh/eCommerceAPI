from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drfapis$ecommerce',
        'USER':'drfapis',
        'PASSWORD': 'admin@123',
        'HOST':'drfapis.mysql.pythonanywhere-services.com',
        'PORT':'3306'
    }
}