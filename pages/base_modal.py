import logging


class BaseModal(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('logger')
