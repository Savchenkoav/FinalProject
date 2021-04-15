from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGINPAGE_LOGINFORM = (By.CSS_SELECTOR, "#login_form")
    LOGINPAGE_REGISTERFORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE =(By.CSS_SELECTOR, "div.product_main p.price_color")
    ALLERT_MESSAGE_NAME =(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][1]/div[@class='alertinner ']")
    ALLERT_MESSAGE_NAME_VALUE = (By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][1]/div[@class='alertinner ']/strong")
    ALLERT_MESSAGE_PRICE =(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][3]/div[@class='alertinner ']")
    ALLERT_MESSAGE_PRICE_VALUE =(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][3]/div[@class='alertinner ']//strong")
    
    
    