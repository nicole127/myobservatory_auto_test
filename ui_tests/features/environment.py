import yaml
from appium import webdriver
from appium.options.common.base import AppiumOptions
from config.settings import UIConfig
from requests import options
from utils.logger import logger


def before_scenario(context, scenario):
    try:
        # 从配置文件读取设备信息+APPIUM_SERVER
        with open("config/devices.yaml") as f:
            device = yaml.safe_load(f)

        context.driver = webdriver.Remote(
            command_executor=UIConfig.APPIUM_SERVER,
            options=AppiumOptions().load_capabilities(device["android_device"])
        )
    except Exception as e:
        logger.error(f"Failed to initialize Appium driver: {e}")
        raise


def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.take_screenshot(f"Failed_{scenario.name}")
    context.driver.quit()