import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.home_page_locators import HomePageLocator
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '/'

    def is_loaded(self):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, HomePageLocator.search_bar)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    @allure.step("Get Search bar for Home Page")
    def get_search_bar(self):
        return ElementFinder.find_element(self.driver, HomePageLocator.search_bar)

    @allure.step("Get submit bar for Home Page")
    def get_submit(self):
        return ElementFinder.find_element(self.driver, HomePageLocator.submit_button)

    @allure.step("Get submit bar for Home Page")
    def click_submit_button(self):
        ElementActions.click_on_element(self.driver, HomePageLocator.header_image)
        ElementActions.click_on_element(self.driver, HomePageLocator.submit_button)
        WaitActions.wait_until_element_is_invisible(self.driver, HomePageLocator.submit_button)
        WaitActions.wait_until_element_is_visible(self.driver, HomePageLocator.search_bar)
