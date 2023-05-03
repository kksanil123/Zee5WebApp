import pytest

from pageObjects.HomePage import HomePage
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen


@pytest.fixture(scope='module')
def hp_obj(setup):
    setup.get(ReadConfig.get_app_url())
    setup.maximize_window()
    setup.implicitly_wait(10)
    hp = HomePage(setup)
    yield hp
    setup.close()
    print("window not closed...")


class TestJunk:

    def test_zee5_logo(self, hp_obj):
        LogGen().get_logger().info('STARTED Testing HOME PAGE ********')
        assert 'ZEE5_logo' in hp_obj.get_zee5_logo()




