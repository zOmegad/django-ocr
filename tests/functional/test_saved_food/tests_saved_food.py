from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

class SavedProductTest(LiveServerTestCase):

    def test_click_on_save_button_saves(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        selenium = webdriver.Firefox(
            executable_path=r'/home/travis/build/'
            'zOmegad/django-ocr/geckodriver', firefox_options=opts)
        selenium.get('http:///accounts/login/')
        username = selenium.find_element_by_id("username_field")
        password = selenium.find_element_by_id("password_field")

        username.send_keys("lol")
        password.send_keys("lol")
        selenium.find_element_by_id("submit_btn").click()

        selenium.get('http://141.94.70.168/search/?query=Jambon')
        save_button = selenium.find_element_by_id('save_btn_59201')
        save_button.click()
        selenium.get('http://141.94.70.168/favorite/my_save_food/')
        food_card = selenium.find_element_by_class_name("card-title")
        self.assertEqual(food_card.text, "Pisellini Primavera")
        selenium.quit()
