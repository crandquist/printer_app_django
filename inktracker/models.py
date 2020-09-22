from django.db import models

# Create your models here.
class Printer(models.Model):
    name = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    vendor = models.CharField(max_length=64)
    num_cartridges = models.IntegerField(default=0)
    cart_on_hand = models.IntegerField(default=0)
    product_url = models.URLField()

class Cartridge(models.Model):
    color = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    vendor = models.CharField(max_length=64)
    product_url = models.URLField()
    quantity = models.IntegerField(default=0)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
