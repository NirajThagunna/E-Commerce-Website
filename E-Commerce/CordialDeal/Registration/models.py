from django.db import models


# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=220)
    image_url = models.CharField(max_length=1080)
    image1 = models.CharField(max_length=1100)
    image2 = models.CharField(max_length=1120)
    image3 = models.CharField(max_length=1140)
    image4 = models.CharField(max_length=1180)


class Order(models.Model):
    product_name = models.CharField(max_length=240)
    price = models.FloatField()
    stock = models.IntegerField()
    product_img = models.CharField(max_length=1300)
    username = models.CharField(max_length=300)
    url = models.CharField(max_length=1500)
    cart = models.CharField(max_length=1800)
