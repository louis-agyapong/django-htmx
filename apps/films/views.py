from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render

from .forms import RegisterForm
from .models import Film


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


class FilmList(ListView):
    template_name = "films.html"
    model = Film
    context_object_name = "films"

    def get_queryset(self):
        user = self.request.user
        return user.films.all()


def check_username(request):
    """
    check if username is available
    """
    username = request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists.</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available.</div>")


def add_film(request):
    """
    add film to user's list
    """
    name = request.POST.get("film_name")
    # create film
    film = Film.objects.create(name=name)
    # add film to user's list
    request.user.films.add(film)
    films = request.user.films.all()
    # return template with all the users films
    return render(request, "partials/film-list.html", {"films": films})
