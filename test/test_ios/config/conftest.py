import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.options.ios import XCUITestOptions


@pytest.fixture
def create_driver():
    caps = {"appium:platformVersion": "16.2", "appium:deviceName": "iPhone 8 Plus",
            "appium:udid": "ad4469ca1bc34f9e4fd766bb22696f1ffb0bbd51", "platformName": "iOS",
            "appium:app": "com.linkedin.LinkedIn", "appium:includeSafariInWebviews": True,
            "appium:newCommandTimeout": 3600, "appium:connectHardwareKeyboard": True}
    options = XCUITestOptions()
    options.load_capabilities(caps)
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
