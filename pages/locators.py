from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGINPAGE_URL="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGINPAGE_LOGINFORM = (By.CSS_SELECTOR, "#login_form")
    LOGINPAGE_REGISTERFORM = (By.CSS_SELECTOR, "#register_form")