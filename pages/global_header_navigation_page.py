import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.global_header_navigation_page_locators import GlobalHeaderNavigationLocator
from pages.base_page import BasePage


class GlobalHeaderNavigation(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '/'

    def is_loaded(self):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, GlobalHeaderNavigationLocator.log_in_button)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    @allure.step("Get Log In button on Main Page")
    def get_login_button(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.log_in_button)

    @allure.step("Click on Log In button on Main Page")
    def click_login_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocator.log_in_button)

    @allure.step("Get username bar on Log In Page")
    def get_username_bar(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.username)

    @allure.step("Enter username on Log In Page")
    def enter_username(self):
        ElementActions.put_text(self.driver, GlobalHeaderNavigationLocator.username, "aaaaa")

    @allure.step("Get password bar on Log In Page")
    def get_password_bar(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.password)

    @allure.step("Enter password bar for Log In Page")
    def enter_password(self):
        ElementActions.put_text(self.driver, GlobalHeaderNavigationLocator.password, "aaaaa")

    @allure.step("Get submit button for Log In Page")
    def get_submit_button(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.submit_button)

    @allure.step("Click on submit button for Log In Page")
    def click_on_submit_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocator.submit_button)

    @allure.step("Get sign up button for Main Page")
    def get_sign_up_button(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.sign_up_button)

    @allure.step("Click on Sign up button for Main Page")
    def click_on_sign_up_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocator.sign_up_button)

    @allure.step("Get confirm password for Sign Up Page")
    def get_confirm_password_button(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.confirm_password)

    @allure.step("Get avatar wrapper for Sign Up Page")
    def get_sign_up_avatar_wrapper(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.sign_up_avatar_wrapper)

    @allure.step("Get theme selector on Sign Up Page")
    def get_sign_up_theme_selector(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.sign_up_theme_selector)

    @allure.step("Get generate nickname button for Sign Up Page")
    def get_generate_nickname(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.generate_nickname)

    @allure.step("Get default nickname button for Sign Up Page")
    def get_default_nickname(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.default_nickname)

    @allure.step("Get create nickname button for Sign Up Page")
    def get_create_nickname(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.create_nickname)

    @allure.step("Get User Avatar on Logged In Page")
    def get_user_avatar(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.user_avatar)

    @allure.step("Get User Name button on Logged In Page")
    def get_user_name(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.user_name)

    @allure.step("Get Game Level on Logged In Page")
    def get_level_game(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.level_game)

    @allure.step("Click on Log Out button on Logged In Page")
    def click_on_log_out_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocator.log_out_button)

    @allure.step("Get Log Out button on Logged In Page")
    def get_log_out_button(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.log_out_button)

    @allure.step("Click on User Page button on Logged In Page")
    def click_on_user_page_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocator.user_page_button)

    @allure.step("Get User Profile page")
    def get_user_profile_page(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.user_profile_page)

    @allure.step("Get Sign Up button for Sign Up Page")
    def get_signup_btn(self):
        return ElementFinder.find_element(self.driver, GlobalHeaderNavigationLocator.sign_up)

    @allure.step("Click on close button on UPGRADE... page")
    def click_on_close_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocator.close_button)
