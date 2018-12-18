import unittest
from selenium import webdriver
import time

from values import strings
from pageobjects.homescreen import HomeScreen
from pageobjects.home_screen_links import HomeScreenLinks


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(strings.base_url)

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_title_is_present()
        home_screen.validate_searchbar_is_present()
        home_screen.validate_nav_bar_options_are_present()
        home_screen.validate_shortcuts_are_visible()

    def test_home_screen_links(self):
        home_screen_links = HomeScreenLinks(self.driver)
        home_screen_links.validate_title_is_present()
        home_screen_links.visit_trending_page()
        home_screen_links.visit_deals_page()
        # home_screen_links.visit_cart_page()
        # home_screen_links.validate_navbar_options()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
