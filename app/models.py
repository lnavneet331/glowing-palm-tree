from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    watchlist = models.ManyToManyField("App", blank=True, related_name="watchlist")


class App(models.Model):
    level = [("Undergraduate","UNDERGRADUATE"),
            ("Postgraduate", "POSTGRADUATE"),
            ("Phd", "PhD"),
            ("Others", "OTHERS")]
    categories = [("National","NATIONAL"),
                 ("International", "INTERNATIONAL")]
    name = models.CharField(max_length=4098, help_text = "Enter Name of Scholarship")
    providedby = models.CharField(max_length=4098, verbose_name = "Provided By", help_text="Enter name of sponsor or organization")
    eligibilitycriteria = models.CharField(max_length=4098, verbose_name = "Eligibility Criteria", help_text="Enter Eligibility Criteria")
    exam = models.CharField(max_length=4098, help_text="Enter if any exam is required")
    scholarshipamount = models.CharField(max_length = 4098, verbose_name = "Scholarship Amount")
    applicationfees = models.CharField(max_length = 4098, verbose_name = "Application Fees")
    deadline = models.CharField(max_length=4098)
    link = models.CharField(max_length=4098, help_text="Enter 404 if not available")
    category = models.CharField(choices=categories, blank=True, verbose_name = "Category", max_length=4098, null=True)
    levels = models.CharField(choices=level, blank=True, verbose_name = "Levels", max_length=4098, null=True)
    like = models.ManyToManyField(User, blank=True, related_name="liked_user")
    description = models.TextField(max_length=4098, help_text="Enter Description of Scholarship", verbose_name="Description")

    def __str__(self):
        return f"{self.id}: {self.name} awarded by {self.providedby} requires {self.eligibilitycriteria}, {self.category} citizenship and {self.exam} can get you upto {self.scholarshipamount} and application fees of {self.applicationfees} must be paid until {self.deadline}"


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField(max_length=4098)

    def __str__(self):
        return self.email


class Comment(models.Model):
    listing = models.ForeignKey(App, on_delete=models.CASCADE, related_name="comments", null=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)
    content = models.TextField(verbose_name="Comment", default="")
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.commenter} commented on {self.listing} ({self.timestamp.date()})"

class Profile(models.Model):
    income_groups = [("0-100000", "0-100000"), ("100001-500000", "100001-500000"), ("500001-1000000", "500001-1000001"), ("Greater than 1000000", "GREATER THAN 1000000")]
    branches = [("Computer Science", "COMPUTER SCIENCE"), ("STEM", "STEM"), ("All", "ALL"), ("Commerce", "COMMERCE"), ("Science", "SCIENCE"), ("Engineering", "ENGINEERING"), ("Arts", "ARTS"), ("Law", "LAW"), ("Medicine", "MEDICINE"), ("Others", "OTHERS")]
    castes = [("SC", "SC"), ("ST", "ST"), ("OBC", "OBC"), ("General", "General")]
    degrees = [("BA", "BA"), ("BSc", "BSc"), ("BCom", "BCom"), ("BBA", "BBA"), ("MBA", "MBA"), ("MSc", "MSc"), ("MCom", "MCom"), ("MCA", "MCA"), ("MPhil", "MPhil"), ("PhD", "PhD"), ("Others", "Others")]
    skills = [("Singing", "SINGING"), ("Dancing", "DANCING"), ("Reading", "READING"), ("Writing", "WRITING"), ("Cooking", "COOKING"), ("Sports", "SPORTS"), ("Others", "OTHERS")]
    genders = [("Male", "MALE"), ("Female", "FEMALE"), ("Other", "OTHER"), ("Prefer not to say", "PREFER NOT TO SAY")]
    income = models.IntegerField(choices=income_groups, blank=True, verbose_name = "Income", null=True)
    branch = models.CharField(choices=branches, blank=True, verbose_name = "Branch", max_length=4098, null=True)
    gender = models.CharField(choices=genders, blank=True, verbose_name = "Gender", max_length=4098, null=True)
    marks_10 = models.IntegerField(verbose_name = "10th Marks", blank=True, null=True)
    marks_12 = models.IntegerField(verbose_name = "12th Marks", blank=True, null=True)
    caste = models.CharField(choices=castes, blank=True, verbose_name = "Caste", max_length=4098, null=True)
    degree = models.CharField(choices=degrees, blank=True, verbose_name = "Degree", max_length=4098, null=True)
    skill = models.CharField(choices=skills, blank=True, verbose_name = "Skill", max_length=4098, null=True)