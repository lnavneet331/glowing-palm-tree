from django.db import models
from django.forms import CharField

# Create your models here.



class App(models.Model):
    name = models.CharField(max_length=64)
    organizer = models.CharField(max_length=64)
    category = models.CharField(max_length=32)
    period = models.CharField(max_length=32)
    amount = models.IntegerField()
    application_fees = models.IntegerField()
    description = models.CharField(max_length=512)
    link = models.URLField(max_length=128)


    def __str__(self):
        return f"{self.id}: {self.name} awarded by {self.organizer} in {self.category} category with period of {self.period} with amount {self.amount} and application fees{self.application_fees} and with description : {self.description}"