from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    created_date = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.title

