from django.db import models
from django.urls import reverse_lazy


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=50)
    product = models.ManyToManyField(Product, verbose_name='Product')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('main')

class FAQ(models.Model):
    question = models.TextField(max_length=500)
    answer = models.CharField(max_length=250)