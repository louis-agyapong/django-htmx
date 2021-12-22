from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass

    class Meta:
        app_label = "films"


class Film(models.Model):
    name = models.CharField(_("name"), max_length=128, unique=True)
    users = models.ManyToManyField(User, verbose_name=_("users"), related_name="films")
