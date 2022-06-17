import urllib.request
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='module')
def setup():
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=opts)
    return driver


@pytest.fixture(autouse=True)
def internet_check():
    try:
        # print("Checking connection anil")
        urllib.request.urlopen('https://www.google.com', timeout=2)
        return True
    except Exception as e:
        raise ConnectionError('Please check internet connection Anil')
