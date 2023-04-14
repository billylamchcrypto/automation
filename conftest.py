import pytest
from settings import *
from appium import webdriver


@pytest.fixture
def setup():
    capabilities = {
        'platformName': (CONFIG[platform]['platformName']),
        'platformVersion': (CONFIG[platform]['platformVersion']),
        'deviceName': (CONFIG[platform]['deviceName']),
        'automationName': (CONFIG[platform]['automationName']),
        'appPackage': (CONFIG[platform]['appPackage']),
        'app': (CONFIG[platform]['app']),
        'noReset': (CONFIG[platform]['noReset']),
        'fullReset': (CONFIG[platform]['fullReset'])

    }
    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    return driver

    # def teardown():
    #     cls.instance.driver.quit()
    # cls.addfinalizer(teardown)
