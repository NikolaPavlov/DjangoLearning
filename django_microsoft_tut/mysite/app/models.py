from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField('artist', max_length=50, blank=True)
    year_formed = models.PositiveIntegerField()


class Album(models.Model):
    name = models.CharField('album', max_length=50, blank=True)
    artist = models.ForeignKey(Artist)
