from .base_page import BasePage
from .locators import LoginPageLocators
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGINPAGE_LOGINFORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGINPAGE_REGISTERFORM), "Register form is not presented"
        
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys((email))
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys((password))
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM).send_keys((password))
        self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON).click()