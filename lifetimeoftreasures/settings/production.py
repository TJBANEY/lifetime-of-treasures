from lifetimeoftreasures.settings.base import *

DEBUG = False
# STATIC_ROOT = '/var/www/html/project/static/'
MEDIA_ROOT = '/var/www/html/project/media'

DATABASES['default'] = {
    'NAME': 'postgres',
    'USER': 'master',
    'PASSWORD': 'Whopper123',
    'HOST': 'alifetimeoftreasures.c9h0jgennv0n.us-east-2.rds.amazonaws.com',
    'PORT': '5432',
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
}