from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from config.settings import UIConfig


class BasePage():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        # 从配置文件中获取超时时间
        self.timeout = UIConfig.DEFAULT_WAIT

    def find_element(self, locator):
        f'Looking for element with locator:{locator}'
        if isinstance(locator, tuple):
            by, value = locator
            print(by, value)
            if by == AppiumBy.ANDROID_UIAUTOMATOR:
                def custom_condition(driver):
                    return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value)
                return WebDriverWait(self.driver, self.timeout).until(custom_condition)
            else:
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located(locator)
                )
        elif isinstance(locator, str) and locator.startswith('new UiScrollable'):
            def custom_condition(driver):
                return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locator)

            return WebDriverWait(self.driver, self.timeout).until(custom_condition)
        else:
            raise ValueError(f"Unsupported locator type: {type(locator)}")

    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def take_screenshot(self, name):
        """take screenshot"""
        self.driver.save_screenshot(f"{UIConfig.SCREENSHOT_DIR}/{name}.png")