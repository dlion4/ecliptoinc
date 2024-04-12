from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from .models import Position, Division


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

    # @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args: Any, **kwargs: Any) -> Any:
        return super().dispatch(*args, **kwargs)


class AboutView(TemplateView):

    template_name = "pages/about.html"


class CareersView(TemplateView):
    positions = Position

    template_name = "pages/careers.html"

    # @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["positions"] = self.positions.objects.all()  # type: ignore
        return context


class CareerPositionView(TemplateView):
    positions = Position

    template_name = "pages/career.html"

    # @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.positions,
            slug=kwargs.get(
                "career_slug",
            ),
        )

    def fetch_related(self, **kwargs):
        return (
            self.positions.objects.filter(division=self.get_object(**kwargs).division)
            .all()
            .exclude(pk=self.get_object(**kwargs).pk)
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["position"] = self.get_object(**kwargs)  # type: ignore
        context["related_positions"] = self.fetch_related(**kwargs)  # type: ignore
        return context


class ContactView(TemplateView):
    template_name = "pages/contact.html"