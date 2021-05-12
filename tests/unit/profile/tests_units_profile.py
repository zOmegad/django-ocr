from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class ProfilePageTestCase(TestCase):

    def setUp(self):
        self.current_user = User.objects.create_user('foo', password='bar')

    def test_profile_page_redirect_if_user_logged_out(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_page_return_200_if_user_logged_in(self):
        self.client.force_login(self.current_user)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
