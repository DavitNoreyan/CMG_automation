import os

import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.global_header_navigation_page import GlobalHeaderNavigation


@allure.feature("global_header_navigation")
@allure.story("global_header_navigation")
@pytest.mark.usefixtures("get_driver")
class TestGlobalHeaderNavigationPage:

    def setup(self):
        self.main_page: GlobalHeaderNavigation = GlobalHeaderNavigation(self.driver)
        self.main_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('GH-1: Verify the Login button functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.global_header_navigation
    @pytest.mark.web
    @pytest.mark.mobile
    def test_login_button(self):
        assert self.main_page.get_login_button().is_displayed()
        self.main_page.click_login_button()
        assert self.main_page.get_username_bar().is_displayed()
        assert self.main_page.get_password_bar().is_displayed()
        assert self.main_page.get_submit_button().is_displayed()

    @allure.testcase('2')
    @allure.title('GH-2: Verify the Sign up button functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.global_header_navigation
    @pytest.mark.web
    @pytest.mark.mobile
    def test_sign_up_page_structure(self):
        self.main_page.click_on_sign_up_button()
        assert self.main_page.get_username_bar().is_displayed()
        assert self.main_page.get_password_bar().is_displayed()
        assert self.main_page.get_confirm_password_button().is_displayed()
        assert self.main_page.get_sign_up_avatar_wrapper().is_displayed()
        assert self.main_page.get_sign_up_theme_selector().is_displayed()
        assert self.main_page.get_default_nickname().is_displayed()
        assert self.main_page.get_generate_nickname().is_displayed() and \
               self.main_page.get_generate_nickname().is_enabled()
        assert self.main_page.get_create_nickname().is_displayed()
        assert self.main_page.get_signup_btn().is_displayed() and \
               self.main_page.get_signup_btn().is_enabled()

    @allure.testcase('3')
    @allure.title('GH-3: Verify the global header for Logged In users')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.global_header_navigation
    @pytest.mark.web
    @pytest.mark.mobile
    def test_logged_in_page(self):
        self.main_page.click_login_button()
        self.main_page.enter_username()
        self.main_page.enter_password()
        self.main_page.click_on_submit_button()
        assert self.main_page.get_user_avatar().is_displayed()
        assert self.main_page.get_user_name().is_displayed()
        assert self.main_page.get_level_game().is_displayed()
        assert self.main_page.get_log_out_button().is_displayed() and \
               self.main_page.get_log_out_button().is_enabled()
       # 'GH-4: Verify clicking on Username takes to User Profile page'
        self.main_page.click_on_user_page_button()
        self.main_page.click_on_close_button()
        assert self.main_page.get_user_profile_page().is_displayed()
        # 'GH-5: Verify the Sign up button functionality'
        self.main_page.click_on_log_out_button()