from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from .models import Position, Division
from .form import ContactForm, NewsletterForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages

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


class ContactView(View):

    template_name = "pages/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_template_names(self, name):
        return (
            """
                <p class="text-md green-700">
                Hello %s, your message was delivered successfully!
                </p>
                """
            % name
        )

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(
                request,
                "<strong>Hello %s!</strong>, your message was delivered successfully!"
                % form.cleaned_data.get("name"),
            )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


from .models import Newsletter


class NewsletterView(View):
    newsletter_form = NewsletterForm
    newsletter = Newsletter

    def post(self, request, *args, **kwargs):
        form = self.newsletter_form(request.POST)
        if form.is_valid():
            newsletter = self.newsletter.objects.filter(  # type:ignore
                email=form.cleaned_data.get("email")
            )  # type:ignore
            if newsletter.exists():
                messages.info(request, "This email is already subscribed!")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            form.save()
            messages.success(request, "You've been subscribed to our newsletter!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
