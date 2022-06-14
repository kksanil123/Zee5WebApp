from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
import urllib.request
import pytest


@pytest.fixture(scope='module')
def setup():
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=opts)
    return driver


@pytest.fixture(scope='module')
def internet_check():
    try:
        urllib.request.urlopen('https://www.google.com', timeout=2)
        return True
    except Exception as e:
        raise ConnectionError('Please check internet connection Anil')
