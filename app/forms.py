from django.forms import ModelForm
from .models import Contact, Profile
from captcha.fields import CaptchaField

class ContactForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'