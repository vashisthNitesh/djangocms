"""
Admin configuration for school models.
Uses django-parler's TranslatableAdmin for full bilingual editing.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin, TranslatableStackedInline

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


@admin.register(HeroSlide)
class HeroSlideAdmin(TranslatableAdmin):
    list_display  = ("title_display", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering      = ("order",)

    def title_display(self, obj):
        return obj.safe_translation_getter("title", any_language=True)
    title_display.short_description = _("Title")


@admin.register(NewsPost)
class NewsPostAdmin(TranslatableAdmin):
    list_display  = ("title_display", "publish_date", "is_published", "is_featured")
    list_filter   = ("is_published", "is_featured")
    list_editable = ("is_published", "is_featured")
    search_fields = ("translations__title",)
    ordering      = ("-publish_date",)

    def title_display(self, obj):
        return obj.safe_translation_getter("title", any_language=True)
    title_display.short_description = _("Title")


class GalleryItemInline(TranslatableStackedInline):
    model  = GalleryItem
    extra  = 1
    fields = ("caption", "image", "order")


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(TranslatableAdmin):
    list_display = ("name_display", "order")
    list_editable = ("order",)
    inlines = [GalleryItemInline]

    def name_display(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    name_display.short_description = _("Name")


@admin.register(GalleryItem)
class GalleryItemAdmin(TranslatableAdmin):
    list_display  = ("caption_display", "category", "order")
    list_filter   = ("category",)
    list_editable = ("order",)

    def caption_display(self, obj):
        return obj.safe_translation_getter("caption", any_language=True)
    caption_display.short_description = _("Caption")


@admin.register(Facility)
class FacilityAdmin(TranslatableAdmin):
    list_display  = ("name_display", "icon", "order")
    list_editable = ("order",)

    def name_display(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    name_display.short_description = _("Name")


@admin.register(AcademicSubject)
class AcademicSubjectAdmin(TranslatableAdmin):
    list_display  = ("name_display", "standard", "is_optional", "order")
    list_filter   = ("standard", "is_optional")
    list_editable = ("order",)

    def name_display(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    name_display.short_description = _("Subject")


@admin.register(AdmissionInfo)
class AdmissionInfoAdmin(TranslatableAdmin):
    list_display  = ("standard", "academic_year", "is_open")
    list_editable = ("is_open",)


@admin.register(StaffMember)
class StaffMemberAdmin(TranslatableAdmin):
    list_display  = ("name_display", "designation_display", "order")
    list_editable = ("order",)

    def name_display(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    name_display.short_description = _("Name")

    def designation_display(self, obj):
        return obj.safe_translation_getter("designation", any_language=True)
    designation_display.short_description = _("Designation")
