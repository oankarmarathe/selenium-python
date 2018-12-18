import time


class Dashboard:

    def __init__(self, driver):
        self.driver = driver
        self.username_field = self.driver.find_element_by_id("id_username")
        self.password_field = self.driver.find_element_by_id("id_password")
        self.loginbtn = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/form/input[2]")

    def login_with_valid_data(self):
        self.username_field.clear()
        self.username_field.send_keys("admin")
        self.password_field.clear()
        self.password_field.send_keys("admin@1234")
        self.loginbtn.click()
        time.sleep(2)
        assert self.driver.title.find(":: mpower app") != -1

    def login_with_invalid_data(self):
        self.username_field.clear()
        self.username_field.send_keys("test")
        self.password_field.clear()
        self.password_field.send_keys("test")
        self.loginbtn.click()
        time.sleep(2)
        assert self.driver.find_element_by_class_name(
            "alert-danger").is_displayed()

    def post_login_links(self):
        time.sleep(5)
        assert self.driver.title.find(":: mpower app") != -1
        assert "ADMIN" in self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/ul[2]/\
            li[1]/a/strong/small").text
        assert "My logs" in self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/ul[2]/li[1]/a").text
        assert "My assignments" in self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/ul[2]/li[2]/a").text
        assert "Assignment monitor" in self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/ul[2]/li[3]/a").text
        assert self.driver.find_element_by_xpath(
            "//span[@role='combobox']").is_displayed()
