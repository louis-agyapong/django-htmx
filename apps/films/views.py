from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model

from .forms import RegisterForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Movie App"
        return context


class Login(LoginView):
    template_name = "registration/login.html"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("films:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def check_username(request):
    """
    check if username is available
    """
    username = request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists.")
    else:
        return HttpResponse("This username is available.")
