import unittest
from selenium import webdriver
import time

from values import strings
from pageobjects.dashboard_test import Dashboard


class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(strings.login_url)

    def test_login(self):
        dashboard = Dashboard(self.driver)
        dashboard.login_with_invalid_data()
        dashboard.login_with_valid_data()

    def test_dashboard(self):
        dashboard = Dashboard(self.driver)
        dashboard.login_with_valid_data()
        dashboard.post_login_links()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
