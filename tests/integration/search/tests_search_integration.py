from django.urls import reverse
from django.test import TestCase

from food.models import Product, Category

class SearchPageTestCase(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(pk=1, name="Viande")
        self.food = Product.objects.create(name='Jambon', nutriscore=1,
        category_id=1)

    def test_search_product_return_the_product(self):
        response = self.client.get('/search/', {'query': 'Jambon'})
        self.assertEqual(response.context['product'], self.food)
        self.assertEqual(response.status_code, 200)

    def test_search_non_existing_product_return_nil_query(self):
        response = self.client.get('/search/', {'query': 'Poisson'})
        self.assertEqual(response.context['nil_query'], 'Poisson')
        self.assertEqual(response.status_code, 200)

    def test_none_search_redirect_home(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 302)
