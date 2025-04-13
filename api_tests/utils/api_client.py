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
        """获取9日天气预报"""
        response = self.session.get(
            f"{self.base_url}{APIConfig.FORECAST_ENDPOINT}",
            timeout=APIConfig.TIMEOUT
        )
        response.raise_for_status()
        return response

    def get_relative_humidity_by_index(self, day_offset):
        """按索引获取湿度数据，获取day_offset天后的湿度数据"""
        target_date = (datetime.now() + timedelta(days=day_offset)).strftime("%Y%m%d")
        try:
            if day_offset < 0 or day_offset>8:
                raise ValueError("day_offset must be between 0 and 8")
            data = self.get_9day_forecast().json()
            assert "forecast_detail" in data, logger.error("Missing forecast_detail in response")
            relative_humidity = None

            for forecast in data["forecast_detail"]:
                if forecast["forecast_date"] == target_date:
                    min_rh = forecast["min_rh"]
                    max_rh = forecast["max_rh"]
                    relative_humidity = f"{min_rh}-{max_rh}%"
                    if min_rh and 0 <= min_rh <= 100 and max_rh and 0 <= max_rh <= 100:
                        relative_humidity = f"{min_rh}-{max_rh}%"
                        logger.info(f"Successfully extract relative humidity {relative_humidity} for the {target_date}")
                        return relative_humidity
            assert relative_humidity, logger.error(f"Extract relative humidity for the {target_date} failed")

        except Exception as e:
            logger.error(f"Extract relative humidity for the {target_date} failed:{e}")
