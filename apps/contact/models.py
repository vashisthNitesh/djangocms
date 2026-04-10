"""Contact models."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    name       = models.CharField(_("Full Name"), max_length=200)
    email      = models.EmailField(_("Email"))
    phone      = models.CharField(_("Phone"), max_length=20, blank=True)
    subject    = models.CharField(_("Subject"), max_length=300, blank=True)
    message    = models.TextField(_("Message"))
    created_at = models.DateTimeField(_("Received At"), auto_now_add=True)
    is_read    = models.BooleanField(_("Read"), default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name        = _("Contact Message")
        verbose_name_plural = _("Contact Messages")

    def __str__(self):
        return f"{self.name} – {self.created_at:%d %b %Y %H:%M}"
