from lifetimeoftreasures.settings.base import *

DEBUG = False
# STATIC_ROOT = '/var/www/html/project/static/'

# Needs to be RDS instance you created
DATABASES['default'] = {
    'NAME': 'lifetimeoftreasures',
    'USER': 'tim',
    'HOST': 'localhost',
    'PORT': '5432',
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
}
