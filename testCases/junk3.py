import time

import pytest
from pageObjects.SignInPage import SignInPage
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def sip_obj(setup):
    setup.get('https://www.zee5.com/signin')
    sp_obj = SignInPage(setup)
    yield setup, sp_obj
    print("\n SignIn Page Driver Closing")
    setup.close()


@pytest.fixture()
def login_email(request, sip_obj):
    driver, sip_obj = sip_obj
    email = request.node.get_closest_marker('email')
    password = request.node.get_closest_marker('password')
    sip_obj.set_email_field(email.args[0])
    sip_obj.set_email_password_field(password.args[0])
    time.sleep(2)
    sip_obj.click_login_btn()
    time.sleep(10)
    if sip_obj.check_profile_menu_btn():
        yield sip_obj, "pass"
    else:
        driver.save_screenshot(r'Screenshots\signin_err2.png')
        yield 'fail'


@pytest.fixture(scope="module")
def logout(setup, login_email):
    sip_obj, result = login_email
    print(setup.title)
    sip_obj.click_logout_btn()
    yield 'pass'


class TestSignInPage:
    # @pytest.mark.parametrize("email, password",[("crmtest@yopmail.com","123456787")])
    @pytest.mark.fixt_data(42)
    @pytest.mark.email('crmtest@yopmail.com')
    @pytest.mark.password(123456787)
    def test_login_email(self, login_email):
        sip_obj, result = login_email
        if result == 'pass':
            assert True
        else:
            assert False
    #
    # def test_logout(self, logout):
    #     if logout == 'pass':
    #         assert True
    #     else:
    #         assert False
