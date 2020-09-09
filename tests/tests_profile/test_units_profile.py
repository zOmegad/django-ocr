from django.urls import reverse
from django.test import TestCase

class ProfilePageTestCase(TestCase):
    def test_profile_page_redirect_if_user_logged_out(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
