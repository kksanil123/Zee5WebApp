import pytest
from pageObjects.HomePage import HomePage
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen


# @pytest.fixture(scope='module')
# def hp_obj(setup):
#     setup.get(ReadConfig.get_app_url())
#     setup.maximize_window()
#     setup.implicitly_wait(10)
#     hp = HomePage(setup)
#     yield hp
#     setup.close()
#
#
# class TestJunk:
#
#     def test_zee5_logo(self, hp_obj):
#         LogGen().get_logger().info('STARTED Testing HOME PAGE ********')
#         print("Log recorded")
#         assert 'ZEE5_logo' in hp_obj.get_zee5_logo()
#
#     def test_home(self, hp_obj):
#         assert 'Home' in hp_obj.get_header_list()











@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry, append_first):
    # Assert
    assert order == [first_entry]



