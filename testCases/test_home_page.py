from selenium import webdriver
from selenium.webdriver.common.service import Service
from pageObjects.HomePage import HomePage
import pytest


class HomePageTest:
    serv_obj = Service(r'/home/kishore/Downloads/chromedriver')

    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=serv_obj, options=opts)

    driver.get('https://www.zee5.com')
    print(driver.title)
    # hp = HomePage(driver)
    #
    # def test_zee5_logo(self,hp):
    #     assert hp.get_zee5_logo() == 'https://www.zee5.com/images/ZEE5_logo.svg?ver=2.51.63'

    driver.close()




