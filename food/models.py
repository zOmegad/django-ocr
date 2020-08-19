from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name=models.CharField(max_length=200)
	nutriscore=models.IntegerField()
	category = models.ForeignKey('Category',
    on_delete=models.CASCADE, null=True)

class Category(models.Model):
	name=models.CharField(max_length=200)
	products = models.ManyToManyField(Product, related_name='products')

class SavedProduct(models.Model):
	product = models.ForeignKey(Product,
    on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')