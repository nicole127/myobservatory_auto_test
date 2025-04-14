# 项目介绍
collapsed:: true
	- 本项目针对香港天文台官方应用 ​**MyObservatory**​ 的 ​**9日天气预报功能**​ 进行自动化测试，采用 ​**分层设计**， ​**UI测试**​ 和 ​**API测试**​ 完全解耦，独立运行，互不影响
- # ​ 项目架构
	- ## ​ Task 1：UI自动化测试 (`ui_tests/`)​ ​
		- ### ​技术栈
		  collapsed:: true
			- **编程语言**：`Python`
			- ​**测试框架**​：`Behave`（行为驱动开发，BDD）
			- ​**自动化工具**​：`Appium`（移动端自动化测试）
			- ​**设计模式**​：`Page Object Model (POM)`，提高代码可维护性
			- ​**报告生成**​：`Allure`（可视化测试报告）
		- ### 项目架构
		  collapsed:: true
			- ```
			  myobservatory_tests/
			  ├── ui_tests/					# UI测试
			  │   ├── features/				# BDD
			  │   │   ├── steps/				# 步骤实现
			  │   │   │   └── forecast_steps.py 
			  │   │   ├── environment.py		# 全局配置：前置/后置操作
			  │   │   └── forecast.feature	# 定义测试场景
			  │   ├── pages/					# 封装页面操作逻辑
			  │   │   ├── base_page.py		# 页面基础操作
			  │   │   ├── agreement_page.py	# 隐私协议页面
			  │   │   ├── main_page.py		# 主页面
			  │   │   ├── popup_page.py		# 弹窗
			  │   │   └── forecast_page.py	# 九天预报页面
			  │   ├── config/					# 配置管理
			  │   │   ├── devices.yaml		# 测试设备信息
			  │   │   └── setting.py			# 全局配置（显式等待超时时间、路径配置等）
			  │   ├── utils/					# 工具类
			  │   │   └── logger.py			# 日志记录模块
			  │   ├── reports/				# 测试报告
			  │   └── logs/					# 日志存储
			  ├── requirements.txt			# 依赖包
			  ├── README.md					# 项目说明文档
			  └── run_tests.py				# 执行测试的脚本文件（执行behave，生成Allure报告）
			  ```
		- ### 设计思路
		  collapsed:: true
			- **Page Object模式**：将每个页面封装为类，元素定位和操作与测试逻辑分离
				- **基类设计**：`BaseObject`结合显示等待封装元素定位、元素点击、截图等操作
				- **页面类继承**：`AgreementPage`、`MainPage`、`PopupPage`、`ForecastPage`继承`BaseObject`
				- **元素定位策略**
					- 优先使用ID定位
					- 添加显示等待
					- 所有定位器按照页面集中管理
			- **Behave行为驱动**：使用自然语言描述测试场景，提高可读性
				- **步骤定义**：`forecast.feature`，关键字`Scenario Outline`结合`Example`实现数据驱动测试
					- ```Gherkin
					  Feature: MyObservatory App UI 9-Day Forecast Test
					    Scenario Outline: Launch the app and check the forecasts for different dates
					      ......
					      Then Check the <day>th day's weather
					      Examples:
					        | day |
					        | 1   |
					        | 5   |
					        | 9   |
					  ```
				- **步骤实现**：`forecast_steps.py`
				- **环境初始化**：`environment.py`，定义前置操作启动设备、后置操作关闭设备
			- **多设备支持**：通过配置文件`devices.yaml`支持不同设备测试
		- ### 测试范围
		  collapsed:: true
			- ✅ 验证 ​**9天预报**​ 的UI展示
			- ✅ 检查 ​**第day天的天气数据**​ 是否正确显示，day参数化配置如1、5、9
		- ### 运行测试
		  collapsed:: true
			- ```bash
			  # 安装依赖
			  pip instaill -r requirements.txt
			  # 运行测试
			  python run_test.py
			  ```
		
	- ## Task 2：API自动化测试（`api_tests/`）
		- ### 技术栈
		  collapsed:: true
			- **编程语言**：`Python`
			- **测试框架**：`pytest`
			- **HTTP请求库**：`requests`
			- **报告生成**：`pytest-html`
		- ### 项目架构
		  collapsed:: true
			- ```Markdown
			  myobservatory_tests/
			  ├── api_tests/					# API测试
			  │   ├── tests/					# 测试用例
			  │   │   └── test_forecat_api.py	# API测试用例
			  │   ├── config/					# 配置管理
			  │   │   └── setting.py			# 全局配置（域名/超时时间等）
			  │   ├── utils/					# 工具类
			  │   │   ├── api_client.py		# 封装HTTP请求客户端
			  │   │   └── logger.py			# 日志记录模块
			  │   ├── reports/				# 测试报告
			  │   └── logs/					# 日志存储
			  ├── pytest.ini					# pytest配置（测试路径/运行参数等）
			  ├── requirements.txt			# 依赖包
			  └── README.md					# 项目说明文档
			  ```
		- ### 设计思路
		  collapsed:: true
			- #### 测试层 (`tests/`)​
				- 定义共享夹具`@pytest.fixture`：`api_client`初始化API客户端
				- 数据驱动测试：`@pytest.mark.parametrize`
				- ```python
				  @pytest.mark.parametrize("day_offset", [
				    2,  # Day after tomorrow
				    8   # 8 days later
				  ])
				  def test_relative_humidity_format(self, api_client, day_offset):
				  ```
			- #### 配置层（`config/settings.py`）
				- 集中管理API全局参数：URL、超时时间、报告配置等
			- #### 工具层(`utils/`)​
				- `api_client.py`：封装HTTP请求和操作
				- `logger.py`​：提供标准化日志记录
		- ### 测试范围​
		  collapsed:: true
			- ✅ 调用 ​**香港天文台官方API**​ 获取9日天气预报数据
			- ✅ 验证 ​**HTTP状态码**​ 和 ​**响应结构**​
			- ✅ 提取 ​**target_date的相对湿度**​（如`60-85%`）并校验格式，target_date可配置化
		- ### 运行测试
		  collapsed:: true
			- ```ba# 安装依赖
			  pip instaill -r requirements.txt
			  # 运行测试
			  pytest
			  py
			  ```
		
- # 安装指南
  collapsed:: true
	- ### 步骤1：克隆代码
		- ```bash
		  git clone https://github.com/yourusername/myobservatory_tests.git
		  cd myobservatory_tests
		  ```
	- ### 步骤2：创建虚拟环境
		- ```bash
		  python -m venv .venv
		  source .venv/bin/activate  # Linux/Mac
		  .\.venv\Scripts\activate   # Windows
		  ```
	- ### 步骤3：安装依赖
		- ```bash
		  # 安装ui_tests依赖
		  pip install -r ui_tests/requirements.txt
		  # 安装api_tests依赖
		  pip install -r api_tests/requirements.txt
		  ```
	- ### 步骤4：运行测试
		- ```bash
		  # 运行ui_tests
		  cd ui_tests && python run_tests.py
		  # 运行api_tests
		  cd api_tests && pytest
		  ```
	- ### 步骤5：查看报告
		- ui_tests：`ui_tests/reports`
		- api_tests：`api_tests/reports`
	
- # 时间花费
  collapsed:: true
	- 环境调试：1.5小时
	- 框架设计：1小时
	- 代码实现：4小时
	- 测试与调试：0.5小时
	- 文档编写：1小时
	- 总计：约8小时