from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Items are presented, but should not be"
    def test_should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), "Message is not presented"    