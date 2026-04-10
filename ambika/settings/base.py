"""
Base settings for Shri Ambika Sanskrit Mahavidyalaya Django CMS project.
"""
import os
from pathlib import Path

import environ

# ─────────────────────────────────────────────
# Env
# ─────────────────────────────────────────────
env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "change-me-in-production-please"),
    ALLOWED_HOSTS=(list, ["*"]),
    DATABASE_URL=(str, "sqlite:///db.sqlite3"),
    EMAIL_BACKEND=(str, "django.core.mail.backends.console.EmailBackend"),
    DEFAULT_FROM_EMAIL=(str, "noreply@ambika.edu"),
    CONTACT_EMAIL=(str, "shriambika1@gmail.com"),
)

# ─────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ─────────────────────────────────────────────
# Security
# ─────────────────────────────────────────────
SECRET_KEY = env("SECRET_KEY")
DEBUG       = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# ─────────────────────────────────────────────
# Application definition
# ─────────────────────────────────────────────
INSTALLED_APPS = [
    "djangocms_admin_style",
    "cms",
    "menus",
    "treebeard",
    "sekizai",
    "djangocms_versioning",
    "djangocms_alias",

    # Django contrib
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",

    # Filer (file & image management for CMS)
    "filer",
    "easy_thumbnails",

    # CMS plugins
    "djangocms_text_ckeditor",
    "djangocms_picture",
    "djangocms_link",
    "djangocms_file",

    # Parler (multilingual model fields)
    "parler",

    # Jinja2 integration
    "django_jinja",

    # Forms
    "crispy_forms",

    # Project apps
    "apps.school",
    "apps.contact",

    # Tailwind CLI (Node-free)
    "django_tailwind_cli",
]

# ─────────────────────────────────────────────
# Middleware
# ─────────────────────────────────────────────
MIDDLEWARE = [
    "cms.middleware.utils.ApphookReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
]

# ─────────────────────────────────────────────
# Security
# ─────────────────────────────────────────────
X_FRAME_OPTIONS = "SAMEORIGIN"
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# Sekizai
SEKIZAI_IGNORE_VALIDATION = True

ROOT_URLCONF = "ambika.urls"

# ─────────────────────────────────────────────
# Templates – Jinja2 primary + Django fallback
# ─────────────────────────────────────────────
TEMPLATES = [
    {
        # Jinja2 engine for project templates
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".html",
            "match_regex": r"^(?!admin/|cms/|djangocms_|filer/|parler/|debug_toolbar/|django/).*",
            "app_dirname": "jinja2",
            "environment": "ambika.jinja2.environment",
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
                "django.template.context_processors.i18n",
            ],
            "extensions": [
                "jinja2.ext.i18n",
                "jinja2.ext.debug",
                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
            ],
            "undefined": "jinja2.Undefined",
            "newstyle_gettext": True,
        },
    },
    {
        # Django engine – used for admin and CMS toolbar
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates" / "django"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
                "django.template.context_processors.i18n",
                "ambika.context_processors.school_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "ambika.wsgi.application"

# ─────────────────────────────────────────────
# Database
# ─────────────────────────────────────────────
DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3"),
}
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# ─────────────────────────────────────────────
# Caching (Crucial for Django CMS Performance)
# ─────────────────────────────────────────────
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "ambika-cms-cache",
    }
}
CMS_PAGE_CACHE = True
CMS_PLACEHOLDER_CACHE = True
CMS_PLUGIN_CACHE = True

# ─────────────────────────────────────────────
# Password validation
# ─────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─────────────────────────────────────────────
# Internationalization
# ─────────────────────────────────────────────
LANGUAGE_CODE = "gu"         # Default: Gujarati
TIME_ZONE     = "Asia/Kolkata"
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ("gu", _("ગુજરાતી")),
    ("en", _("English")),
]

LOCALE_PATHS = [BASE_DIR / "locale"]

# ─────────────────────────────────────────────
# Static & Media
# ─────────────────────────────────────────────
STATIC_URL  = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL  = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ─────────────────────────────────────────────
# Sites framework
# ─────────────────────────────────────────────
SITE_ID = 1

# ─────────────────────────────────────────────
# Django CMS
# ─────────────────────────────────────────────
CMS_TEMPLATES = [
    ("home.html",        "Home"),
    ("about.html",       "About Us"),
    ("academics.html",   "Academics"),
    ("admissions.html",  "Admissions"),
    ("gallery.html",     "Gallery"),
    ("news/list.html",   "News & Events"),
    ("facilities.html",  "Facilities"),
    ("contact.html",     "Contact Us"),
    ("base.html",        "Base (Generic)"),
]

