import time

from selenium.webdriver.support.ui import Select


class ManageSection:

    def __init__(self, driver):
        self.driver = driver
        self.username_field = self.driver.find_element_by_id(
            "id_username")
        self.password_field = self.driver.find_element_by_id("id_password")
        self.loginbtn = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/form/input[2]")

    def login(self):
        self.username_field.clear()
        self.username_field.send_keys("admin")
        self.password_field.clear()
        self.password_field.send_keys("admin@1234")
        self.loginbtn.click()
        assert self.driver.title.find(":: mpower app") != -1

    def add_designation(self):
        self.driver.find_element_by_partial_link_text("Manage").click()
        self.driver.find_element_by_link_text("Designation").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/h1").text == "Manage Designation"
        time.sleep(2)
        self.driver.find_element_by_link_text("New Designation").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/h2").text == "New Designation"
        designation_name = self.driver.find_element_by_id("id_name")
        designation_name.send_keys("Partner")
        working_hours = self.driver.find_element_by_id("id_working_hours")
        working_hours.clear()
        working_hours.send_keys("8.5")
        min_log_time = self.driver.find_element_by_id("id_min_log_time")
        min_log_time.clear()
        min_log_time.send_keys("8")
        self.driver.find_element_by_name("submit").click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/h1").text == "Manage Designation"
        assert self.driver.find_element_by_xpath(
            "//table[@id='inactive-employees-datatable']/tbody/\
            tr[last()]/td[1]").text == "Partner"

    def add_customer(self):
        self.driver.find_element_by_partial_link_text("Manage").click()
        self.driver.find_element_by_link_text("Customers").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/h1").text == "Manage customers"
        time.sleep(2)
        self.driver.find_element_by_link_text("New customer").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[1]/div/h1").text == "New customer"
        customer_name = self.driver.find_element_by_id("id_name")
        customer_name.send_keys("Shetty Foods")
        customer_addr = self.driver.find_element_by_id("id_address")
        customer_addr.send_keys("Chennai")
        gstin_no = self.driver.find_element_by_id("id_gstin_number")
        gstin_no.send_keys("33TMCDDDDD1234C")
        pan_no = self.driver.find_element_by_id("id_pan_number")
        pan_no.send_keys("DDDDD1234C")
        state_dropdown = Select(self.driver.find_element_by_id("id_state"))
        state_dropdown.select_by_value('6')
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div/form/div[9]/input").click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/h1").text == "Manage customers"
        assert self.driver.find_element_by_xpath(
            "//table[@id='customer-datatable']/tbody/\
            tr[1]/td[1]").text == "Shetty Foods"

    def add_employee(self):
        self.driver.find_element_by_partial_link_text("Manage").click()
        self.driver.find_element_by_link_text("Employees").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/h1").text == "Manage employees"
        time.sleep(2)
        self.driver.find_element_by_link_text("New employee").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/h2").text == "New employee"
        username = self.driver.find_element_by_id("id_username")
        username.send_keys("jitendra")
        first_name = self.driver.find_element_by_id("id_first_name")
        first_name.send_keys("Jitendra")
        last_name = self.driver.find_element_by_id("id_last_name")
        last_name.send_keys("Varma")
        password = self.driver.find_element_by_id("id_password")
        password.send_keys("123")
        email = self.driver.find_element_by_id("id_email")
        email.send_keys("jitendra@fafadiatech.com")
        costing_rate = self.driver.find_element_by_id("id_costing_rate")
        costing_rate.send_keys("500")
        billing_rate = self.driver.find_element_by_id("id_billing_rate")
        billing_rate.send_keys("500")
        designation_dropdown = Select(
            self.driver.find_element_by_id("id_designation"))
        designation_dropdown.select_by_value('7')
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/form/input[2]").click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/h1").text == "Manage employees"
        emp_names = []
        all_employees = self.driver.find_elements_by_xpath(
            "//table[@id='active-employees-datatable']/tbody/\
            tr/td[1]")
        for name in all_employees:
            emp_names.append(name.text)
        assert "Jitendra Varma" in emp_names

    def add_department(self):
        self.driver.find_element_by_partial_link_text("Manage").click()
        self.driver.find_elements_by_link_text("Departments")[1].click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/h1").text == "Manage departments"
        time.sleep(2)
        self.driver.find_element_by_link_text("New department").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[1]/div/h2").text == "New department"
        dept_name = self.driver.find_element_by_id("id_name")
        dept_name.send_keys("SC")
        self.driver.find_element_by_xpath("//span[@role='combobox']").click()
        self.driver.find_elements_by_xpath("//li[@role='treeitem']")[3].click()
        self.driver.find_element_by_class_name("fs-label").click()
        self.driver.find_elements_by_class_name("fs-checkbox")[2].click()
        self.driver.find_elements_by_class_name("fs-checkbox")[4].click()
        self.driver.find_element_by_class_name("fs-label").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div/form/input[2]").click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(
            "//*[@id='parent_container']/div/div[1]/div/h1").text == "SC"

    def add_job_template(self):
        self.driver.find_element_by_partial_link_text("Manage").click()
        self.driver.find_element_by_link_text("Job templates").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/\
            div/div[1]/div/h1").text == "Manage Job Templates"
        time.sleep(2)
        self.driver.find_element_by_link_text("New job template").click()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[1]/div/h1").text == "Create a job template"
        job_template_name = self.driver.find_element_by_id("id_name")
        job_template_name.send_keys("System Administration")
        self.driver.find_element_by_xpath("//span[@role='combobox']").click()
        self.driver.find_elements_by_xpath("//li[@role='treeitem']")[5].click()
        job_task1 = self.driver.find_element_by_id("id_fkeytasks-0-name")
        job_task1.send_keys("Hardware Installation")
        self.driver.find_element_by_id("add").click()
        job_task2 = self.driver.find_element_by_id("id_fkeytasks-1-name")
        job_task2.send_keys("Software Installation")
        self.driver.find_element_by_id("add").click()
        job_task3 = self.driver.find_element_by_id("id_fkeytasks-2-name")
        job_task3.send_keys("System Upgradation")
        self.driver.find_element_by_id("add").click()
        job_task3 = self.driver.find_element_by_id("id_fkeytasks-3-name")
        job_task3.send_keys("New System Setup")
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div/div/form/input[3]").click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/\
            div[1]/div/h1").text == "System Administration"
