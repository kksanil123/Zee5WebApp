import string
import time
import pytest
import random
from selenium.webdriver.common.by import By
from pageObjects.SignUpPage import SignUpPage
from pageObjects.HomePage import HomePage

D = string.ascii_uppercase


@pytest.fixture(scope='module')
def driver_setup(setup):
    sup_obj = SignUpPage(setup)
    yield setup, sup_obj
    print("\n SignUp Page Driver Closing")


@pytest.fixture(scope='module')
def hp_obj(setup):
    h = HomePage(setup)
    return h


@pytest.fixture(scope='class')
def email_gen():
    a = time.gmtime()
    d = a.tm_mday
    m = a.tm_mon
    y = a.tm_year
    r = random.choices(D, k=2)
    return 'a' + f'{d}' + f'{m}' + f'{y}' + f'{r[0]}' + f'{r[1]}' + '@yopmail.com'


@pytest.fixture
def get_otp(setup, request):
    setup.switch_to.new_window('window')
    setup.get("https://yopmail.com/")
    setup.maximize_window()
    email = request.getfixturevalue('email_gen')
    setup.find_element(By.XPATH, '//input[@placeholder="Enter your inbox here"]').send_keys(email)
    setup.find_element(By.XPATH, '//button[@class="md"]').click()
    setup.switch_to.frame('ifmail')
    subj = setup.find_element(By.XPATH, '//div[@class="ellipsis nw b f18"]').text
    setup.switch_to.default_content()
    setup.switch_to.window(setup.window_handles[0])
    return subj[0:4]


@pytest.fixture(scope='function')
def email_signup(driver_setup, hp_obj, request):
    driver, sup_obj = driver_setup
    driver.get('https://www.zee5.com/register')
    # email = request.node.get_closest_marker("email")
    email = request.getfixturevalue('email_gen')
    print(email)
    # otp = request.node.get_closest_marker("otp")
    sup_obj.set_email_field(email)
    sup_obj.select_tAc_box()
    sup_obj.click_create_acc_btn()
    sup_obj.set_age(22)
    sup_obj.set_gender()
    sup_obj.select_tAc_box2()
    sup_obj.click_send_otp_btn()
    otp = request.getfixturevalue('get_otp')
    sup_obj.enter_otp(otp)
    sup_obj.click_verify_otp_btn()
    try:
        if hp_obj.check_profile_menu_btn():
            yield hp_obj, "pass"
            hp_obj.click_logout_btn()
            print('Logged out')
        else:
            yield hp_obj, 'fail'

    except Exception as e:
        print(type(e))
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print(e.args)


class TestSignUpPage:

    # @pytest.mark.email('aniltest@yopmail1.com')
    # @pytest.mark.otp('1111')
    def test_email_reg_success(self, email_signup):
        hp_obj, result = email_signup
        if result == 'pass':
            assert True
        else:
            assert False


