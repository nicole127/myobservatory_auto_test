import subprocess
import os
from pathlib import Path

def run_api_tests():
    """run api tests"""
    # 获取当前脚本所在目录
    project_root = Path(__file__).parent
    print(project_root)
    api_tests_dir = project_root / "api_tests"
    # 确定报告目录是否存在，不存在则新建
    reports_dir = api_tests_dir / "reports"
    reports_dir.mkdir(exist_ok=True)
    # 切换到api_tests目录
    os.chdir(api_tests_dir)
    # 执行behave UI自动化生成HTML格式的报告
    subprocess.run('pytest')
    # 返回原始工作目录
    os.chdir(project_root)


def run_ui_tests():
    """run ui tests"""
    # 获取当前脚本所在目录
    project_root = Path(__file__).parent
    ui_tests_dir = project_root / "ui_tests"
    # 确定报告目录是否存在，不存在则新建
    reports_dir = ui_tests_dir / "reports"
    reports_dir.mkdir(exist_ok=True)
    # 切换到ui_tests目录
    os.chdir(ui_tests_dir)
    # 执行behave UI自动化生成HTML格式的报告
    behave_cmd = [
        'behave',
        '-f', 'behave_html_formatter:HTMLFormatter',
        '-o', 'reports/report.html',
        '--no-capture'
    ]
    subprocess.run(behave_cmd)
    # 返回原始工作目录
    os.chdir(project_root)


if __name__ == "__main__":
    # run_api_tests()
    run_ui_tests()