from django.db import models


class FilmCategory(models.IntegerChoices):
    UNCATEGORIZED = 0, 'UNCATEGORIZED'
    BLOCKBUSTER = 1, 'Hard BLOCKBUSTER'


class Country(models.IntegerChoices):
    NOCOUNTRY = 0, 'NOCOUNTRY'
    USA = 1, 'USA'
    RUSSIA = 2, 'RUSSIA'
