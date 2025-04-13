from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import logging


class BasePage():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        f'Looking for element with locator:{locator}'
        if isinstance(locator, tuple):
            by, value = locator
            print(by, value)
            if by == AppiumBy.ANDROID_UIAUTOMATOR:
                def custom_condition(driver):
                    return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value)
                return WebDriverWait(self.driver, timeout).until(custom_condition)
            else:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )
        elif isinstance(locator, str) and locator.startswith('new UiScrollable'):
            def custom_condition(driver):
                return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locator)

            return WebDriverWait(self.driver, timeout).until(custom_condition)
        else:
            raise ValueError(f"Unsupported locator type: {type(locator)}")
        # return WebDriverWait(self.driver, timeout).until(
        #     EC.presence_of_element_located(locator)
        # )

    def click(self, locator, timeout=10):
        f'Clicking on element with locator:{locator}'
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        text = element.text
        f"Got text: '{text}' from element with locator: {locator}"
        return text
