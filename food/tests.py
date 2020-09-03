from django.urls import reverse
from django.test import TestCase

from food.models import Product

class IndexPageTestCase(TestCase):
    def test_index_page_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class ShowPageTestCase(TestCase):
    def test_show_with_product_returns_200(self):
        product = Product.objects.create(name="Pasta", nutriscore=1,)
        food = Product.objects.get(pk=1)
        response = self.client.get(reverse('show', args=[food.id]))
        self.assertEqual(response.status_code, 200)

class ProductsPageTestCase(TestCase):
    
