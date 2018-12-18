import time


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()


def openBrowser():
    driver.maximize_window()


def navigate():
    driver.get("https://dev.firstbuy.com/")
    time.sleep(2)


def hover_signin_link():
    hover_element1 = driver.find_element_by_link_text("Sign In / Up")
    hover1 = ActionChains(driver).move_to_element(hover_element1)
    hover1.perform()
    time.sleep(5)


def click_signin():
    driver.find_element_by_link_text("Sign In").click()
    time.sleep(2)


def input_Username():
    input_username = driver.find_element_by_id("username")
    input_username.clear()
    input_username.send_keys("oankar")


def input_Password():
    input_password = driver.find_element_by_id("password")
    input_password.clear()
    input_password.send_keys("test123")


def click_login():
    driver.find_element_by_class_name("margin-bottom-none").click()


def waitFor():
    time.sleep(5)
    assert driver.title.find("Firstbuy.com") != -1


def hover_username_link():
    hover_element2 = driver.find_element_by_partial_link_text(
        "oankar")
    hover2 = ActionChains(driver).move_to_element(hover_element2)
    hover2.perform()
    time.sleep(2)


def click_logout():
    driver.find_element_by_partial_link_text("Logout").click()


def closeBrowser():
    driver.quit()
