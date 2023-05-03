import time

import selenium.webdriver.common.action_chains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)

    def get_zee5_logo(self):
        return self.driver.find_element(By.XPATH, '//img[@title ="ZEE5 Logo"]').get_attribute('src')

    def get_header_list(self):
        time.sleep(5)
        # header_links1 = self.driver.find_elements(By.XPATH, '(//div[@class="navMenuWrapper "])[1]/ul/descendant::a')
        # header_list = []
        # for link in header_links1:
        #     header_list.append(link.text)

        header_list = []
        header_links2 = self.driver.find_elements(By.XPATH,
                                                  '(//div[@class="navMenuWrapper "])[2]//li[@class=" "]/descendant::a')
        for link in header_links2:
            header_list.append(link.get_attribute('text'))

        print(header_list)
        return header_list

    def get_more_menu_btn(self):
        script = 'window.getComputedStyle(document.querySelector(".iconInitialLoad-ic_Bento"), "::before");'
        self.driver.execute_script(script)
        # return self.driver.find_element(By.XPATH, '//div[@class="moreMenuBtn iconInitialLoad-ic_Bento"]')

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

    def is_displaying(self, element_xpath):
        try:
            self.driver.find_element(By.XPATH, element_xpath).is_displayed()
        except NoSuchElementException:
            return False
        else:
            return True

    # def collection_scroll(self):
    #     while not self.is_displaying("//a[@title ='Watch Best Releases of 2022']"):
    #         self.driver.execute_script('window.scrollBy(0,600)')
    #         time.sleep(2)
    #     else:
    #         self.driver.find_element(By.XPATH,"//div[@class='page-container']/descendant::button[2]").click()
    #         print(self.driver.find_element(By.XPATH,"//div[@class='page-container']/descendant::button[2]").text)
    #         time.sleep(20)
    #
    #     return True

    def page_scroll(self):
        while not self.is_displaying("//a[@title='Watch Explore By Channels']"):
            self.driver.execute_script('window.scrollBy(0,400)')
            time.sleep(2)
        else:
            self.driver.save_screenshot(r'Screenshots\scroll_end.png')

        return True

    def more_btn_hover(self):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.XPATH, '//div[@class="moreMenuBtn iconInitialLoad-ic_Bento"]'))
        act.perform()
        time.sleep(2)
        act.reset_actions()

    def collection_hover(self):
        self.driver.execute_script('window.scrollBy(0,500)')
        mov_list = self.driver.find_elements(By.XPATH, "(//div[@class='movieTrayWrapper'])[1]//img")
        act = ActionChains(self.driver)
        for each in mov_list:
            act.move_to_element(each)
            act.perform()
            time.sleep(2)

        act.reset_actions()

    def change_dis_lang(self, ln_name):
        self.driver.find_element(By.CSS_SELECTOR, 'div#languageBtn').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[text()="Display Language"]').click()
        self.driver.find_element(By.XPATH, '//div[@class="checkboxText"]//span[text()="{ln_name}"]').click()
        return True

    def check_profile_menu_btn(self):
        try:
            self.driver.find_element(By.XPATH, '//div[@data-tooltip="My profile"]')
        except Exception as e:
            return False
        else:
            return True

    def click_logout_btn(self):
        self.driver.find_element(By.XPATH, '//div[@data-tooltip="My profile"]')
        self.driver.find_element(By.XPATH,
                                 '//div[@data-tooltip="My profile"]/parent::div/child::button[text()="Open Menu"]').click()
        return self.driver.find_element(By.XPATH, '//div[text()="Logout"]').click()
