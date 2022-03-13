from django.db import models

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
        return self.title
