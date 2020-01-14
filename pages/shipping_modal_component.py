from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_modal import BaseModal
from pages.base_page_element import BasePageElement


class ShippingModalElement(BasePageElement):
    PROCEED_BUTTON = (By.ID, 'btn-proceed-address')
    MAIN_MODAL = (By.ID, 'myModal-container')


class ShippingModalComponent(BaseModal):
    """Shipping Address Modal During Checkout"""

    def __init__(self, driver):
        super(ShippingModalComponent, self).__init__(driver)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 500).until(lambda driver: self.driver.find_element(*ShippingModalElement.PROCEED_BUTTON))

    def click_proceed_button(self):
        self.logger.info('Clicking Proceed Button in Shipping Address Modal')
        self.driver.find_element(*ShippingModalElement.PROCEED_BUTTON).click()
