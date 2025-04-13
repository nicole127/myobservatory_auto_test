import pytest
import requests
from utils.logger import logger
from datetime import datetime,timedelta

@pytest.fixture
def api_response(url, expected_status_code):
    """send the request, and test the response status code"""
    try:
        response = requests.get(url)
        logger.info(f"Request to {url}, response status code:{response.status_code}")
        assert response.status_code == expected_status_code, f"Request failed, expected_status_code:{expected_status_code}, got {response.status_code}"
        return response
    except requests.RequestException as e:
        logger.error(f"Request to {url} failed: {e}")
        pytest.fail(f"Request to {url} failed: {e}")


@pytest.mark.parametrize("url, expected_status_code",[
    ("https://pda.weather.gov.hk/sc/locspc/data/fnd_uc.xml", 200)
])
def test_9day_forecast_api(url, expected_status_code, api_response):
    """Test the request response status is whether successful or not"""
    pass


@pytest.mark.parametrize("url, expected_status_code, day_offset", [
    ("https://pda.weather.gov.hk/sc/locspc/data/fnd_uc.xml", 200, 2), # 后天
    ("https://pda.weather.gov.hk/sc/locspc/data/fnd_uc.xml", 200, 4) # 4天后
])
def test_humidity_format(url, expected_status_code, day_offset, api_response):
    """Extract the relative humidity(e,g,60-85%) for the day after day_offset days"""
    target_date = (datetime.now()+timedelta(days=day_offset)).strftime("%Y%m%d")
    try:
        data = api_response.json()
        assert "forecast_detail" in data, logger.error("Missing forecast_detail in response")
        relative_humidity = None

        for forecast in data["forecast_detail"]:
            if forecast["forecast_date"] == target_date:
                min_rh = forecast["min_rh"]
                max_rh = forecast["max_rh"]
                if min_rh and 0 <= min_rh <= 100 and max_rh and 0 <= max_rh <= 100:
                    relative_humidity = f"{min_rh}-{max_rh}%"
                    logger.info(
                        f"Successfully extract relative humidity {relative_humidity} for the {target_date}")
                    break
                else:
                    logger.error(f"Invalid humidity values in forecast for {target_date}:min_rh={min_rh},max_rh={max_rh}")
                    pytest.fail(f"Invalid humidity values in forecast for {target_date}:min_rh={min_rh},max_rh={max_rh}")

        assert relative_humidity, logger.error(f"Could not find forecast data for {target_date}")
    except Exception as e:
        logger.error(f"Extract relative humidity for the {target_date} failed:{e}")
        pytest.fail(f"Extract relative humidity for the {target_date} failed:{e}")
