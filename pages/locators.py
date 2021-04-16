from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGINPAGE_LOGINFORM = (By.CSS_SELECTOR, "#login_form")
    LOGINPAGE_REGISTERFORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTR_BUTTON = (By.CSS_SELECTOR,"[name='registration_submit']")
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE =(By.CSS_SELECTOR, "div.product_main p.price_color")
    SUCCESS_MESSAGE_NAME =(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][1]/div[@class='alertinner ']")
    SUCCESS_MESSAGE_NAME_VALUE = (By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][1]/div[@class='alertinner ']/strong")
    SUCCESS_MESSAGE_PRICE =(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][3]/div[@class='alertinner ']")
    SUCCESS_MESSAGE_PRICE_VALUE =(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' alert ')][3]/div[@class='alertinner ']//strong")
    
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR,".basket-items")
    MESSAGE_EMPTY = (By.XPATH,"//div[@id='content_inner']/p")
    
    
    
    