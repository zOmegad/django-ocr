from django.urls import reverse
from django.test import TestCase

from food.models import Product, Category

class SearchPageTestCase(TestCase):
    def setUp(self):
        self.food = Product.objects.create(name='Jambon', nutriscore=1)
        self.food.category.create(name='Viande')

    def test_search_product_return_the_product(self):
        response = self.client.get('/search/', {'query': 'Jambon'})
        print(response.context)
        self.assertEqual(response.status_code, 200)
