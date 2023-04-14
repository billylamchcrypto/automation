# Created by billylam at 14/4/2023
Feature: App Open

  Scenario: Open the Main App and enter passcode
    Given Users are in the passcode page
    When Users enter correct passcode
    Then Users access the home page