from django.db import models


class FilmCategory(models.IntegerChoices):
    BOEVICK = 0, 'BOEVICK'
    VESTERN = 1, 'VESTERN'
    ARMY = 2, 'ARMY'
    DETEKTIV = 3, 'DETEKTIV'
    KOMEDI = 4, 'KOMEDI'
    KRIMINAL = 5, 'KRIMINAL'
    MELODRAMMA = 6, 'MELODRAMMA'
    FANTASY = 7, 'FANTASY'
    SPORT = 8, 'SPORT'


class Country(models.IntegerChoices):
    NOCOUNTRY = 0, 'NOCOUNTRY'
    USA = 1, 'USA'
    RUSSIA = 2, 'RUSSIA'
    BRITTAN = 3, 'BRITTAN'
