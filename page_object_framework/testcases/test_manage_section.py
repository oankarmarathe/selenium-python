import unittest
from selenium import webdriver
import time

from values import strings
from pageobjects.manage_section import ManageSection


class TestManageSection(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(strings.login_url)

    def test_add_designation(self):
        manage = ManageSection(self.driver)
        manage.login()
        manage.add_designation()

    def test_add_customer(self):
        manage = ManageSection(self.driver)
        manage.login()
        manage.add_customer()

    def test_add_employee(self):
        manage = ManageSection(self.driver)
        manage.login()
        manage.add_employee()

    def test_add_department(self):
        manage = ManageSection(self.driver)
        manage.login()
        manage.add_department()

    def test_add_job_template(self):
        manage = ManageSection(self.driver)
        manage.login()
        manage.add_job_template()

    def logout(self):
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    def tearDown(self):
        self.logout()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
