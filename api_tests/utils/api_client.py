import time

import requests
from config.settings import APIConfig
from utils.logger import logger
from datetime import datetime, timedelta


class ForecastAPIClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = APIConfig.BASE_URL

    def get_9day_forecast(self):
        """获取9天天气预报"""
        response = self.session.get(
            f"{self.base_url}{APIConfig.FORECAST_ENDPOINT}",
            timeout=APIConfig.TIMEOUT
        )
        response.raise_for_status()
        return response

    def get_general_situation(self):
        """获取天气概况"""
        try:
            data = self.get_9day_forecast().json()
            assert "general_situation" in data, logger.error("Missing general_situation in response")
            general_situation = data["general_situation"]
            assert isinstance(general_situation, str) and len(general_situation) > 0, logger.error("Invalid general_situation format")
            logger.info(f"Successfully extract general situation: {general_situation}")
            return general_situation
        except Exception as e:
            logger.error(f"Extract general situation failed: {e}")

    def get_forecast_detail(self):
        """获取9天天气预报详情"""
        try:
            data = self.get_9day_forecast().json()
            assert "forecast_detail" in data, logger.error("Missing forecast_detail in response")
            forecast_detail = data["forecast_detail"]
            assert isinstance(forecast_detail, list) and len(forecast_detail) == 9, logger.error("Invalid forecast_detail format")
            logger.info("Successfully extract forecast detail")
            return forecast_detail
        except Exception as e:
            logger.error(f"Extract forecast detail failed: {e}")

    def get_forecast_detail_for_target_date(self, day_offset):
        """按索引获取day_offset天后的天气数据"""
        target_date = (datetime.now() + timedelta(days=day_offset)).strftime("%Y%m%d")

        try:
            if day_offset < 1 or day_offset>9:
                raise ValueError("day_offset must be between 0 and 8")
            data = self.get_9day_forecast().json()
            assert "forecast_detail" in data, logger.error("Missing forecast_detail in response")
            for forecast in data["forecast_detail"]:
                if forecast["forecast_date"] == target_date:
                    logger.info(f"Successfully extract forecast detail for {target_date}: {forecast}")
                    return forecast
        except Exception as e:
            logger.error(f"Extract forecast detail for {target_date} failed: {e}")
