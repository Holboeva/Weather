from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.IntegerField()
    flag_url = models.URLField()
    wikipedia_link = models.URLField()
    youtube_link = models.URLField()
