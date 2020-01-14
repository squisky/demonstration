from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.base_page_element import BasePageElement


class CheckoutElement(BasePageElement):
    CART_TOTAL = (By.XPATH, '//*[@class="payment-due__price"]')
    EMAIL = (By.XPATH, '//*[@data-trekkie-id="email_field"]')
    FIRST_NAME_FIELD = (By.XPATH, '//*[@data-trekkie-id="shipping_firstname_field"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@data-trekkie-id="shipping_lastname_field"]')
    ADDRESS1_FIELD = (By.XPATH, '//*[@data-trekkie-id="shipping_address1_google_autocomplete_field"]')
    CITY_FIELD = (By.XPATH, '//*[@data-trekkie-id="shipping_city_field"]')
    ZIP_FIELD = (By.XPATH, '//*[@data-trekkie-id="shipping_zip_google_autocomplete_field"]')
    PHONE_FIELD = (By.XPATH, '//*[@data-trekkie-id="shipping_phone_field"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@data-trekkie-id="continue_to_shipping_method_button"]')


class CheckoutPage(BasePage):
    """ Checkout Page Methods"""

    def __init__(self, driver):
        super(CheckoutPage, self).__init__(driver)
        self.title = 'Information'

    def enter_text(self, locator, string_input):
        element = self.driver.find_element(*locator)
        element.click()
        element.clear()
        element.send_keys(string_input)

    def get_cart_total(self):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*CheckoutElement.CART_TOTAL))
        element = self.driver.find_element(*CheckoutElement.CART_TOTAL)
        return element.text

    def enter_email(self, email):
        self.logger.info('Entering email {}'.format(email))
        self.enter_text(CheckoutElement.EMAIL, email)

    def enter_first_name(self, name_input):
        self.logger.info('Entering first name {}'.format(name_input))
        self.enter_text(CheckoutElement.FIRST_NAME_FIELD, name_input)

    def enter_last_name(self, name_input):
        self.logger.info('Entering last name {}'.format(name_input))
        self.enter_text(CheckoutElement.LAST_NAME_FIELD, name_input)

    def enter_address1(self, address1_input):
        self.logger.info('Entering address1 {}'.format(address1_input))
        self.enter_text(CheckoutElement.ADDRESS1_FIELD, address1_input)

    def enter_city(self, city_input):
        self.logger.info('Entering city {}'.format(city_input))
        self.enter_text(CheckoutElement.CITY_FIELD, city_input)

    def enter_zip(self, zip_input):
        self.logger.info('Entering zip code {}'.format(zip_input))
        self.enter_text(CheckoutElement.ZIP_FIELD, zip_input)

    def enter_phone(self, phone_input):
        self.logger.info('Entering phone {}'.format(phone_input))
        self.enter_text(CheckoutElement.PHONE_FIELD, phone_input)

    def click_continue(self):
        self.logger.info('Clicking continue button.')
        self.driver.find_element(*CheckoutElement.CONTINUE_BUTTON).click()
