from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from datetime import datetime,timedelta


class ForecastPage(BasePage):
    # 九天预报滚动框
    roll_box = (AppiumBy.XPATH, '//*[@resource-id="hko.MyObservatory_v1_0:id/mainAppSevenDayView"]/android.widget.LinearLayout')
    # 九天预报第day_offset天
    def get_day_forecast(self, day_offset):
        # 九天预报滚动框
        self.find_element(self.roll_box)
        # 滚动到第day_offset天（根据content-desc定位）
        target_date = (datetime.now()+timedelta(days=day_offset)).strftime('%-m月%-d日')
        day_forecast = self.find_element((AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().descriptionContains("{target_date}"))')
        )
        return day_forecast

