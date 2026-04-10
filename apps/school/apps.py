"""
School app configuration.
"""
from django.apps import AppConfig


class SchoolConfig(AppConfig):
    name           = "apps.school"
    verbose_name   = "School"
    default_auto_field = "django.db.models.BigAutoField"
