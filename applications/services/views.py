from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from django.utils.decorators import method_decorator

# from .forms import RequestQuoteContactForm
from applications.services.models import Pricing
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from django.views.decorators.cache import cache_page

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


class ServiceListView(TemplateView):
    template_name = "pages/services.html"

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)


class ServiceView(TemplateView):
    category = Category
    template_name = "pages/service.html"
    # form_class = RequestQuoteContactForm

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        return get_object_or_404(self.category, slug=kwargs.get("slug"))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["category"] = self.get_object(**kwargs)
        context["form"] = self.form_class()
        return context
