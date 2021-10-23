from django.conf import settings
from django.db import models

from films.enums import FilmCategory, Country


class Film(models.Model):
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    film_id = models.IntegerField('Film id', default=0)
    name = models.CharField('Film name', max_length=255, default='No name')
    category = models.IntegerField('Category', choices=FilmCategory.choices, default=FilmCategory.BOEVICK.value)
    country = models.IntegerField('Country', choices=Country.choices, default=Country.NOCOUNTRY.value)
    description = models.TextField('Description', default='')
    actor = models.CharField('Actor', max_length=250, default='None')

    image = models.ImageField('Poster', null=True, blank=True, upload_to='images/')

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    link = "Edit"

    def __str__(self):
        return f'# {self.name}'
