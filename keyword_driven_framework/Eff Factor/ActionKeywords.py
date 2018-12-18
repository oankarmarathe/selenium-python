import time


from selenium import webdriver

driver = webdriver.Firefox()


def openBrowser():
    driver.maximize_window()


def navigate():
    driver.get("http://localhost:8000/login/?next=/")
    time.sleep(2)


def input_valid_Username():
    input_username = driver.find_element_by_id("id_username")
    input_username.clear()
    input_username.send_keys("admin")


def input_valid_Password():
    input_password = driver.find_element_by_id("id_password")
    input_password.clear()
    input_password.send_keys("admin@1234")


def input_invalid_Username():
    input_username = driver.find_element_by_id("id_username")
    input_username.clear()
    input_username.send_keys("test")


def input_invalid_Password():
    input_password = driver.find_element_by_id("id_password")
    input_password.clear()
    input_password.send_keys("test")


def click_login():
    driver.find_element_by_xpath(
        "/html/body/div[3]/div/div/form/input[2]").click()


def login_error_message():
    assert driver.find_element_by_class_name("alert-danger").is_displayed()


def post_login_title():
    time.sleep(5)
    assert driver.title.find(":: mpower app") != -1


def click_logout():
    driver.find_element_by_partial_link_text("Logout").click()


def closeBrowser():
    driver.quit()
