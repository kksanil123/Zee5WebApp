from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_zee5_logo(self):
        return self.driver.find_element(By.XPATH,'//img[@title ="ZEE5 Logo"]').get_attribute('src')

