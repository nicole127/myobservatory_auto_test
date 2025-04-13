from appium import webdriver
from appium.options.common.base import AppiumOptions


def before_scenario(context, scenario):
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "15",
        "appium:deviceName": "cc14d7f0",
        "appium:appPackage": "hko.MyObservatory_v1_0",
        "appium:appActivity": "hko.MyObservatory_v1_0/.AgreementPage",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": False
    })

    context.driver = webdriver.Remote("http://localhost:4723", options=options)


def after_scenario(context, scenario):
    context.driver.quit()