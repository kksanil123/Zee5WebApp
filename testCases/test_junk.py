import pytest
from pageObjects.HomePage import HomePage
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen


@pytest.fixture(scope='module')
def hp_obj(setup):
    site_url = ReadConfig.get_app_url()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    setup.get('https://www.zee5.com')
    hp = HomePage(setup)
    return hp


class TestJunk:
    logger = LogGen.get_logger()

    def test_zee5_logo(self, hp_obj):
        self.logger.info("Test Test Test")
        assert 'ZEE5_logo' in hp_obj.get_zee5_logo()

    def test_home(self, hp_obj):
        assert 'Home' in hp_obj.get_header_list()
