from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    images = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=100)
    stock = models.IntegerField()
    active = models.BooleanField()
    
