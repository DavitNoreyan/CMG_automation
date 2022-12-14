import itertools

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from action_wrapper.wait_actions import WaitActions


class MoveActions:
    @staticmethod
    @allure.step("Move to {1} element to be visible")
    def move_to_element_located(driver, locator, time_out=30, repeat=3):
        try:
            for _ in itertools.repeat(None, repeat):
                element = WaitActions.wait_until_element_is_visible(driver, locator)
                ActionChains(driver).move_to_element(element)
        except TimeoutException:
            raise TimeoutException(f"The {locator} element is not found after {time_out} seconds of wait")