CMS_LANGUAGES = {
    "default": {
        "public":           True,
        "hide_untranslated": False,
        "redirect_on_fallback": True,
        "fallbacks":        ["gu", "en"],
    },
    1: [
        {
            "code":              "gu",
            "name":              "ગુજરાતી",
            "public":            True,
            "fallbacks":         ["en"],
            "hide_untranslated": False,
        },
        {
            "code":              "en",
            "name":              "English",
            "public":            True,
            "fallbacks":         ["gu"],
            "hide_untranslated": False,
        },
    ],
}

# ─────────────────────────────────────────────
# i18n URL Prefixing
# ─────────────────────────────────────────────
PREFIX_DEFAULT_LANGUAGE = True

CMS_PERMISSION  = False
CMS_CONFIRM_VERSION4 = True   # Required by django-cms 4.x
CMS_PLACEHOLDER_CONF = {}

# ─────────────────────────────────────────────
# Parler (translations)
# ─────────────────────────────────────────────
PARLER_DEFAULT_LANGUAGE_CODE = "gu"
PARLER_LANGUAGES = {
    1: (
        {"code": "gu"},
        {"code": "en"},
    ),
    "default": {
        "fallbacks":         ["en"],
        "hide_untranslated": False,
    },
}

# ─────────────────────────────────────────────
# Filer (file manager)
# ─────────────────────────────────────────────
FILER_ENABLE_LOGGING         = True
FILER_IMAGE_MODEL            = "filer.Image"
THUMBNAIL_HIGH_RESOLUTION     = True
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# ─────────────────────────────────────────────
# Email
# ─────────────────────────────────────────────
EMAIL_BACKEND    = env("EMAIL_BACKEND")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
CONTACT_EMAIL    = env("CONTACT_EMAIL", default="shriambika1@gmail.com")

# SMTP (uncomment and configure for production)
# EMAIL_HOST          = env("EMAIL_HOST", default="localhost")
# EMAIL_PORT          = env.int("EMAIL_PORT", default=587)
# EMAIL_HOST_USER     = env("EMAIL_HOST_USER", default="")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
# EMAIL_USE_TLS       = env.bool("EMAIL_USE_TLS", default=True)

# ─────────────────────────────────────────────
# Crispy Forms
# ─────────────────────────────────────────────
CRISPY_TEMPLATE_PACK = "bootstrap4"   # override in templates if needed

# ─────────────────────────────────────────────
# Meta / SEO
# ─────────────────────────────────────────────
META_SITE_PROTOCOL = "https"
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True

# ─────────────────────────────────────────────
# Default auto field
# ─────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ─────────────────────────────────────────────
# School constants (used across templates)
# ─────────────────────────────────────────────
SCHOOL_NAME_GU   = "શ્રી અંબિકા સંસ્કૃત મહાવિદ્યાલય, અંબાજી"
SCHOOL_NAME_EN   = "Shri Ambika Sanskrit Mahavidyalaya, Ambaji"
SCHOOL_TRUST_GU  = "શ્રી આરાસુરી અંબાજી માતા દેવસ્થાન ટ્રસ્ટ"
SCHOOL_TRUST_EN  = "Shri Arasuri Ambaji Mata Devasthan Trust"
SCHOOL_TAGLINE_GU = "ઋષિ કુમારો (Boys) માટે – ધો. ૯ થી ૧૨"
SCHOOL_TAGLINE_EN = "Sanskrit Education for Rishi Kumars (Boys) – Std 9 to 12"
SCHOOL_PHONE     = "9925368974"
SCHOOL_EMAIL     = "shriambika1@gmail.com"
SCHOOL_ADDRESS_GU = "અંબાજી, બનાસકાંઠા, ગુજરાત"
SCHOOL_ADDRESS_EN = "Ambaji, Banaskantha, Gujarat – 385110"

# ─────────────────────────────────────────────
# Tailwind CLI Configuration
# ─────────────────────────────────────────────
TAILWIND_CLI_VERSION = "3.4.1"
TAILWIND_CLI_PATH = BASE_DIR / "bin"
TAILWIND_CLI_CONFIG_FILE = "tailwind.config.js"
TAILWIND_CLI_SRC_CSS = "static/src/input.css"
TAILWIND_CLI_DIST_CSS = "dist/output.css"
