import pytest

from appium.webdriver.common.appiumby import AppiumBy
from test.utils.Base_Page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_Sign_In_button(self):
        self.click(locator=AppiumBy.ID, path="Sign in")

    def enter_username(self):
        self.enter(locator=AppiumBy.XPATH, path='//XCUIElementTypeTextField',
                   value="vijay@gmail.com")

    def enter_password(self):
        self.enter(locator=AppiumBy.XPATH, path='//XCUIElementTypeSecureTextField',
                   value="testpass")

    def click_Sign_In_button_to_log_in(self):
        self.click(locator=AppiumBy.XPATH, path="//XCUIElementTypeButton/XCUIElementTypeStaticText[@name='Sign in']")
