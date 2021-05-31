from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions

class SavedProductTest(LiveServerTestCase):

    def test_click_on_save_button_saves(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        selenium = webdriver.Firefox(
            executable_path=r'//home/jonhson/Downloads/geckodriver-v0.29.1-linux64/geckodriver', firefox_options=opts)
        selenium.get('http://141.94.70.168/accounts/login/')
        username = selenium.find_element_by_id("username_field")
        password = selenium.find_element_by_id("password_field")

        username.send_keys("user_1")
        password.send_keys("azerty12345")
        selenium.find_element_by_id("submit_btn").click()
        selenium.get('http://141.94.70.168/search/?query=+')
        new_product = selenium.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/h5").get_attribute('textContent')
        selenium.find_element_by_xpath('//*[@id="save_btn_160"]').click()
        selenium.get('http://141.94.70.168/favorite/my_save_food/')
        food_card = selenium.find_element_by_class_name("card-title")
        self.assertEqual(food_card.text, new_product)
        selenium.quit()
