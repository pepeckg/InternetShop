from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50)

class HashTag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField()
    price = models.FloatField(null=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    hashtags = models.ManyToManyField(
        'products.HashTag',
        blank=True,
        related_name='posts'
    )
    category = models.ManyToManyField(
        'Category',
        blank=True,
        related_name='posts'
    )

    def __str__(self) -> str:
        return f'{self.id} {self.title}'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField()
    characteristics = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
