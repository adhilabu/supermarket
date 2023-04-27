from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    product_code = models.TextField(unique=True)
    product_name = models.TextField()
    unit_price = models.DecimalField(max_digits=5,decimal_places=2)
    tax_percent = models.DecimalField(max_digits=12,decimal_places=4)
    
    def __str__(self):
        return self.product_code