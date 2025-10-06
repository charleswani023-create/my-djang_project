from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    specification = models.TextField(max_length=255)
    quantity_stock = models.IntegerField()
    color = models.CharField(max_length=10)


        