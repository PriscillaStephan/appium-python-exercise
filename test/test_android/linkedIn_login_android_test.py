import pytest

from test.test_android.page.linkedIn_login_android_page import LoginPage
from test.test_android.config.conftest import *

class Test_linkedIn_login:

    @pytest.fixture(autouse=True)
    def driver_setUp(self, create_driver):
        self.driver = create_driver

    def test_log(self):
        login = LoginPage(self.driver)
        login.click_cancel_button_If_visible()
        login.click_Sign_In_button()
        login.enter_username()
        login.enter_password()
        login.click_Sign_In_button_to_log_in()
