import pytest
import requests
from common.logger import logger

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