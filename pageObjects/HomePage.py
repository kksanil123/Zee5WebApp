from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_zee5_logo(self):
        return self.driver.find_element(By.XPATH, '//img[@title ="ZEE5 Logo"]').get_attribute('src')

    def get_header_list(self):
        header_links = self.driver.find_elements(By.XPATH, '(//div[@class="navMenuWrapper "])[2]/ul/li/a')
        header_list = []
        for link in header_links:
            header_list.append(link.text)
        return header_list

    def get_more_menu_btn(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div[1]/div/div/div/div/div')

    def get_search_btn(self):
        return self.driver.find_element(By.XPATH, '//div[@class ="searchWrapper  "]')

    def get_language_btn(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div[1]/div/span/div[2]')

    def get_login_btn(self):
        return self.driver.find_element(By.XPATH, '//*[text()="Login"]')

    def get_buyplan_btn(self):
        return self.driver.find_element(By.XPATH, '//a[@class ="subscribeBtn noSelect"]')

    def get_hamburger_menu_btn(self):
        return self.driver.find_element(By.XPATH, '//button[text() ="Open Menu"]')
