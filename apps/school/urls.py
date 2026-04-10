"""URL patterns for the school app."""
from django.urls import path
from . import views

app_name = "school"

urlpatterns = [
    path("news/",          views.news_list,   name="news_list"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("gallery/",       views.gallery,     name="gallery"),
    path("facilities/",    views.facilities,  name="facilities"),
    path("academics/",     views.academics,   name="academics"),
    path("admissions/",    views.admissions,  name="admissions"),
    path("about/",         views.about,       name="about"),
    path("explore/",       views.explore,     name="explore"),
    path("apply/",         views.apply,       name="apply"),
]
