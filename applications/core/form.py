from .models import Contact, Newsletter
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")

    widgets = {
        "name": forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
        "email": forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "email@example.com"}
        ),
        "message": forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "How can we help you today ?",
                "rows": 5,
            }
        ),
    }

    labels = {
        "name": "Your Name",
        "email": "Your Email",
        "message": "Message",
    }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]

    widgets = {
        "email": forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "email@example.com"}
        )
    }
