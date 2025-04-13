from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class PopupPage(BasePage):
    # 首页弹窗-地球天气新服务-下一页按钮
    next_btn = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/exit_btn')

    def popup_exists(self):
        """Check if the popup exists."""
        try:
            self.find_element(self.next_btn)
            return True
        except:
            return False

    def close_popup(self):
        """Close the popup."""
        self.click(self.next_btn)
        self.click(self.next_btn)
