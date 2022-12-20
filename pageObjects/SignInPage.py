from selenium.webdriver.common.by import By


class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def set_email_field(self, email):
        return self.driver.find_element(By.NAME, "userName").send_keys(email)

    def set_mobile_field(self):
        return self.driver.find_element(By.NAME, "userName").send_keys("8688167985")

    def set_email_password_field(self, password):
        return self.driver.find_element(By.NAME, "password").send_keys(password)

    def set_otp_fields(self):
        otp_fields = self.driver.find_elements(By.XPATH, '//*[@class="floatingLabelInput otpInputWrap"]/input')
        for field in otp_fields:
            field.send_keys("1")

    def click_verify_btn(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Verify']").click()

    def click_login_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='gradientBtnContainer']//span[text()='Login']").click()

    def check_profile_menu_btn(self):
        try:
            self.driver.find_element(By.XPATH, '//div[@data-tooltip="My profile"]')
        except Exception as e:
            return False
        else:
            return True

    def click_logout_btn(self):
        self.driver.find_element(By.XPATH,
                                 '//div[@data-tooltip="My profile"]/parent::div/child::button[text()="Open Menu"]').click()
        return self.driver.find_element(By.XPATH, '//div[text()="Logout"]').click()
