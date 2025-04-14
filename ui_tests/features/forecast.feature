Feature: MyObservatory App UI 9-Day Forecast Test
  Scenario Outline: Launch the app and check the forecasts for different dates
    Given launch the MyObservatory app
    When agree to the disclaimer and privacy policy statement
    And deny notification and location permission
    And close the pop-up if exists
    And navigate to the 9-day forecast screen
    Then Check the <day>th day's weather
    Examples:
      | day |
      | 2   |
      | 5   |
      | 8   |