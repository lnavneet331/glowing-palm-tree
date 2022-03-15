from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=64, help_text = "Enter Name of Scholarship")
    providedby = models.CharField(max_length=64, verbose_name = "Provided By", help_text="Enter name of sponsor or organization")
    eligibilitycriteria = models.CharField(max_length=512, verbose_name = "Eligibility Criteria", help_text="Enter Eligibility Criteria")
    exam = models.CharField(max_length=64, help_text="Enter if any exam is required")
    scholarshipamount = models.CharField(max_length = 18, verbose_name = "Scholarship Amount")
    applicationfees = models.CharField(max_length = 18, verbose_name = "Application Fees")
    deadline = models.CharField(max_length=32)
    link = models.CharField(max_length=128, help_text="Enter 404 if not available")

    def __str__(self):
        return f"{self.id}: {self.name} awarded by {self.providedby} requires {self.eligibilitycriteria} and {self.exam} can get you upto {self.scholarshipamount} and application fees of {self.applicationfees} must be paid until {self.deadline}"


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField(max_length=4098)

    def __str__(self):
        return self.email