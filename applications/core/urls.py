from django.urls import reverse, path, include


from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/",views.AboutView.as_view(), name="about"),
]
