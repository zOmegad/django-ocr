from django.db import models
from django.contrib.auth.models import User
from food.models import Product


class SavedProduct(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user')

    def __str__(self):
        return self.product.name
