from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def product_added(self):
        a_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE)
        assert ProductPageLocators.MESSAGES in a_message.text, "Товар добавлен в корзину"
        print("Товар добавлен успешно")