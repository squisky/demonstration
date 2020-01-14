from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import settings
from pages.base_page import BasePage
from pages.base_page_element import BasePageElement


class CartElement(BasePageElement):
    CART_SUBTOTAL = (By.XPATH, '//*[@class="cart-summary"]/dl/dd')
    CHECKOUT_BUTTON = (By.XPATH, '//*[@name="checkout"]')


class CartPage(BasePage):
    """Cart Page methods"""

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)
        self.directory = settings.LOVEVERY_URL + '/cart'
        self.title = 'Your Shopping Cart'

    def get_cart_total(self):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*CartElement.CART_SUBTOTAL))
        element = self.driver.find_element(*CartElement.CART_SUBTOTAL)
        self.logger.info('Subtotal found is: {}'.format(element.text))
        return element.text

    def click_checkout_button(self):
        self.logger.info('Clicking Checkout Button')
        self.driver.find_element(*CartElement.CHECKOUT_BUTTON).click()
