import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver
