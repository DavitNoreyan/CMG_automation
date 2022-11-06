import os

import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.home_page import HomePage


@allure.feature("Home")
@allure.story("Home")
@pytest.mark.usefixtures("get_driver")
class TestHomePage:

    def setup(self):
        self.home_page: HomePage = HomePage(self.driver)
        self.home_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify home page structure')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home
    @pytest.mark.web
    @pytest.mark.mobile
    def test_home_page_structure(self):
        assert self.home_page.get_search_bar().is_displayed()
        self.home_page.get_search_bar().send_keys("google")
        self.home_page.click_submit_button()
        # assert
