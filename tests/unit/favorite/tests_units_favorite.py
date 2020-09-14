from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from food.models import Product
from favorite.models import SavedProduct

class FavoritePageTestCase(TestCase):
    def setUp(self):
        self.current_user=User.objects.create_user('foo', password='bar')
        self.client.force_login(self.current_user)
        food = Product.objects.create(name="Jambon", nutriscore=1)
        favorite = SavedProduct.objects.create(product=food, user=self.current_user)

    def test_saved_food_page_redirect_if_user_logged_out(self):
        self.client.logout()
        response = self.client.get(reverse('saved_food'))
        self.assertEqual(response.status_code, 302)

    def test_saved_food_page_return_200_if_user_logged_in(self):
        response = self.client.get(reverse('saved_food'))
        self.assertEqual(response.status_code, 200)
