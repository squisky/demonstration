
import settings
from pages.base_page import BasePage


class BaseProduct(BasePage):
    """Abstract Product Page"""
    def __init__(self, driver):
        super(BaseProduct, self).__init__(driver)
        self.price = 0.00
        self.directory = settings.LOVEVERY_URL + '/products'
        self.title = 'Products'

    def go_to_page(self):
        self.logger.info('Going to the {} page'.format(self.title))
