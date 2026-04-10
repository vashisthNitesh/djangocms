"""Local development settings – Neon PostgreSQL."""
from .base import *  # noqa: F401, F403

DEBUG = True

SECRET_KEY = "dev-secret-key-not-for-production-12345"

ALLOWED_HOSTS = ["*"]

# ─────────────────────────────────────────────
# Neon PostgreSQL Database
# ─────────────────────────────────────────────
import os

DATABASES = {
    "default": {
        "ENGINE":   "django.db.backends.postgresql",
        "NAME":     "neondb",
        "USER":     "neondb_owner",
        "PASSWORD": "npg_RhJc4unsp1Cq",
        "HOST":     "ep-billowing-heart-anovw6p8-pooler.c-6.us-east-1.aws.neon.tech",
        "PORT":     "5432",
        "OPTIONS": {
            "sslmode":         "require",
            "channel_binding": "require",
        },
        "DISABLE_SERVER_SIDE_CURSORS": True,
        "CONN_MAX_AGE": 60,
    }
}

# Console email backend (prints emails to terminal)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Static files served by Django in dev
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
