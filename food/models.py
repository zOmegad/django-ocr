from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    nutriscore = models.IntegerField()
    nutriscore_grade = models.CharField(max_length=10, default="x")
    image = models.URLField(
        null=False, default="https://blog.rahulbhutani.com/wp"
        "-content/uploads/2020/05/Screenshot-2018-12-16-at-21.06.29.png")
    url = models.URLField(
        null=False,
        default="https://world.openfoodfacts.org/")
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return self.name
