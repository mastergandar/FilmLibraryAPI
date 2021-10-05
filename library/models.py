from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Library(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class LibraryProducts(models.Model):
    film = models.ForeignKey('films.Film', on_delete=models.CASCADE, unique=True)

    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='product')
