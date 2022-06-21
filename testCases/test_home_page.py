import time
import os
from selenium import webdriver
from selenium.webdriver.common.service import Service
from pageObjects.HomePage import HomePage
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
import pytest

@pytest.fixture(scope='module')
def hp_obj(setup):
    setup.get(ReadConfig.get_app_url())
    hp = HomePage(setup)
    setup.maximize_window()
    yield hp
    setup.close()


class TestHomePage:
    logger = LogGen.get_logger()

    def test_zee5_logo(self, hp_obj):
        self.logger.info('STARTED Testing HOME PAGE')
        assert 'ZEE5_logo' in hp_obj.get_zee5_logo()

    # def test_home(self, hp_obj):
    #     assert 'Home' in hp_obj.get_header_list()
    #
    # def test_tvshows(self, hp_obj):
    #     assert 'TV Shows' in hp_obj.get_header_list()
    #
    # def test_movies(self, hp_obj):
    #     assert 'Movies' in hp_obj.get_header_list()
    #
    # def test_webseries(self, hp_obj):
    #     assert 'Web Series' in hp_obj.get_header_list()
    #
    # def test_news(self, hp_obj):
    #     assert 'News' in hp_obj.get_header_list()
    #
    # def test_eduauraa(self, hp_obj):
    #     assert 'Eduauraa' in hp_obj.get_header_list()
    #
    # def test_premium(self, hp_obj):
    #     assert 'Premium' in hp_obj.get_header_list()
    #
    # def test_livetv(self, hp_obj):
    #     assert 'Live TV' in hp_obj.get_header_list()
    #
    # def test_music(self, hp_obj):
    #     assert 'Music' in hp_obj.get_header_list()
    #
    # def test_zeeplex(self, hp_obj):
    #     assert 'ZEEPLEX' in hp_obj.get_header_list()
    #
    # def test_play(self, hp_obj):
    #     assert 'Play' in hp_obj.get_header_list()
    #
    # def test_articles(self, hp_obj):
    #     assert 'Articles' in hp_obj.get_header_list()
    #
    # def test_kids(self, hp_obj):
    #     assert 'Kids' in hp_obj.get_header_list()
    #
    # def test_videos(self, hp_obj):
    #     assert 'Videos' in hp_obj.get_header_list()
    #
    # def test_stories(self, hp_obj):
    #     assert 'Stories' in hp_obj.get_header_list()
    #
    # def test_channels(self, hp_obj):
    #     assert 'Channels' in hp_obj.get_header_list()

    # def test_more_menu_btn(self, hp_obj):
    #     hp_obj.get_more_menu_btn()
    #     assert True

    def test_search_btn(self, hp_obj):
        assert hp_obj.get_search_btn()

    # def test_language_btn(self, hp_obj):
    #     hp_obj.get_language_btn()
    #     assert True

    # def test_login_btn(self, hp_obj):
    #     assert hp_obj.get_login_btn()
    #
    # def test_buyplan_btn(self, hp_obj):
    #     assert hp_obj.get_buyplan_btn()
    #
    # def test_hamburger_menu_btn(self, hp_obj):
    #     assert hp_obj.get_hamburger_menu_btn()


