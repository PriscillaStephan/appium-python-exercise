import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver

@pytest.fixture(autouse=True)
def create_driver():
    dc = {'platformName': 'android', 'deviceName': 'Nokia G20', 'osVersion': '12'}
    options = UiAutomator2Options()
    options.load_capabilities(dc)
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", options=options)
    driver.activate_app('com.linkedin.android')
    return driver
