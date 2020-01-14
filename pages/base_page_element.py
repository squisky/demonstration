from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement(object):
    """Abstract Page Element Object"""

    def __get__(self, instance, owner):
        pass
