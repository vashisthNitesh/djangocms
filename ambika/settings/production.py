"""Production settings (PostgreSQL, whitenoise, etc.)."""
import environ
from .base import *  # noqa: F401, F403

env = environ.Env()

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost"])

DATABASES = {
    "default": env.db("DATABASE_URL"),
}
DATABASES["default"]["CONN_MAX_AGE"] = 60

# HTTPS settings
SECURE_SSL_REDIRECT          = True
SECURE_HSTS_SECONDS          = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD          = True
SESSION_COOKIE_SECURE        = True
CSRF_COOKIE_SECURE           = True

# Email
EMAIL_BACKEND       = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST          = env("EMAIL_HOST", default="localhost")
EMAIL_PORT          = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_USER     = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS       = env.bool("EMAIL_USE_TLS", default=True)
DEFAULT_FROM_EMAIL  = env("DEFAULT_FROM_EMAIL", default="noreply@ambika.edu")
