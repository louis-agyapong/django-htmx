from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "films"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register")
]
