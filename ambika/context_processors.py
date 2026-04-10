from django.conf import settings

def school_settings(request):
    """
    Exposes school-related constants from settings to all templates.
    """
    return {
        "SCHOOL_NAME_GU":    getattr(settings, "SCHOOL_NAME_GU", ""),
        "SCHOOL_NAME_EN":    getattr(settings, "SCHOOL_NAME_EN", ""),
        "SCHOOL_TRUST_GU":   getattr(settings, "SCHOOL_TRUST_GU", ""),
        "SCHOOL_TRUST_EN":   getattr(settings, "SCHOOL_TRUST_EN", ""),
        "SCHOOL_TAGLINE_GU": getattr(settings, "SCHOOL_TAGLINE_GU", ""),
        "SCHOOL_TAGLINE_EN": getattr(settings, "SCHOOL_TAGLINE_EN", ""),
        "SCHOOL_PHONE":      getattr(settings, "SCHOOL_PHONE", ""),
        "SCHOOL_EMAIL":      getattr(settings, "SCHOOL_EMAIL", ""),
        "SCHOOL_ADDRESS_GU": getattr(settings, "SCHOOL_ADDRESS_GU", ""),
        "SCHOOL_ADDRESS_EN": getattr(settings, "SCHOOL_ADDRESS_EN", ""),
    }
