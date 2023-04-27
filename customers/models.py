from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_code = models.TextField( unique=True)
    customer_name = models.TextField()
    customer_address = models.TextField()

    def __str__(self):
        return self.customer_code