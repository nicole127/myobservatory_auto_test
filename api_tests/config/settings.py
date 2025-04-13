from pathlib import Path


class APIConfig:
    # API配置、
    BASE_URL = "https://pda.weather.gov.hk"
    FORECAST_ENDPOINT = "/sc/locspc/data/fnd_uc.xml"
    TIMEOUT = 15

    # 报告配置
    PROJECT_ROOT = Path(__file__).parent.parent
    HTML_REPORT_DIR = PROJECT_ROOT / "reports" / "html"
    HTML_REPORT_DIR.mkdir(parents=True, exist_ok=True)