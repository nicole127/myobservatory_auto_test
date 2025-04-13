import os
from pathlib import Path

class UIConfig:
    DEFAULT_WAIT = 10  # 默认等待时间(秒)
    APPIUM_SERVER = "http://localhost:4723"  # Appium服务器地址

    # 路径配置
    PROJECT_ROOT = Path(__file__).parent.parent
    SCREENSHOT_DIR = PROJECT_ROOT / "reports" / "screenshots"

    # 创建目录
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    # 报告配置
    ALLURE_REPORT_DIR = PROJECT_ROOT / "reports" / "allure"
    HTML_REPORT_DIR = PROJECT_ROOT / "reports" / "html"