"""
Jinja2 environment configuration for Django.
Bridges Django template tags/filters with Jinja2.
"""
from django.conf import settings
from django.contrib import messages
from django.templatetags.static import static
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext, ngettext

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)

    # i18n
    env.install_gettext_callables(gettext, ngettext, newstyle=True)

    env.globals.update(
        {
            # Django built-ins
            "static":          static,
            "url":             reverse,
            "get_messages":    messages.get_messages,

            # Language helpers
            "LANGUAGES":       settings.LANGUAGES,
            "LANGUAGE_CODE":   translation.get_language,

            # School constants
            "SCHOOL_NAME_GU":    settings.SCHOOL_NAME_GU,
            "SCHOOL_NAME_EN":    settings.SCHOOL_NAME_EN,
            "SCHOOL_TRUST_GU":   settings.SCHOOL_TRUST_GU,
            "SCHOOL_TRUST_EN":   settings.SCHOOL_TRUST_EN,
            "SCHOOL_TAGLINE_GU": settings.SCHOOL_TAGLINE_GU,
            "SCHOOL_TAGLINE_EN": settings.SCHOOL_TAGLINE_EN,
            "SCHOOL_PHONE":      settings.SCHOOL_PHONE,
            "SCHOOL_EMAIL":      settings.SCHOOL_EMAIL,
            "SCHOOL_ADDRESS_GU": settings.SCHOOL_ADDRESS_GU,
            "SCHOOL_ADDRESS_EN": settings.SCHOOL_ADDRESS_EN,
        }
    )
    return env
