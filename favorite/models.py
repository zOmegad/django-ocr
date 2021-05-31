from django.db import models
from django.contrib.auth.models import User
from food.models import Product


class SavedProduct(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user')

    def __str__(self):
        return self.product.name
