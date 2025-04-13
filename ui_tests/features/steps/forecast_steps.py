from behave import given,when,then
from pages.agreement_page import AgreementPage
from pages.forecast_page import ForecastPage
from pages.main_page import MainPage
from pages.popup_page import PopupPage
from utils.logger import logger


@given('launch the MyObservatory app')
def launch_app(context):
    """Launch the MyObservatory app."""
    try:
        context.agreement_page = AgreementPage(context.driver)
        context.main_page = MainPage(context.driver)
        context.forecast_page = ForecastPage(context.driver)
        context.popup_page = PopupPage(context.driver)
    except Exception as e:
        logger.error(f"Failed to launch the MyObservatory app: {str(e)}")
        raise


@when('agree to the disclaimer and privacy policy statement')
def agree_statements(context):
    """Agree to the disclaimer and privacy policy statement"""
    try:
        context.agreement_page.accept_agreements()
        logger.info("Agree to the disclaimer and privacy policy statement")
    except Exception as e:
        logger.error(f"Failed to agree to the statements: {str(e)}")
        raise


@when('deny notification and location permission')
def deny_permission(context):
    """deny notification and location permission"""
    try:
        context.agreement_page.handle_permissions()
        logger.info("deny notification and location permission")
    except Exception as e:
        logger.error(f"Failed to deny permissions: {str(e)}")
        raise


@when('close the pop-up if exists')
def close_popup(context):
    """Close the pop-up window"""
    try:
        if context.popup_page.popup_exists():
            context.popup_page.close_popup()
            logger.info("close the pop-up on the main page")
        else:
            logger.info("No pop-up window found on the main page")
    except Exception as e:
        logger.error(f"Failed to close the pop-up: {str(e)}")
        raise


@when('navigate to the 9-day forecast screen')
def navigate_to_9day_forecast(context):
    try:
        context.forecast_page = context.main_page.navigate_to_9day_forecast()
        logger.info("navigate to the 9-day forecast screen")
    except Exception as e:
        logger.error(f"Failed to navigate to the 9-day forecast screen: {str(e)}")
        raise


@then(u"check the {day_offset}th day\'s weather forecast")
def check_9day_forecast(context, day_offset):
    """Check the 9th day's weather forecast"""
    try:
        day_forecast = context.forecast_page.get_day_forecast(int(day_offset))
        assert day_forecast
        desc = day_forecast.get_attribute('content-desc')
        assert desc
        logger.info(f"Check the {day_offset}th day's weather forecast successfully, desc:{desc}")
    except AssertionError as e:
        logger.error(f"Failed to get the {day_offset}th day's weather forecast: {str(e)}")
    except Exception as e:
        logger.error(f"An error occurred while checking the {day_offset}th day's weather forecast: {str(e)}")
        raise