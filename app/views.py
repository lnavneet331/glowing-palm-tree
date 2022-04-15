from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import App
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'app/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

@login_required
def index(request):
    search_post = request.GET.get('search')
    if search_post:
        apps = App.objects.filter(Q(name__contains=search_post) | Q(providedby__contains=search_post) | Q(eligibilitycriteria__contains=search_post) |Q(exam__contains=search_post) | Q(scholarshipamount__contains=search_post) | Q(applicationfees__contains=search_post) | Q(deadline__contains=search_post) |Q(link__contains=search_post))
    else:
        apps = App.objects.all().order_by("-scholarshipamount")
    return render(request, "app/index.html",{
        "apps":apps
    })

@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'app/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'app/contact.html', context)

def about(request):
    return render(request, "app/about.html")

def landing(request):
    return render(request, "app/landing.html")

def category(request):
    search_post = request.GET.get('dropdown')
    search_level = request.GET.get('level')
    search_salary = request.GET.get('salary')
    if search_post:
        apps = App.objects.filter(Q(category=search_post) & Q(levels=search_level))
    else:
        apps = App.objects.all().order_by("-name")
    return render(request, "app/filter.html",{
        "apps":apps
    })