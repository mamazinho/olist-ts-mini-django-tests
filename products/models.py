from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    class Meta:
        managed = True
