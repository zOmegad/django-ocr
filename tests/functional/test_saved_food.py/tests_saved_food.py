from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.auth.models import User

from favorite.models import SavedProduct

class SavedProductTest(LiveServerTestCase):

    def test_click_on_save_button_saves(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/accounts/login/')
        username = selenium.find_element_by_id("username_field")
        password = selenium.find_element_by_id("password_field")

        username.send_keys("admin")
        password.send_keys("admin")
        selenium.find_element_by_id("submit_btn").click()

        selenium.get('http://127.0.0.1:8000/search/?query=Jambon')
        save_button = selenium.find_element_by_id('save_btn_70051')
        save_button.click()
        selenium.get('http://127.0.0.1:8000/favorite/my_save_food/')
        food_card = selenium.find_element_by_class_name("card-title")
        self.assertEqual(food_card.text, "Pomme de terre bistrot")
