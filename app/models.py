from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    watchlist = models.ManyToManyField("App", blank=True, related_name="watchlist")


class App(models.Model):
    level = [("Undergraduate","UNDERGRADUATE"),
            ("Postgraduate", "POSTGRADUATE"),
            ("Phd", "PhD")]
    categories = [("National","NATIONAL"),
                 ("International", "INTERNATIONAL")]
    name = models.CharField(max_length=64, help_text = "Enter Name of Scholarship")
    providedby = models.CharField(max_length=64, verbose_name = "Provided By", help_text="Enter name of sponsor or organization")
    eligibilitycriteria = models.CharField(max_length=512, verbose_name = "Eligibility Criteria", help_text="Enter Eligibility Criteria")
    exam = models.CharField(max_length=64, help_text="Enter if any exam is required")
    scholarshipamount = models.CharField(max_length = 18, verbose_name = "Scholarship Amount")
    applicationfees = models.CharField(max_length = 18, verbose_name = "Application Fees")
    deadline = models.CharField(max_length=32)
    link = models.CharField(max_length=128, help_text="Enter 404 if not available")
    category = models.CharField(choices=categories, blank=True, verbose_name = "Category", max_length=200, null=True)
    levels = models.CharField(choices=level, blank=True, verbose_name = "Levels", max_length=200, null=True)
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