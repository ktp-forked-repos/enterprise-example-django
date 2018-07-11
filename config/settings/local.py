from .base import *


DEBUG = True

SECRET_KEY = 'SECURITY WARNING: keep the secret key used in production secret!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
