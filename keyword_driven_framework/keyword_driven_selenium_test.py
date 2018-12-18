import time

import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class EcommerceLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_ecommerce_login(self):
        driver = self.driver
        driver.get("https://dev.firstbuy.com/")
        time.sleep(2)
        hover_element1 = driver.find_element_by_link_text("Sign In / Up")
        hover1 = ActionChains(driver).move_to_element(hover_element1)
        hover1.perform()
        time.sleep(5)
        driver.find_element_by_link_text("Sign In").click()
        time.sleep(2)
        input_username = driver.find_element_by_id("username")
        input_username.clear()
        input_username.send_keys("oankar")
        input_password = driver.find_element_by_id("password")
        input_password.clear()
        input_password.send_keys("test123")
        driver.find_element_by_class_name("margin-bottom-none").click()
        time.sleep(5)
        hover_element2 = driver.find_element_by_partial_link_text("oankar")
        hover2 = ActionChains(driver).move_to_element(hover_element2)
        hover2.perform()
        time.sleep(2)
        driver.find_element_by_partial_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
