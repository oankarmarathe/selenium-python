import ActionKeywords

from ExcelUtils import get_excel_data

all_values = get_excel_data()


def keyword_driven_test():
    for value in all_values:
        if value == "openBrowser":
            ActionKeywords.openBrowser()
        elif value == "navigate":
            ActionKeywords.navigate()
        elif value == "hover_signin_link":
            ActionKeywords.hover_signin_link()
        elif value == "click_signin":
            ActionKeywords.click_signin()
        elif value == "input_Username":
            ActionKeywords.input_Username()
        elif value == "input_Password":
            ActionKeywords.input_Password()
        elif value == "click_login":
            ActionKeywords.click_login()
        elif value == "waitFor":
            ActionKeywords.waitFor()
        elif value == "hover_username_link":
            ActionKeywords.hover_username_link()
        elif value == "logout":
            ActionKeywords.click_logout()
        elif value == "closeBrowser":
            ActionKeywords.closeBrowser()


if __name__ == '__main__':
    keyword_driven_test()
