"""
Views for the school app.
"""
from django.shortcuts import get_object_or_404, render
from django.utils.translation import get_language

from .models import (
    AcademicSubject,
    AdmissionInfo,
    Facility,
    GalleryCategory,
    GalleryItem,
    HeroSlide,
    NewsPost,
    StaffMember,
)


def home(request):
    slides   = HeroSlide.objects.filter(is_active=True).order_by("order")
    news     = NewsPost.objects.filter(is_published=True)[:3]
    facilities = Facility.objects.order_by("order")[:6]
    admission_open = AdmissionInfo.objects.filter(is_open=True)

    return render(request, "home.html", {
        "slides":         slides,
        "news":           news,
        "facilities":     facilities,
        "admission_open": admission_open,
    })


def about(request):
    staff = StaffMember.objects.order_by("order")
    return render(request, "about.html", {"staff": staff})


def academics(request):
    subjects_9  = AcademicSubject.objects.filter(standard="9").order_by("order")
    subjects_10 = AcademicSubject.objects.filter(standard="10").order_by("order")
    subjects_11 = AcademicSubject.objects.filter(standard="11").order_by("order")
    subjects_12 = AcademicSubject.objects.filter(standard="12").order_by("order")

    return render(request, "academics.html", {
        "subjects_9":  subjects_9,
        "subjects_10": subjects_10,
        "subjects_11": subjects_11,
        "subjects_12": subjects_12,
    })


def admissions(request):
    admission_9  = AdmissionInfo.objects.filter(standard="9").first()
    admission_11 = AdmissionInfo.objects.filter(standard="11").first()

    return render(request, "admissions.html", {
        "admission_9":  admission_9,
        "admission_11": admission_11,
    })


def gallery(request):
    categories = GalleryCategory.objects.prefetch_related("items").order_by("order")
    all_items  = GalleryItem.objects.select_related("category").order_by("category__order", "order")

    return render(request, "gallery.html", {
        "categories": categories,
        "all_items":  all_items,
    })


def news_list(request):
    posts = NewsPost.objects.filter(is_published=True).order_by("-publish_date")
    return render(request, "news/list.html", {"posts": posts})


def news_detail(request, slug):
    lang  = get_language()
    posts = NewsPost.objects.translated(slug=slug)
    post  = posts.first()
    if post is None:
        # Try any language
        from parler.utils.context import switch_language
        post = get_object_or_404(NewsPost, translations__slug=slug)

    return render(request, "news/detail.html", {"post": post})


def facilities(request):
    items = Facility.objects.order_by("order")
    return render(request, "facilities.html", {"facilities": items})


def explore(request):
    return render(request, "explore.html")


def apply(request):
    return render(request, "apply.html")
