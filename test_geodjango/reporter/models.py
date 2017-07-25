from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Incident(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    manager = models.GeoManager()

    def __str__(self):
        return self.name
