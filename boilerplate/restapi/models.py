from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    base_price = models.IntegerField()
    description = models.CharField(max_length=128)
    weight = models.FloatField()
    category = models.CharField(max_length=32)
