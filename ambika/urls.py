"""URL configuration for Shri Ambika Sanskrit Mahavidyalaya."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

# Django CMS must handle URLs last
from cms.sitemaps import CMSSitemap

# i18n URL patterns
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Language switcher endpoint
    path("i18n/", include("django.conf.urls.i18n")),
    # Admin (Standard location for CMS reliability)
    path("admin/", admin.site.urls),
]

from apps.school import views as school_views

urlpatterns += i18n_patterns(
    path("contact/",  include("apps.contact.urls", namespace="contact")),
    path("school/",   include("apps.school.urls",  namespace="school")),
    
    # Root-level shortcuts to prevent CMS 404s for hardcoded legacy links
    path("academics/",  school_views.academics,  name="root_academics"),
    path("admissions/", school_views.admissions, name="root_admissions"),
    path("explore/",    school_views.explore,    name="root_explore"),
    path("apply/",      school_views.apply,      name="root_apply"),

    # Sitemap
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"cmspages": CMSSitemap}},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    # CMS must be LAST
    path("", include("cms.urls")),

    prefix_default_language=getattr(settings, "PREFIX_DEFAULT_LANGUAGE", True),
)

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
