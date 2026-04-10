"""
School models with full bilingual support via django-parler.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from cms.models.pluginmodel import CMSPlugin

# ─────────────────────────────────────────────
# Core Database Models (For News, Gallery, etc.)
# ─────────────────────────────────────────────

class HeroSlide(TranslatableModel):
    translations = TranslatedFields(
        title        = models.CharField(_("Title"), max_length=200),
        subtitle     = models.TextField(_("Subtitle"), blank=True),
        button_text  = models.CharField(_("Button Text"), max_length=100, blank=True),
        button_url   = models.CharField(_("Button URL"), max_length=200, blank=True, default="/"),
    )
    image    = models.ImageField(_("Image"), upload_to="hero/")
    order    = models.PositiveIntegerField(_("Order"), default=0)
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Hero Slide")
        verbose_name_plural = _("Hero Slides")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or f"Slide #{self.pk}"

class NewsPost(TranslatableModel):
    translations = TranslatedFields(
        title   = models.CharField(_("Title"), max_length=300),
        slug    = models.SlugField(_("Slug"), max_length=320, unique=False, allow_unicode=True),
        excerpt = models.TextField(_("Excerpt"), blank=True),
        body    = models.TextField(_("Body")),
    )
    cover_image   = models.ImageField(_("Cover Image"), upload_to="news/", blank=True, null=True)
    publish_date  = models.DateField(_("Publish Date"), auto_now_add=True)
    is_published  = models.BooleanField(_("Published"), default=True)
    is_featured   = models.BooleanField(_("Featured on Homepage"), default=False)

    class Meta:
        ordering = ["-publish_date"]
        verbose_name = _("News Post")
        verbose_name_plural = _("News Posts")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or f"Post #{self.pk}"

class GalleryCategory(TranslatableModel):
    translations = TranslatedFields(name = models.CharField(_("Name"), max_length=100))
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Gallery Category")
        verbose_name_plural = _("Gallery Categories")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or f"Category #{self.pk}"

class GalleryItem(TranslatableModel):
    translations = TranslatedFields(caption = models.CharField(_("Caption"), max_length=300, blank=True))
    image    = models.ImageField(_("Image"), upload_to="gallery/")
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="items")
    order    = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        ordering = ["category__order", "order"]
        verbose_name = _("Gallery Item")
        verbose_name_plural = _("Gallery Items")

    def __str__(self):
        return self.safe_translation_getter("caption", any_language=True) or f"Image #{self.pk}"

class Facility(TranslatableModel):
    translations = TranslatedFields(
        name        = models.CharField(_("Name"), max_length=200),
        description = models.TextField(_("Description"), blank=True),
    )
    icon  = models.CharField(_("Icon"), max_length=50, default="🏫")
    image = models.ImageField(_("Image"), upload_to="facilities/", blank=True, null=True)
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Facility")
        verbose_name_plural = _("Facilities")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or f"Facility #{self.pk}"

class StaffMember(TranslatableModel):
    translations = TranslatedFields(
        name        = models.CharField(_("Name"), max_length=200),
        designation = models.CharField(_("Designation"), max_length=200),
        bio         = models.TextField(_("Biography"), blank=True),
    )
    photo = models.ImageField(_("Photo"), upload_to="staff/", blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Staff Member")
        verbose_name_plural = _("Staff Members")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or f"Staff #{self.pk}"

class AcademicSubject(TranslatableModel):
    translations = TranslatedFields(
        name        = models.CharField(_("Subject Name"), max_length=200),
        description = models.TextField(_("Description"), blank=True),
    )
    standard    = models.CharField(_("Standard"), max_length=5)
    is_optional = models.BooleanField(_("Optional"), default=False)
    order       = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        ordering = ["standard", "order"]

class AdmissionInfo(TranslatableModel):
    translations = TranslatedFields(
        eligibility   = models.TextField(_("Eligibility")),
        fees_details  = models.TextField(_("Fees")),
    )
    standard       = models.CharField(_("Standard"), max_length=5, unique=True)
    academic_year  = models.CharField(_("Year"), max_length=20, default="2026-27")
    is_open        = models.BooleanField(_("Open"), default=True)


# ─────────────────────────────────────────────
# CMS Plugin Models (Total Control Overhaul)
# ─────────────────────────────────────────────

class StaffGridPluginModel(CMSPlugin):
    title = models.CharField(_("Section Title"), max_length=200, blank=True)

class StaffItemPluginModel(CMSPlugin):
    name        = models.CharField(_("Name"), max_length=200)
    designation = models.CharField(_("Designation"), max_length=200)
    photo       = models.ImageField(_("Photo"), upload_to="staff/", blank=True, null=True)
    bio         = models.TextField(_("Brief Bio"), blank=True)

class FacilityGridPluginModel(CMSPlugin):
    title   = models.CharField(_("Section Title"), max_length=200, blank=True)
    tagline = models.TextField(_("Tagline"), blank=True)

class FacilityItemPluginModel(CMSPlugin):
    title       = models.CharField(_("Facility Title"), max_length=200)
    icon_class  = models.CharField(_("Icon Class / Emoji"), max_length=50, default="🏫")
    image       = models.ImageField(_("Image"), upload_to="facilities/", blank=True, null=True)
    description = models.TextField(_("Description"), blank=True)

class AcademicGridPluginModel(CMSPlugin):
    title = models.CharField(_("Section Title"), max_length=200, blank=True)

class AcademicItemPluginModel(CMSPlugin):
    label    = models.CharField(_("Block Heading"), max_length=100)
    tag      = models.CharField(_("Side Tag"), max_length=10, default="09")
    subjects = models.TextField(_("Subjects List"))

class SchoolStatsPluginModel(CMSPlugin):
    title       = models.CharField(_("Section Title"), max_length=200, blank=True)
    stat1_label = models.CharField(_("Label 1"), max_length=100, blank=True)
    stat1_value = models.CharField(_("Value 1"), max_length=50, blank=True)
    stat2_label = models.CharField(_("Label 2"), max_length=100, blank=True)
    stat2_value = models.CharField(_("Value 2"), max_length=50, blank=True)
    stat3_label = models.CharField(_("Label 3"), max_length=100, blank=True)
    stat3_value = models.CharField(_("Value 3"), max_length=50, blank=True)
    stat4_label = models.CharField(_("Label 4"), max_length=100, blank=True)
    stat4_value = models.CharField(_("Value 4"), max_length=50, blank=True)

class GalleryItemPluginModel(CMSPlugin):
    image   = models.ImageField(_("Gallery Image"), upload_to="gallery/")
    caption = models.CharField(_("Caption"), max_length=200, blank=True)

class NewsItemPluginModel(CMSPlugin):
    title   = models.CharField(_("News Title"), max_length=200)
    date    = models.DateField(_("Post Date"))
    excerpt = models.TextField(_("Excerpt"), blank=True)
    image   = models.ImageField(_("Image"), upload_to="news/", blank=True, null=True)
    url     = models.CharField(_("Link URL"), max_length=200, blank=True)

class AdmissionBannerPluginModel(CMSPlugin):
    title    = models.CharField(_("Title"), max_length=200)
    subtitle = models.TextField(_("Subtitle"), blank=True)
    btn_text = models.CharField(_("Button Text"), max_length=50)
    btn_url  = models.CharField(_("Button URL"), max_length=200, default="/admissions")
    bg_color = models.CharField(_("Background Hex Color"), max_length=20, default="#0F172A")

# ─────────────────────────────────────────────
# Header & Footer Plugins
# ─────────────────────────────────────────────

class PremiumHeaderPluginModel(CMSPlugin):
    logo = models.ImageField(_("Logo"), upload_to="branding/", blank=True, null=True)

class HeaderSlideModel(CMSPlugin):
    image    = models.ImageField(_("Background Image"), upload_to="hero/")
    title    = models.CharField(_("Title"), max_length=200, blank=True)
    subtitle = models.TextField(_("Subtitle"), blank=True)
    btn_text = models.CharField(_("Button Text"), max_length=50, blank=True)
    btn_url  = models.CharField(_("Button URL"), max_length=200, blank=True)

class FooterBuilderModel(CMSPlugin):
    background_color = models.CharField(_("Background Color"), max_length=20, default="#0F172A")

class FooterColumnModel(CMSPlugin):
    title = models.CharField(_("Column Title"), max_length=100)
    body  = models.TextField(_("Column Body / Links"), help_text="Enter text or raw links")

class TestimonialCarouselModel(CMSPlugin):
    title = models.CharField(_("Section Title"), max_length=200, blank=True)

class TestimonialItemModel(CMSPlugin):
    author = models.CharField(_("Author Name"), max_length=100)
    role   = models.CharField(_("Role"), max_length=100, blank=True)
    quote  = models.TextField(_("Quote"))
    image  = models.ImageField(_("Photo"), upload_to="testimonials/", blank=True, null=True)
