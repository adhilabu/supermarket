from itertools import product
from pyexpat import model
from django.db import models

# Create your models here.

class FullOrderLine(models.Model):
    order_id = models.TextField()
    product_name = models.TextField()
    product_quantity = models.TextField()
    customer_name = models.TextField()
    gross_amount = models.DecimalField(max_digits=12,decimal_places=4)
    total_amount = models.DecimalField(max_digits=12,decimal_places=4)

class FullOrder(models.Model):
    order_id = models.TextField()
    quantity = models.TextField()
    customer_name = models.TextField()
    total_amount = models.DecimalField(max_digits=12,decimal_places=4)