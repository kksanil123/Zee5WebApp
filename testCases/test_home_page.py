import time
import pytest

from pageObjects.HomePage import HomePage
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


@pytest.fixture(scope='module')
def hp_obj(setup):
    hp = HomePage(setup)
    yield hp
    setup.close()
    print("\n Home Page Driver Closing")


@pytest.fixture(scope='module')
def headers(hp_obj):
    return hp_obj.get_header_list()


class TestHomePage:

    def test_zee5_logo(self, hp_obj):
        LogGen.get_logger().info('+++++++++++ STARTED Testing HOME PAGE +++++++++++')
        assert 'ZEE5_logo' in hp_obj.get_zee5_logo()

    def test_home(self, headers):
        assert 'Home' in headers

    def test_tvshows(self, headers):
        assert 'TV Shows' in headers

    def test_movies(self, headers):
        assert 'Movies' in headers

    def test_webseries(self, headers):
        assert 'Web Series' in headers

    def test_news(self, headers):
        assert 'News' in headers

    def test_eduauraa(self, headers):
        assert 'Eduauraa' in headers

    def test_premium(self, headers):
        assert 'Premium' in headers

    def test_livetv(self, headers):
        assert 'Live TV' in headers

    def test_music(self, headers):
        assert 'Music' in headers

    def test_kids(self, headers):
        assert 'Kids' in headers

    def test_videos(self, headers):
        assert 'Videos' in headers

    def test_channels(self, headers):
        assert 'Channels' in headers

    def test_more_menu_btn(self, hp_obj):
        hp_obj.get_more_menu_btn()
        assert True

    def test_search_btn(self, hp_obj):
        assert hp_obj.get_search_btn()

    def test_language_btn(self, hp_obj):
        hp_obj.get_language_btn()
        assert True

    def test_login_btn(self, hp_obj):
        assert hp_obj.get_login_btn()

    def test_buyplan_btn(self, hp_obj):
        assert hp_obj.get_buyplan_btn()

    def test_hamburger_menu_btn(self, hp_obj):
        assert hp_obj.get_hamburger_menu_btn()

    def test_banner_scroll(self, hp_obj):
        assert hp_obj.get_banner_scroll()

    def test_banner_click(self, hp_obj):
        assert hp_obj.get_banner_click()
