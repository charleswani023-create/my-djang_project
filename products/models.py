from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    quantity_stock = models.IntegerField()
    specification = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # ✅ new field

    def __str__(self):
        return self.name
