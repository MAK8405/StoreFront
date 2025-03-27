from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField()
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(max_length=255)
    birth_date = models.DateField(auto_now_add=True)
