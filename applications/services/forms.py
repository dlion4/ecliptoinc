from applications.core.models import RequestQuoteContact
from django import forms
from applications.services.models import Pricing # type: ignore


class RequestQuoteContactForm(forms.ModelForm):
    package = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control py-2 px-2",
                "style": "padding: 0.94rem 1.5rem",
            },
        ),
        choices=(
            ("B", "Basic"),
            ("P", "Premium"),
            ("E", "Enterprise"),
        ),
    )  # type: ignore

    occupation = forms.CharField(
        max_length=100, help_text="What you do, i.e., student, software developer, etc."
    )

    class Meta:
        model = RequestQuoteContact
        fields = ["full_name", "occupation", "email", "package", "message"]
