import time

import allure
from selenium.common.exceptions import ElementNotInteractableException, \
    ElementClickInterceptedException

from action_wrapper.element_finder import ElementFinder


class ElementActions:

    @staticmethod
    @allure.step("Click to {1} element")
    def click_on_element(driver, locator, repeat=3, timeout=20):
        is_stale = True
        repeat_count = 0
        while is_stale and repeat_count < repeat:
            try:
                repeat_count += 1
                ElementFinder.find_element(driver, locator, timeout=timeout).click()
                is_stale = False
            except (ElementNotInteractableException,
                    ElementClickInterceptedException) as e:
                # firefox solution
                time.sleep(0.3)

    @staticmethod
    @allure.step("Get value of {1} element text")
    def get_text(driver, locator, timeout=20):
        return ElementFinder.find_element(driver, locator, timeout=timeout).text

    @staticmethod
    @allure.step("Type text on {1} element")
    def put_text(driver, locator, text, timeout=20):
        return ElementFinder.find_element(driver, locator, timeout=timeout).send_keys(text)

    @staticmethod
    @allure.step("Type value of attribute of {1} element")
    def get_attribute(driver, locator, attribute, timeout=20):
        return ElementFinder.find_element(driver, locator, timeout=timeout).get_attribute(attribute)