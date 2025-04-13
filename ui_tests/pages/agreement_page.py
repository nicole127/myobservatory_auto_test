from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class AgreementPage(BasePage):
    # 免责声明/隐私政策声明-同意按钮
    agree_btn = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/btn_agree')
    # 系统通知-拒绝按钮
    deny_notification = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')
    # 背景存取位置资讯-确定按钮
    confirm_btn = (AppiumBy.ID, 'android:id/button1')
    # 获取当前设备位置-不允许按钮
    deny_location = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')

    def accept_agreements(self):
        """Accept the disclaimer and privacy policy statement."""
        self.click(self.agree_btn)
        self.click(self.agree_btn)

    def handle_permissions(self):
        """Handle the permission requests."""
        self.click(self.deny_notification)
        self.click(self.confirm_btn)
        self.click(self.deny_location)