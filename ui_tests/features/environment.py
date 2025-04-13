from appium import webdriver
from appium.options.common.base import AppiumOptions


def before_scenario(context, scenario):
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "platformVersion": "15",
        "deviceName": "cc14d7f0",
        "appPackage": "hko.MyObservatory_v1_0",
        "appActivity": "hko.MyObservatory_v1_0/.AgreementPage",
        "automationName": "UiAutomator2",
        "noReset": False
    })

    context.driver = webdriver.Remote("http://localhost:4723", options=options)


def after_scenario(context, scenario):
    context.driver.quit()