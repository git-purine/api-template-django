"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

rack = os.environ.get('RACK_ENV', 'local')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "isviz.settings.%s" % rack)

application = get_wsgi_application()
