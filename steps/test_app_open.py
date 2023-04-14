import pytest
from page.common_page import Passcode
from page.home_page import Home
from pytest_bdd import given, when, then


@given('Users are in the passcode page')
@pytest.mark.usefixtures('setup')
def test_passcode_here(setup):
    start = Passcode(setup)
    start.passcode_here()


@when('Users enter correct passcode')
@pytest.mark.usefixtures('setup')
def test_open_app(setup):
    start = Passcode(setup)
    start.passcode_enter()


@then('Users access the home page')
@pytest.mark.usefixtures('setup')
def test_home_here(setup):
    start = Home(setup)
    start.home_here()
