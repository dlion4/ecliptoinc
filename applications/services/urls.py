from django.urls import reverse, path, include


from . import views

app_name = "services"
urlpatterns = [
    path("<str:slug>/", views.ServiceView.as_view(), name="category"),
]
