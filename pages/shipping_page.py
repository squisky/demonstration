from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.base_page_element import BasePageElement


class ShippingElement(BasePageElement):
    CART_SUBTOTAL = (By.XPATH, '//*[@data-checkout-subtotal-price-target]')
    TAX_TOTAL = (By.XPATH, '//*[@data-checkout-total-taxes-target]')


class ShippingPage(BasePage):
    """Shipping Page Methods"""

    def __init__(self, driver):
        super(ShippingPage, self).__init__(driver)
        self.title = 'Shipping'

    def get_cart_subtotal(self):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*ShippingElement.CART_SUBTOTAL))
        element = self.driver.find_element(*ShippingElement.CART_SUBTOTAL)
        self.logger.info('Cart subtotal is {}'.format(element.text))
        return element.text

    def get_tax_total(self):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*ShippingElement.TAX_TOTAL))
        element = self.driver.find_element(*ShippingElement.TAX_TOTAL)
        self.logger.info('Tax total is {}'.format(element.text))
        return element.text
