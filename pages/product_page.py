from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def test_correct_product_add(self):
        self.test_should_be_basket_message()
        self.test_should_be_product_name_equal()
        self.test_should_be_price_message()
        self.test_should_be_price_equal()
    
    def test_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        
    def test_should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_NAME), "Success message with product name is not presented"
    
    def test_should_be_product_name_equal(self):
        Name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        BasketName = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_NAME_VALUE).text
        assert Name == BasketName, print("'",Name,"'", "name does not match","'",BasketName,"'") 

    def test_should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRICE), "Success message with product price is not presented" 
        
    def test_should_be_price_equal(self):
        Price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        BasketPrice = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRICE_VALUE).text
        assert Price == BasketPrice, print("'",Price,"'", " price does not match ","'",BasketPrice,"'")  
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_NAME), \
        "Success message is presented, but should not be"
        
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_NAME), \
        "Success message is not is_disappeared, but should be"