from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class AgreementPage(BasePage):
    # 免责声明/隐私政策声明-确认按钮
    agree_btn = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/btn_agree')
    # 系统通知-拒绝按钮
    deny_notification = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')
    # 背景存取位置资讯-确定按钮
    confirm_btn = (AppiumBy.ID, 'android:id/button1')
    # 获取当前设备位置-不允许按钮
    deny_location = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')

    # 点击：免责声明+隐私政策声明
    def accept_agreements(self):
        self.click(self.agree_btn)
        self.click(self.agree_btn)

    # 点击：系统通知+背景存取位置资讯+获取当前设备位置
    def handle_permissions(self):
        self.click(self.deny_notification)
        self.click(self.confirm_btn)
        self.click(self.deny_location)