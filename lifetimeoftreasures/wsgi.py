"""
WSGI config for lifetimeoftreasures project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lifetimeoftreasures.settings.production')

sys.path.append('/var/www/html/project/lifetime-of-treasures/')
sys.path.append('/var/www/html/project/django/lib/python3.6/site-packages')

application = get_wsgi_application()
