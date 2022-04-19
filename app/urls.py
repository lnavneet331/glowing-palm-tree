from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.landing, name="landing"),
    path("index/", views.index, name = "index"),
    path("contact/", views.contact_view, name="contact"),
    path("about/", views.about, name="about"),
    path("filter/", views.category, name="filter"),
    path("listing/<str:listing_id>", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_comment/<str:listing_id>", views.add_comment, name="add_comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("toggle_watchlist/<str:listing_id>", views.toggle_watchlist, name="toggle_watchlist"),
    path("listing/<str:listing_id>", views.listing, name="listing"),
]