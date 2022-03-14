from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import App
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
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