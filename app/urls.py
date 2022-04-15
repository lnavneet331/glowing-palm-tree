from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.landing, name="landing"),
    path("index/", views.index, name = "index"),
    path("contact/", views.contact_view, name="contact"),
    path("about/", views.about, name="about"),
    path("filter/", views.category, name="filter"),
    path("accounts/sign_up", views.sign_up, name="sign-up"),
    path("index/<str:listing_id>", views.listing, name="listing"),
]