"""Contact form."""
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model  = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name":    forms.TextInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-saffron-200 focus:ring-2 focus:ring-saffron-500 focus:outline-none bg-cream-100",
                "placeholder": _("Your full name / તમારું નામ"),
            }),
            "email":   forms.EmailInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-saffron-200 focus:ring-2 focus:ring-saffron-500 focus:outline-none bg-cream-100",
                "placeholder": "example@email.com",
            }),
            "phone":   forms.TextInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-saffron-200 focus:ring-2 focus:ring-saffron-500 focus:outline-none bg-cream-100",
                "placeholder": _("Mobile number / મોબાઈલ નંબર"),
            }),
            "subject": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-saffron-200 focus:ring-2 focus:ring-saffron-500 focus:outline-none bg-cream-100",
                "placeholder": _("Subject / વિષય"),
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-saffron-200 focus:ring-2 focus:ring-saffron-500 focus:outline-none bg-cream-100",
                "rows": 5,
                "placeholder": _("Your message / તમારો સંદેશ"),
            }),
        }
