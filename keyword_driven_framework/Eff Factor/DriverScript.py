import ActionKeywords

from ExcelUtils import get_excel_data

all_values = get_excel_data()


def valid_login_test():
    for value in all_values:
        if value == "openBrowser":
            ActionKeywords.openBrowser()
        elif value == "navigate":
            ActionKeywords.navigate()
        elif value == "input_valid_Username":
            ActionKeywords.input_valid_Username()
        elif value == "input_valid_Password":
            ActionKeywords.input_valid_Password()
        elif value == "click_login":
            ActionKeywords.click_login()
        elif value == "post_login_title":
            ActionKeywords.post_login_title()
        elif value == "logout":
            ActionKeywords.click_logout()
        elif value == "closeBrowser":
            ActionKeywords.closeBrowser()


def invalid_login_test():
    for value in all_values:
        if value == "openBrowser":
            ActionKeywords.openBrowser()
        elif value == "navigate":
            ActionKeywords.navigate()
        elif value == "input_invalid_Username":
            ActionKeywords.input_invalid_Username()
        elif value == "input_invalid_Password":
            ActionKeywords.input_invalid_Password()
        elif value == "click_login":
            ActionKeywords.click_login()
        elif value == "login_error_message":
            ActionKeywords.login_error_message()
        elif value == "closeBrowser":
            ActionKeywords.closeBrowser()


if __name__ == '__main__':
    valid_login_test()
    invalid_login_test()
