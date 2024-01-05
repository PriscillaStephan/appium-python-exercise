import pytest

from appium.webdriver.common.appiumby import AppiumBy

from test.utils.Base_Page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_cancel_button_If_visible(self):
        if self.isvisible(locator=AppiumBy.ID, path='com.google.android.gms:id/cancel', time=10):
            self.click(locator=AppiumBy.ID, path='com.google.android.gms:id/cancel')

    def click_Sign_In_button(self):
        self.click(locator=AppiumBy.ID, path='com.linkedin.android:id/growth_prereg_fragment_login_button')

    def enter_username(self):
        self.enter(locator=AppiumBy.ID, path='com.linkedin.android:id/growth_login_join_fragment_email_address',
                   value="vijay@gmail.com")

    def enter_password(self):
        self.enter(locator=AppiumBy.ID, path='com.linkedin.android:id/growth_login_join_fragment_password',
                   value="testpass")

    def click_Sign_In_button_to_log_in(self):
        self.click(locator=AppiumBy.ID, path='com.linkedin.android:id/growth_login_fragment_sign_in')
