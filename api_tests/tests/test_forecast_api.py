import pytest
import requests
from utils.logger import logger
from datetime import datetime,timedelta
from utils.api_client import ForecastAPIClient


class TestForecastAPI:
    """Test the forecast API"""
    @pytest.fixture
    def api_client(self):
        """Initialize the API client"""
        return ForecastAPIClient()

    def test_api_response(self, api_client):
        response = api_client.get_9day_forecast()
        try:
            assert response.status_code==200, logger.error(f"Request failed, got {response.status_code}")
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")

    @pytest.mark.parametrize("day_offset", [
        2,  # Day after tomorrow
        8   # 8 days later
    ])
    def test_relative_humidity_format(self, api_client, day_offset):
        """Extract the relative humidity(e,g,60-85%) for the day after day_offset days"""
        relative_humidity = api_client.get_relative_humidity_by_index(day_offset)
        assert '-' in relative_humidity and '%' in relative_humidity
