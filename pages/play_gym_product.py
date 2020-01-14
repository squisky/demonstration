import pytest
from selenium.webdriver.common.by import By

from pages.base_page_element import BasePageElement
from pages.base_product import BaseProduct


class PlayGymElement(BasePageElement):
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[contains(@name, "add")]/span')


class PlayGymProduct(BaseProduct):
    """ Product page for the Play Gym"""

    def __init__(self, driver):
        BaseProduct.__init__(self, driver)
        self.price = "{0:.2f}".format(140.00)  # could have a db call to retrieve price value here
        self.directory = self.directory + '/the-play-gym/'
        self.title = 'The Play Gym'

    def go_to_page(self):
        self.logger.info('Going to {} page'.format(self.title))
        self.driver.get(self.directory)

    def click_add_to_cart(self):
        self.logger.info('Click Add to Cart Button')
        self.driver.find_element(*PlayGymElement.ADD_TO_CART_BUTTON).click()
