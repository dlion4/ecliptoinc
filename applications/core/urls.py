from django.urls import reverse, path, include


from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about", views.AboutView.as_view(), name="about"),
    path("careers", views.CareersView.as_view(), name="careers"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("contact/success", views.ContactView.as_view(), name="contact_success"),
    path("newsletter", views.NewsletterView.as_view(), name="newsletter"),
    path("careers/<career_slug>", views.CareerPositionView.as_view(), name="position"),
]
