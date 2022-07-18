from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_to_basket.click()

    def product_should_be_added_to_basket(self):
        self.should_be_message_that_product_added_to_basket()
        self.should_be_message_with_total_price()

    def should_be_message_that_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_AFTER_ADDING_TO_BASKET), \
            "Message that product added to the basket is absent"
        product_name_on_the_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_THE_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_on_the_message == product_name, \
            "Product name on the message does not match the product you added"

    def should_be_message_with_total_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_TOTAL_PRICE), \
            "Message with total price is absent"
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert total_price == product_price, "Total price does not match the product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_AFTER_ADDING_TO_BASKET), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_AFTER_ADDING_TO_BASKET), \
            "Success message is not disappeared, but should be"