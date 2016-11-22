from django.db import models


# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_category


class Product(models.Model):
    name_product = models.CharField(max_length=100, blank=True)
    description_product = models.CharField(max_length=1000, blank=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name_product
