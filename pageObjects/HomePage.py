import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def get_zee5_logo(self):
        return self.driver.find_element(By.XPATH, '//img[@title ="ZEE5 Logo"]').get_attribute('src')

    def get_header_list(self):
        time.sleep(5)
        # header_links1 = self.driver.find_elements(By.XPATH, '(//div[@class="navMenuWrapper "])[1]/ul/descendant::a')
        # header_list = []
        # for link in header_links1:
        #     header_list.append(link.text)

        header_list = []
        header_links2 = self.driver.find_elements(By.XPATH, '(//div[@class="navMenuWrapper "])[2]//li[@class=" "]/descendant::a')
        for link in header_links2:
            header_list.append(link.get_attribute('text'))

        print(header_list)
        return header_list

    def get_more_menu_btn(self):
        script = 'window.getComputedStyle(document.querySelector(".iconInitialLoad-ic_Bento"), "::before");'
        self.driver.execute_script(script)
        # return self.driver.find_element(By.CSS_SELECTOR, '//div[@class="moreMenuBtn iconInitialLoad-ic_Bento"]')

    def get_search_btn(self):
        return self.driver.find_element(By.XPATH, '//div[@class ="searchWrapper  "]')

    def get_language_btn(self):
        script = 'window.getComputedStyle(document.querySelector("#languageBtn"), "::before");'
        self.driver.execute_script(script)
        # return self.driver.find_element(By.XPATH, '//*[@id="languageBtn"]')

    def get_login_btn(self):
        return self.driver.find_element(By.XPATH, '//*[text()="Login"]')

    def get_buyplan_btn(self):
        return self.driver.find_element(By.XPATH, '//a[@class ="subscribeBtn noSelect"]')

    def get_hamburger_menu_btn(self):
        return self.driver.find_element(By.XPATH, '//button[text() ="Open Menu"]')

    def get_banners(self):
        return self.driver.find_elements(By.XPATH, '//div[@class="carouselDots"]')

    def get_banner_scroll(self):
        banners = self.get_banners()
        banner_names = []
        for i in range(0, len(banners)):
            time.sleep(4)
            banner = self.driver.find_element(By.XPATH,
                                              '//*[@class="slick-slide slick-active slick-center slick-current"]//h2[@class="legendTitle  "]')
            banner_names.append(banner.text)

        print(banner_names)
        return banner_names

    def get_banner_click(self):
        banners = self.get_banners()
        banner_names = []
        for banner in banners:
            time.sleep(1)
            banner.click()
            banner_ele = self.driver.find_element(By.XPATH,
                                                  '//*[@class="slick-slide slick-active slick-center slick-current"]//h2[@class="legendTitle  "]')
            banner_names.append(banner_ele.text)

        print(banner_names)
        return banner_names
