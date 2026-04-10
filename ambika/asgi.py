"""ASGI config for ambika project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ambika.settings.local")
application = get_asgi_application()
