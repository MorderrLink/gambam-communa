"""
WSGI config for gambam project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import os
import sys
# DJANGO_PATH =  os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
# sys.path.append(DJANGO_PATH)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gambam.settings')

application = get_wsgi_application()

app = application
