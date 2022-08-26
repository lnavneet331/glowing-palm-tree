from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import App, Comment, User, Profile
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.db.models import Q, Max, Count
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.forms import ModelForm, Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import IntegrityError
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect 
from django.http import JsonResponse
User = get_user_model()

# Create your views here.
class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs["placeholder"] = "Enter comment"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.add_input(Submit("submit", "Add Comment"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        income = request.POST.get("income")
        branch = request.POST["branch"]
        gender = request.POST.get("gender")
        marks_10 = request.POST["marks_10"]
        marks_12 = request.POST["marks_12"]
        caste = request.POST.get("caste")
        degree = request.POST["degree"]
        skill = request.POST.get("skill")
        profile = Profile(username, password, email, income, branch, gender, marks_10, marks_12, caste, degree, skill)
        profile = Profile(username=username, password=password, email=email, income=income, branch=branch, gender=gender, marks_10=marks_10, marks_12=marks_12, caste=caste, degree=degree, skill=skill)
        profile.save()
        alphas, nums, lower, upper = 0, 0, 0, 0
        for i in password:
            if i.isalpha():
                alphas += 1
            if i.isnumeric():
                nums += 1
            if i.islower():
                lower += 1
            if i.isupper():
                upper += 1
        if len(password) < 8 or alphas < 1 or nums < 1 or lower < 1 or upper < 1:
            return render(request, "app/register.html", {
                "message": "Password must be at least 8 characters long and must contain at least one uppercase letter, one lowercase letter, and one number."
            })
        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("landing"))

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

def listing(request, listing_id):
    listing, comments, in_watchlist = listing_page_utility(request, listing_id)
    apps = App.objects.all().order_by("-name")
    return render(request, "app/listing.html",{
        "apps":apps,
        "listing":listing,
        "comments":comments,
        "comment_form":NewCommentForm(),
        "in_watchlist":in_watchlist
    })

def listing_page_utility(request, listing_id):
    listing = App.objects.annotate(name_of_scholarship = Max("name"), provided_by = Max("providedby"), eligibility_criteria = Max("eligibilitycriteria"), exam_what = Max("exam"), scholarship_amount = Max("scholarshipamount"), application_fees = Max("applicationfees"), dead_line = Max("deadline"), link_to_page = Max("link"), cat = Max("category"), level = Max("levels"), descrip = Max("description")).get(id=listing_id)
    comments = Comment.objects.filter(listing=listing)

    if request.user.is_authenticated:
        in_watchlist = listing in request.user.watchlist.all()
    else:
        in_watchlist = False

    return listing, comments, in_watchlist

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
            human = True
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

@login_required
def add_comment(request, listing_id):
    listing, comments, in_watchlist = listing_page_utility(request, listing_id)
    
    form = NewCommentForm(request.POST)

    if form.is_valid():
        content = form.cleaned_data["content"]
        comment = Comment(listing=listing, commenter=request.user, content=content)
        comment.save()
        return HttpResponseRedirect(reverse("listing", args=(listing.id,)))

    else:
        return render(request, "app/listing.html", {
            "listing": listing,
            "comments": comments,
            "comment_form": form,
            "in_watchlist": in_watchlist
        })

@login_required
def watchlist(request):
    return render(request, "app/watchlist.html", {
        "listings": request.user.watchlist.all()
    })

@login_required
def toggle_watchlist(request, listing_id):
    listing, _, in_watchlist = listing_page_utility(request, listing_id)

    if in_watchlist:
        request.user.watchlist.remove(listing)
    else:
        request.user.watchlist.add(listing)

    return HttpResponseRedirect(reverse("listing", args=(listing.id,)))

@login_required
#@csrf_exempt
def like(request):
    if request.method == "POST":
        listing_id = request.POST.get("id")
        is_liked = request.POST.get("is_liked")
        try:
            post = App.objects.get(id=listing_id)
            if is_liked == "no":
                post.like.add(request.user)
                is_liked = "yes"
            elif is_liked == "yes":
                post.like.remove(request.user)
                is_liked == "no"
            post.save()

            return JsonResponse({'like_count':listing.like.count(), 'is_liked':is_liked, "status":201})
        except:
            return JsonResponse({"error":"Scholarship not found", 'status':404})
    return JsonResponse({}, status=400)

@login_required
def profile(request):

    return render(request, "app/profile.html")