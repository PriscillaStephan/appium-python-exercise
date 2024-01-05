import pytest

from test.test_ios.page.linkedIn_login_ios_page import LoginPage
from test.test_ios.config.conftest import *

class Test_linkedIn_login:

    @pytest.fixture(autouse=True)
    def driver_setUp(self, create_driver):
        self.driver = create_driver

    def test_log(self):
        login = LoginPage(self.driver)
        login.click_Sign_In_button()
        login.enter_username()
        login.enter_password()
        login.click_Sign_In_button_to_log_in()
