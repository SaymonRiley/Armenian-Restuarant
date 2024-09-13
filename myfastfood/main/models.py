from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_small = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price_large =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.title



class Person(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to='media')
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    twitter_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    

    def __str__(self) -> str:
        return self.title
    