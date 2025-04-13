from behave import given,when,then
from pages.agreement_page import AgreementPage
from pages.forecast_page import ForecastPage
from pages.main_page import MainPage

@given('launch the MyObservatory app')
def launch_app(context):
    """Launch the MyObservatory app."""
    context.agreement_page = AgreementPage(context.driver)
    context.main_page = MainPage(context.driver)
    context.forecast_page = ForecastPage(context.driver)


@when('agree to the disclaimer and privacy policy statement')
def agree_statements(context):
    """Agree to the disclaimer and privacy policy statement"""
    context.agreement_page.accept_agreements()
    f"agree to the disclaimer and privacy policy statement"


@when('deny notification and location permission')
def deny_permission(context):
    """deny notification and location permission"""
    context.agreement_page.handle_permissions()
    f"deny notification and location permission"


@when('close the pop-up window on the main page')
def close_popup(context):
    """Close the pop-up window on the home page"""
    try:
        context.main_page.close_popup()
        f"close the pop-up window on the main page"
    except:
        f"no popup"
        pass


@when('navigate to the 9-day forecast screen')
def navigate_to_9day_forecast(context):
    context.forecast_page = context.main_page.navigate_to_9day_forecast()
    f"navigate to the 9-day forecast screen"


@then(u"check the {day_offset}th day\'s weather forecast")
def check_9day_forecast(context, day_offset):
    """Check the 9th day's weather forecast"""
    assert context.forecast_page.get_day_forecast(int(day_offset))