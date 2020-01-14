import logging


class BasePage(object):
    """ Base class to initialize page for page object"""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('logger')

    def get_current_page_title(self):
        return self.driver.title
