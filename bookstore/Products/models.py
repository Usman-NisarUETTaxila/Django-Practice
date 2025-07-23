from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def get_absolute_url(self):
        return reverse("products:show_product", kwargs={"id": self.id})
