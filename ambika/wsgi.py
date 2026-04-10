"""WSGI config for ambika project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ambika.settings.local")
application = get_wsgi_application()
