from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import App

# Create your views here.
def index(request):
    return render(request, "app/index.html",{
        "apps":App.objects.all()
    })

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response