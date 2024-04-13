from django.urls import reverse, path, include


from . import views

app_name = "services"
urlpatterns = [
    path("", views.ServiceListView.as_view(), name="services"),
    path("/features", views.FeatureListView.as_view(), name="features"),
    path("<str:slug>/", views.ServiceView.as_view(), name="category"),
]
