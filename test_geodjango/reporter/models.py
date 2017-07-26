from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Incident(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100, default='This is picture')
    location = models.PointField(srid=4326)

    @property
    def get_url(self):
        return 'http://localhost:8000/reporters/' + self.pk

    def __str__(self):
        return self.name
