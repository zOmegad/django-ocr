from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name=models.CharField(max_length=200)
	nutriscore=models.IntegerField()
	image=models.URLField(null=False, default="https://blog.rahulbhutani.com/wp-content/uploads/2020/05/Screenshot-2018-12-16-at-21.06.29.png")
	category = models.ForeignKey('Category',
    on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=200)
	products = models.ManyToManyField(Product, related_name='products')

	def __str__(self):
		return self.name
