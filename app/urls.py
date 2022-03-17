from django.urls import path
from . import views

urlpatterns = [
    path("", views.New_Landing, name="New_Landing"),
    path("index/", views.index, name = "index"),
    path("contact/", views.contact_view, name="contact"),
    path("about/", views.about, name="about")
]