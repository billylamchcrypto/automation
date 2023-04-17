import pytest
from page.common_page import Passcode
from page.home_page import Home
from pytest_bdd import scenario, given, when, then


@given('Users are in the passcode page')
def passcode_here(driver):
    start = Passcode(driver)
    # start.passcode_here()
    print("app opened")


@when('Users enter correct passcode')
def open_app(driver):
    # start = Passcode(setup)
    # start.passcode_enter()
    print("app opened")


@then('Users access the home page')
def home_here(driver):
    # start = Home(setup)
    # start.home_here()
    print("ended")
