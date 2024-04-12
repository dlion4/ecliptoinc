from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import RequestQuoteContactForm
from applications.services.models import Pricing
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


class ServiceView(TemplateView):
    category = Category
    template_name = "services/index.html"
    form_class = RequestQuoteContactForm

    def get_object(self, **kwargs):
        return get_object_or_404(self.category, slug=kwargs.get("slug"))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["category"] = self.get_object(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.service = self.get_object(**kwargs).name
            instance.save()
            form.save()
            messages.success(request, "Your form was submitted successfully")
            return redirect(self.get_object(**kwargs))
        messages.error(request, str(form.errors))
        return redirect(self.get_object(**kwargs))
