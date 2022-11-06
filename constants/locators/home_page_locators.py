from selenium.webdriver.common.by import By


class HomePageLocator:
    search_bar = (By.CSS_SELECTOR, "input[role=\"combobox\"]")
    submit_button = (By.CSS_SELECTOR, 'form div:nth-of-type(3) input[type="submit"]:nth-of-type(1)')
    header_image = (By.CSS_SELECTOR, 'img[alt="Google"]')
