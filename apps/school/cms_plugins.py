from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import (
    StaffGridPluginModel, StaffItemPluginModel, FacilityGridPluginModel, FacilityItemPluginModel,
    AcademicGridPluginModel, AcademicItemPluginModel, SchoolStatsPluginModel,
    GalleryItemPluginModel, NewsItemPluginModel, AdmissionBannerPluginModel,
    PremiumHeaderPluginModel, HeaderSlideModel, FooterBuilderModel, FooterColumnModel,
    TestimonialCarouselModel, TestimonialItemModel
)

# ─────────────────────────────────────────────
# Header Suite
# ─────────────────────────────────────────────

@plugin_pool.register_plugin
class PremiumHeaderPlugin(CMSPluginBase):
    model           = PremiumHeaderPluginModel
    name            = _("Premium Header (Hero)")
    module          = _("Ambika: Navigation")
    render_template = "cms/plugins/header_premium.html"
    allow_children  = True
    child_classes   = ["HeaderSlidePlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class HeaderSlidePlugin(CMSPluginBase):
    model           = HeaderSlideModel
    name            = _("Header Slide")
    module          = _("Ambika: Navigation")
    render_template = "cms/plugins/header_slide.html"
    require_parent  = True
    parent_classes  = ["PremiumHeaderPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

# ─────────────────────────────────────────────
# Footer Suite
# ─────────────────────────────────────────────

@plugin_pool.register_plugin
class FooterBuilderPlugin(CMSPluginBase):
    model           = FooterBuilderModel
    name            = _("Footer Builder")
    module          = _("Ambika: Navigation")
    render_template = "cms/plugins/footer_builder.html"
    allow_children  = True
    child_classes   = ["FooterColumnPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class FooterColumnPlugin(CMSPluginBase):
    model           = FooterColumnModel
    name            = _("Footer Column")
    module          = _("Ambika: Navigation")
    render_template = "cms/plugins/footer_column.html"
    require_parent  = True
    parent_classes  = ["FooterBuilderPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

# ─────────────────────────────────────────────
# Content Suite (Builder Pattern)
# ─────────────────────────────────────────────

@plugin_pool.register_plugin
class AdmissionBannerPlugin(CMSPluginBase):
    model           = AdmissionBannerPluginModel
    name            = _("Admission Banner")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/admission_banner.html"
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class StaffGridPlugin(CMSPluginBase):
    model           = StaffGridPluginModel
    name            = _("Staff Showcase")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/staff_grid.html"
    allow_children  = True
    child_classes   = ["StaffItemPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class StaffItemPlugin(CMSPluginBase):
    model           = StaffItemPluginModel
    name            = _("Staff Member Item")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/staff_item.html"
    require_parent  = True
    parent_classes  = ["StaffGridPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class FacilityGridPlugin(CMSPluginBase):
    model           = FacilityGridPluginModel
    name            = _("Facility Cards")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/facility_grid.html"
    allow_children  = True
    child_classes   = ["FacilityItemPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class FacilityItemPlugin(CMSPluginBase):
    model           = FacilityItemPluginModel
    name            = _("Facility Item")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/facility_item.html"
    require_parent  = True
    parent_classes  = ["FacilityGridPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class GalleryHighlightsPlugin(CMSPluginBase):
    model           = CMSPlugin
    name            = _("Gallery Grid")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/gallery_highlights.html"
    allow_children  = True
    child_classes   = ["GalleryItemPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class GalleryItemPlugin(CMSPluginBase):
    model           = GalleryItemPluginModel
    name            = _("Gallery Item")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/gallery_item_dynamic.html"
    require_parent  = True
    parent_classes  = ["GalleryHighlightsPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class LatestNewsPlugin(CMSPluginBase):
    model           = CMSPlugin
    name            = _("News Feed")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/latest_news.html"
    allow_children  = True
    child_classes   = ["NewsItemPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class NewsItemPlugin(CMSPluginBase):
    model           = NewsItemPluginModel
    name            = _("News Item")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/news_item_plugin.html"
    require_parent  = True
    parent_classes  = ["LatestNewsPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

# ─────────────────────────────────────────────
# Layout Suite
# ─────────────────────────────────────────────

@plugin_pool.register_plugin
class AcademicGridPlugin(CMSPluginBase):
    model           = AcademicGridPluginModel
    name            = _("Academic Section Builder")
    module          = _("Ambika: Layout")
    render_template = "cms/plugins/academic_grid.html"
    allow_children  = True
    child_classes   = ["AcademicItemPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class AcademicItemPlugin(CMSPluginBase):
    model           = AcademicItemPluginModel
    name            = _("Academic Block Item")
    module          = _("Ambika: Layout")
    render_template = "cms/plugins/academic_item.html"
    require_parent  = True
    parent_classes  = ["AcademicGridPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        context["subjects"] = [s.strip() for s in instance.subjects.split("\n") if s.strip()]
        return context

@plugin_pool.register_plugin
class SchoolStatsPlugin(CMSPluginBase):
    model           = SchoolStatsPluginModel
    name            = _("School Statistics")
    module          = _("Ambika: Content")
    render_template = "cms/plugins/school_stats.html"
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        context["stats"] = [
            {"label": instance.stat1_label, "value": instance.stat1_value},
            {"label": instance.stat2_label, "value": instance.stat2_value},
            {"label": instance.stat3_label, "value": instance.stat3_value},
            {"label": instance.stat4_label, "value": instance.stat4_value},
        ]
        return context

# ─────────────────────────────────────────────
# Advanced UI
# ─────────────────────────────────────────────

@plugin_pool.register_plugin
class TestimonialCarousel(CMSPluginBase):
    model           = TestimonialCarouselModel
    name            = _("Testimonial Slider")
    module          = _("Ambika: Advanced UI")
    render_template = "cms/plugins/testimonial_slider.html"
    allow_children  = True
    child_classes   = ["TestimonialItemPlugin"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class TestimonialItemPlugin(CMSPluginBase):
    model           = TestimonialItemModel
    name            = _("Testimonial Item")
    module          = _("Ambika: Advanced UI")
    render_template = "cms/plugins/testimonial_item.html"
    require_parent  = True
    parent_classes  = ["TestimonialCarousel"]
    cache           = False

    def render(self, context, instance, placeholder):
        context["instance"] = instance
        return context
