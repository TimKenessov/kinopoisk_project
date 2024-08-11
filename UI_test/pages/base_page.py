from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver,
                    timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver,
                    timeout).until(EC.element_to_be_clickable(locator))

    def is_movie_page_opened(self):
        current_url = self.driver.current_url
        return "/film/" in current_url

    captcha_locator = (By.ID, "js-button")

    def is_captcha_present(self):
        try:
            return self.driver.find_element(
                *self.captcha_locator).is_displayed()
        except NoSuchElementException:
            return False
