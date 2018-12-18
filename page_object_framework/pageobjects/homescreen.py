class HomeScreen:

    def __init__(self, driver):
        self.driver = driver
        self.title = self.driver.title
        self.searchbar = self.driver.find_elements_by_xpath(
            ".//input[@role='combobox']")[0]
        self.nav_bar = self.driver.find_element_by_class_name("site-menu")
        self.option1 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/header/div[1]/div[3]/div[2]/a/div/span")
        self.option2 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/header/div[1]/div[3]/div[3]/a/div/span")
        self.option3 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/header/div[1]/div[3]/div[4]/a/div/span")

    def validate_title_is_present(self):
        assert self.title.find("Firstbuy.com") != -1

    def validate_searchbar_is_present(self):
        assert self.searchbar.is_displayed()

    def validate_nav_bar_options_are_present(self):
        assert self.nav_bar.is_displayed()

    def validate_shortcuts_are_visible(self):
        assert self.option1.text == "Trending"
        assert self.option2.text == "Deals"
        assert self.option3.text == "Sign In / Up"
