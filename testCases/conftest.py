import urllib.request
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.readproperties import ReadConfig


@pytest.fixture(scope='module')
def setup():
    opts = Options()
    # opts.add_argument('--headless')
    # opts.add_argument('--no-sandbox')
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    opts.add_experimental_option('prefs', prefs)
    opts.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=opts)
    driver.get(ReadConfig.get_app_url())
    driver.maximize_window()
    print("Driver initialized")
    return driver


@pytest.fixture(autouse=True)
def internet_check():
    try:
        urllib.request.urlopen('https://www.google.com', timeout=2)
        return True
    except Exception as e:
        raise ConnectionError('Please check internet connection Anil')


