import subprocess
from pathlib import Path
from config.settings import UIConfig


def run_ui_tests():
    """执行UI测试并生成报告"""
    # 确保报告目录存在
    UIConfig.ALLURE_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    UIConfig.HTML_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    # 执行Behave测试
    cmd = [
        "behave",
        "features/",
        "--format", "allure_behave.formatter:AllureFormatter",
        "-o", str(UIConfig.ALLURE_REPORT_DIR),
        "--format", "pretty"
    ]
    subprocess.run(cmd, check=True)


    # 生成Allure报告
    subprocess.run([
        "allure", "generate",
        str(UIConfig.ALLURE_REPORT_DIR),
        "-o", str(UIConfig.HTML_REPORT_DIR / "allure"),
        "--clean"
    ], check=True)
    print(f"Allure report generated at: {UIConfig.HTML_REPORT_DIR / 'allure' / 'index.html'}")


if __name__ == "__main__":
    run_ui_tests()