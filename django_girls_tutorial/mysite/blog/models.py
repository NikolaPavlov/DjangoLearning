from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        date_time_to_be_formated = self.created_date
        formated_date_time = date_time_to_be_formated.strftime("%d/%m/%y %H:%M:%S")
        return formated_date_time + ' ' + self.title
