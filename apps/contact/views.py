"""Contact views."""
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from .forms import ContactForm


def contact(request):
    form    = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            # Send notification email
            try:
                send_mail(
                    subject=f"[Ambika Mahavidyalaya] {msg.subject or 'New Contact Message'}",
                    message=(
                        f"Name: {msg.name}\n"
                        f"Email: {msg.email}\n"
                        f"Phone: {msg.phone}\n\n"
                        f"{msg.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            success = True
            form    = ContactForm()  # reset

    return render(request, "contact.html", {"form": form, "success": success})
