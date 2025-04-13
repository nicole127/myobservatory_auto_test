from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from .forecast_page import ForecastPage

class MainPage(BasePage):
    # 左上角菜单按钮
    menu_btn = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    # 一级菜单-预报及警告服务
    warm_btn = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="预报及警告服务"]')
    # 二级菜单-九天预报
    nine_weather_btn = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="九天预报"]')

    def navigate_to_9day_forecast(self):
        """navigate to 9day forecast"""
        self.click(self.menu_btn)
        self.click(self.warm_btn)
        self.click(self.nine_weather_btn)
        return ForecastPage(self.driver)