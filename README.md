# 一、整体设计思路
本次任务旨在对 “香港天文台 MyObservatory” 应用的 9 天天气预报页面进行自动化测试，包括 App UI 测试和 API 测试。采用行为驱动开发（BDD）模式，使用 Python 结合 Appium 进行移动测试，利用 Pytest 框架编写测试用例并生成测试报告，借助 Page Object 模式管理页面元素，实现代码的可维护性和复用性。同时，通过日志记录测试过程，确保测试的可追溯性。
# 二、技术选型
编程语言：Python，因其简洁易读、丰富的库支持，适合自动化测试开发。
移动测试框架：Appium，可跨平台进行移动应用自动化测试，支持多种语言和移动操作系统。
测试框架：Pytest，功能强大，支持 BDD 风格的测试用例编写，可方便地进行参数化、生成测试报告等操作。
BDD 框架：Behave，用于实现 BDD 风格的测试，使测试用例更接近自然语言描述，便于理解和维护。
日志库：logging，Python 标准库，用于记录测试过程中的详细信息。
测试报告生成库：Allure - Pytest，生成美观、详细的测试报告，展示测试结果和执行过程。
# 三、目录结构
```plaintext
myobservatory_tests/
│
├── appium_driver/
│   └── driver_setup.py  # Appium驱动配置文件
│
├── data/
│   └── test_data.csv  # 测试数据文件
│
├── features/
│   ├── steps/
│   │   ├── app_ui_steps.py  # App UI测试步骤定义
│   │   └── api_steps.py  # API测试步骤定义
│   ├── app_ui.feature  # App UI测试场景描述
│   └── api.feature  # API测试场景描述
│
├── pages/
│   └── forecast_page.py  # 9天天气预报页面元素定位和操作方法
│
├── reports/
│   └── allure/  # Allure测试报告生成目录
│
├── tests/
│   └── conftest.py  # Pytest配置文件
│
├── logs/
│   └── test.log  # 测试日志文件
│
├── requirements.txt  # 项目依赖库文件
├── README.md  # 项目说明文件
└── setup.py  # 项目安装脚本
```

