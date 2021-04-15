from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def test_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        
    def test_should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ALLERT_MESSAGE_NAME), "Alert message with product name is not presented"
    
    def test_should_be_product_name_equal(self):
        Name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME ).text
        assert Name in self.browser.find_element(*ProductPageLocators.ALLERT_MESSAGE_NAME).text, "name does not match" 

    def test_should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.ALLERT_MESSAGE_PRICE), "Alert message with product price is not presented" 
        
    def test_should_be_price_equal(self):
        Price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert Price in self.browser.find_element(*ProductPageLocators.ALLERT_MESSAGE_PRICE_VALUE).text, "Price does not match" 
    