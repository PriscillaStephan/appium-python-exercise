from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement


class BasePage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator: str, path: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator, path)))
        self.driver.find_element(by=locator, value=path).click()

    def enter(self, locator: str, path: str, value: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator, path)))
        self.driver.find_element(by=locator, value=path).send_keys(value)

    def isvisible(self, locator: str, path: str, time: float):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((locator, path)))
            return True
        except:
            return False
