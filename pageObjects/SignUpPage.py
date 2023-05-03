from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignUpPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def set_email_field(self, email):
        self.driver.find_element(By.XPATH, '//input[@name="userName"]').send_keys(email)

    def select_tAc_box(self):
        self.driver.find_element(By.XPATH, '//span[@class="markCheckbox"]').click()

    def click_create_acc_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Create account"]').click()

    def set_age(self, age):
        self.driver.find_element(By.XPATH, '//input[@name="age"]').send_keys(age)

    def set_gender(self):
        self.driver.find_element(By.XPATH, '//span[text()="Select Gender"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Male"]').click()

    def select_tAc_box2(self):
        self.driver.find_element(By.XPATH, '//input[@name="policy"]').click()

    def click_send_otp_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Send OTP"]').click()

    def enter_otp(self, otp):
        for i in range(len(otp)):
            code = i + 1
            path='//input[@name="otp'+f'{code}'+'"]'
            self.driver.find_element(By.XPATH, path).send_keys(otp[i])

    def click_verify_otp_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Verify OTP"]').click()
