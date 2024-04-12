from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from applications.services.models import Category
from typing import Any
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class HomeView(TemplateView):
    category = Category

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = self.category.objects.all()  # type: ignore
        return context

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args: Any, **kwargs: Any) -> Any:
        return super().dispatch(*args, **kwargs)


class AboutView(TemplateView):

    template_name = "pages/about.html"
