import pytest
import requests
from utils.logger import logger
from datetime import datetime,timedelta
from utils.api_client import ForecastAPIClient


class TestForecastAPI:
    """Test the forecast API"""
    # 发起1次API请求，作用域为整个模块
    @pytest.fixture(scope="module")
    def api_client(self):
        """Initialize the API client"""
        return ForecastAPIClient()

    def test_api_response(self, api_client):
        """Test the API response status code"""
        response = api_client.get_9day_forecast()
        try:
            assert response.status_code==200, pytest.fail(f"Request failed, got {response.status_code}")
        except Exception as e:
            logger.error(f"Request failed: {e}")
            pytest.fail(f"Request failed: {e}")

    def test_general_situation(self, api_client):
        """Extract the general situation"""
        try:
            general_situation = api_client.get_general_situation()
            assert isinstance(general_situation, str), pytest.fail("General situation is not a string")
            assert len(general_situation) > 0, pytest.fail("General situation is empty")
        except AssertionError as e:
            pytest.fail(f"Extract the general situation failed: {e}")

    def test_forecast_detail(self, api_client):
        """Extract the forecast detail"""
        try:
            forecast_detail = api_client.get_forecast_detail()
            assert isinstance(forecast_detail, list), pytest.fail("Forecast detail is not a list")
            assert len(forecast_detail) == 9, pytest.fail("Forecast detail length is not 9")
        except AssertionError as e:
            pytest.fail(f"Extract the forecast detail failed: {e}")

    @pytest.mark.parametrize("day_offset", [
        1,  # tomorrow
        2,  # Day after tomorrow
        3,  # 3 days later
    ])
    def test_forecast_detail_for_target_date(self, api_client, day_offset):
        """
        Check day_offset day's forecast detail，
        return the relative humidity(e,g,60-85%) for the given day_offset day
        """
        try:
            forecast_detail = api_client.get_forecast_detail_for_target_date(day_offset)
            assert "forecast_date" in forecast_detail, pytest.fail("Missing forecast_date in response")
            assert "forecast_day_of_week" in forecast_detail, pytest.fail("Missing forecast_day_of_week in response")
            assert 0<=forecast_detail["forecast_day_of_week"]<=6 , pytest.fail("forecast_day_of_week is not in [0,6]")
            assert "wind_info" in forecast_detail, pytest.fail("Missing wind_info in response")
            assert "wx_desc" in forecast_detail, pytest.fail("Missing wx_desc in response")
            assert "max_temp" in forecast_detail, pytest.fail("Missing max_temp in response")
            assert "min_temp" in forecast_detail, pytest.fail("Missing min_temp in response")
            assert "max_rh" in forecast_detail, pytest.fail("Missing max_rh in response")
            assert 0<=forecast_detail["max_rh"]<=100, pytest.fail("max_rh is not a number")
            assert "min_rh" in forecast_detail, pytest.fail("Missing min_rh in response")
            assert 0<=forecast_detail["min_rh"]<=100, pytest.fail("max_rh is not a number")
            assert forecast_detail["min_rh"]<=forecast_detail["max_rh"], pytest.fail("min_rh is greater than max_rh")
            assert "wx_icon" in forecast_detail, pytest.fail("Missing wx_icon in response")
            assert "psr" in forecast_detail, pytest.fail("Missing psr in response")
            assert "psr_id" in forecast_detail, pytest.fail("Missing psr_id in response")

            relative_humidity = f'{forecast_detail["min_rh"]}-{forecast_detail["max_rh"]}%'
            return relative_humidity

        except AssertionError as e:
            pytest.fail(f"Check {day_offset} day's forecast detail failed: {e}")
