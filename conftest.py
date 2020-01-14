from selenium import webdriver
import pytest
import logging
from datetime import datetime


@pytest.fixture(scope="session")
def driver_init(request):
    driver = webdriver.Chrome(executable_path='drivers/chromedriver')
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def logger_init(request):
    logger1 = logging.getLogger('logger')
    fh = logging.FileHandler('test_logs/test_case_{}.txt'.format(datetime.now()))
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # Need more code here to differentiate the logging per thread
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger1.addHandler(fh)
    logger1.addHandler(ch)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "logger", logger1)
    logger1.setLevel(logging.INFO)
    logger1.info('Created logger.')

    yield logger1
