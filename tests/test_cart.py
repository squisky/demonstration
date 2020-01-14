import pytest

import settings
from helper import helper
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.play_gym_product import PlayGymProduct
from pages.shipping_modal_component import ShippingModalComponent
from pages.shipping_page import ShippingPage


@pytest.mark.usefixtures("driver_init")
@pytest.mark.usefixtures("logger_init")
class TestCart:

    def test_adding_gym_to_cart_and_validate_total_with_tax(self):
        self.logger.info('Starting Add Gym to Cart & Validate Total Test')
        baby_gym_page = PlayGymProduct(self.driver)
        baby_gym_page.go_to_page()
        baby_gym_page.click_add_to_cart()
        cart_page = CartPage(self.driver)
        subtotal = cart_page.get_cart_total()
        self.logger.info('Subtotal was {}'.format(subtotal))
        cart_page.click_checkout_button()
        checkout_page = CheckoutPage(self.driver)
        total = checkout_page.get_cart_total()
        self.logger.info('Total was {}'.format(total))
        checkout_page.enter_email(settings.TEST_EMAIL)
        checkout_page.enter_first_name('B')
        checkout_page.enter_last_name('B')
        checkout_page.enter_address1('Forest Road 1234')
        checkout_page.enter_city('Soda Springs')
        checkout_page.enter_zip('83276')
        checkout_page.enter_phone('1234567890')
        checkout_page.click_continue()
        ShippingModalComponent(self.driver).click_proceed_button()
        shipping_page = ShippingPage(self.driver)
        subtotal = shipping_page.get_cart_subtotal()
        tax_total = shipping_page.get_tax_total()
        # We can implement an Assertion class for better assertions, and take screenshots on fail.
        assert subtotal.replace('$', '') == baby_gym_page.price
        calculated_tax = helper.calculate_tax_total([baby_gym_page.price], settings.IDAHO_TAX_RATE)
        assert tax_total.replace('$', '') == calculated_tax

    def test_show_parallel_tests(self):
        self.logger.info('Starting Parallels Test')
        baby_gym_page = PlayGymProduct(self.driver)
        baby_gym_page.go_to_page()
        baby_gym_page.click_add_to_cart()
        cart_page = CartPage(self.driver)
        subtotal = cart_page.get_cart_total()
        self.logger.info('Subtotal was {}'.format(subtotal))
        cart_page.click_checkout_button()
        checkout_page = CheckoutPage(self.driver)
        total = checkout_page.get_cart_total()
        self.logger.info('Total was {}'.format(total))
        checkout_page.enter_email(settings.TEST_EMAIL)
        checkout_page.enter_first_name('C')
        checkout_page.enter_last_name('C')
        checkout_page.enter_address1('Forest Road 4567')
        checkout_page.enter_city('Soda Springs')
        checkout_page.enter_zip('83276')
        checkout_page.enter_phone('1234567890')
        title = checkout_page.get_current_page_title()
        self.logger.info('Title is {}'.format(title))
        assert title.startswith(checkout_page.title)
