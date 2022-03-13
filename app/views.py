from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import App
from django.db.models import Q

# Create your views here.
def index(request):
    search_post = request.GET.get('search')

    if search_post:
        apps = App.objects.filter(Q(name__contains=search_post) | Q(category__contains=search_post) | Q(period__contains=search_post) |Q(amount__contains=search_post) | Q(link__contains=search_post) | Q(description__contains=search_post) | Q(application_fees__contains=search_post) |Q(organizer__contains=search_post))
    else:
        apps = App.objects.all().order_by("-amount")

    return render(request, "app/index.html",{
        "apps":apps
    })