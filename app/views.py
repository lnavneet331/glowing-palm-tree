from django.shortcuts import render
from django.http import HttpResponse
from .models import App

# Create your views here.
def index(request):
    return render(request, "app/index.html",{
        "apps":App.objects.all()
    })