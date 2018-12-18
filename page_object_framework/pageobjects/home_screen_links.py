import time

from values import strings


class HomeScreenLinks:

    def __init__(self, driver):
        self.driver = driver
        self.title = self.driver.title
        self.trending = self.driver.get(strings.trending_url)
        self.deals = self.driver.get(strings.deals_url)
        self.cart = self.driver.get(strings.cart_url)
        self.menu_option1 = self.driver.find_elements_by_xpath(
            "//li[@class='has-megamenu']/a")[0]
        self.menu_option2 = self.driver.find_elements_by_xpath(
            "//li[@class='has-megamenu']/a")[1]
        self.menu_option3 = self.driver.find_elements_by_xpath(
            "//li[@class='has-megamenu']/a")[2]
        self.menu_option4 = self.driver.find_elements_by_xpath(
            "//li[@class='has-megamenu']/a")[3]
        self.menu_option5 = self.driver.find_elements_by_xpath(
            "//li[@class='has-megamenu']/a")[4]
        self.menu_option6 = self.driver.find_elements_by_xpath(
            "//li[@class='has-megamenu']/a")[5]
        self.menu_option7 = self.driver.find_elements_by_xpath(
            "//li[@class='has-megamenu']/a")[6]

    def validate_title_is_present(self):
        assert self.title.find("Firstbuy.com") != -1

    def visit_trending_page(self):
        assert self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div[1]/div[1]/\
            div/div[1]/h1").text == "Trending Categories"

    def visit_deals_page(self):
        assert self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div[1]/div[1]/\
            div/div[1]/h1").text == "Deals"

    def visit_cart_page(self):
        assert self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div[1]/div[1]/\
            div/div[1]/h1").text == "Cart"

    def validate_navbar_options(self):
        assert self.menu_option1.text == "Computers & Accessories"
        assert self.menu_option2.text == "Laptops & Accessories"
        assert self.menu_option3.text == "Tablets & Mobiles"
        assert self.menu_option4.text == "Network & Servers"
        assert self.menu_option5.text == "Gaming"
        assert self.menu_option6.text == "Audio"
        assert self.menu_option7.text == "Smart Connect"
