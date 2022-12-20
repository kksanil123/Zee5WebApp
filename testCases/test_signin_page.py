import time

import pytest
from pageObjects.SignInPage import SignInPage
from selenium.webdriver.support.ui import WebDriverWait

pytestmark = [pytest.mark.email("crmtest@yopmail.com"), pytest.mark.password("1234567879")]


@pytest.fixture(scope="module")
def sip_obj(setup):
    sp_obj = SignInPage(setup)
    yield setup, sp_obj
    print("\n SignIn Page Driver Closing")
    setup.close()


@pytest.fixture(scope="function")
def login_email(sip_obj, request):
    driver, sip_obj = sip_obj
    driver.get('https://www.zee5.com/signin')
    email = request.node.get_closest_marker("email")
    password = request.node.get_closest_marker("password")
    print(password)
    sip_obj.set_email_field(email.args[0])
    sip_obj.set_email_password_field(password.args[0])
    time.sleep(2)
    sip_obj.click_login_btn()
    time.sleep(1)
    driver.save_screenshot(r'Screenshots\signin_err2.png')
    time.sleep(10)
    try:
        if sip_obj.check_profile_menu_btn():
            yield sip_obj, "pass"
            sip_obj.click_logout_btn()
            print('Logged out')
        else:
            yield sip_obj, 'fail'

    except Exception as e:
        print(type(e))
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print(e.args)


@pytest.fixture(scope="function")
def logout(setup, login_email):
    sip_obj, result = login_email
    if result == 'pass':
        sip_obj.click_logout_btn()
        return 'pass'
    else:
        return 'fail'


# @pytest.mark.email("crmtest@yopmail.com")
# @pytest.mark.password("123456787")
class TestSignInPage:
    # @pytest.mark.parametrize("email, password",[("crmtest@yopmail.com","123456787")])
    @pytest.mark.email("crmtest@yopmail.com")
    @pytest.mark.password("12345678")
    def test_login_email_failure(self, login_email):
        sip_obj, result = login_email
        if result == 'fail':
            pytest.xfail("Invalid credentials")
        else:
            assert False

    @pytest.mark.email("crmtest@yopmail.com")
    @pytest.mark.password("123456787")
    def test_login_email_success(self, login_email):
        sip_obj, result = login_email
        if result == 'pass':
            assert True
        else:
            assert False

    @pytest.mark.email("crmtest991@yopmail.com")
    @pytest.mark.password("1234567")
    def test_login_unreg_email(self, login_email):
        sip_obj, result = login_email
        if result == 'fail':
            pytest.xfail("Unregistered email")
        else:
            assert False

    @pytest.mark.email("crmtest@yopmail.com")
    @pytest.mark.password("123456787")
    def test_logout(self, logout):
        if logout == 'pass':
            assert True
        else:
            assert False
