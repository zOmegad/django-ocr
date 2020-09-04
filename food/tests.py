from django.urls import reverse
from django.test import TestCase

from food.models import Product

class IndexPageTestCase(TestCase):
    def test_index_page_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class ShowPageTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Pasta", nutriscore=1,)
        self.food = Product.objects.get(pk=1)

    def test_show_with_product_returns_200(self):
        response = self.client.get(reverse('show', args=[self.food.id]))
        self.assertEqual(response.status_code, 200)

class ProductPageTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Pasta", nutriscore=1,)
        self.food = Product.objects.get(pk=1)
