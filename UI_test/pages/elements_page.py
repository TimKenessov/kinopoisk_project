from UI_test.pages.base_page import BasePage
from UI_test.locators.elements_page_locators import SearchFieldLocators
from UI_test.locators.elements_page_locators import MovieResultPageLocators
from UI_test.locators.elements_page_locators import ExpandedSearchLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import allure


class SearchField(BasePage):
    search_loc = SearchFieldLocators()

    @allure.step("Поиск фильма по названию")
    def search_movie(self, title):
        self.element_is_visible(self.search_loc.search_field).send_keys(title)
        self.element_is_visible(self.search_loc.search_button).click()

    @allure.step("Получение результата поиска")
    def get_search_results(self):
        result = self.elements_are_visible(self.search_loc.search_results)
        return result

    # Сообщение об отрицательном результате поиска
    def no_results_message_is_present(self):
        return self.element_is_visible(
            self.search_loc.search_results_message).text

    # Обработка на случай возниконовения CAPTCHA
    def captcha_check(self):
        self.is_captcha_present()

    # Обработка на случай если фильм имеет уникальное название и открыввается
    # сразу при нажатии на кнопку поиск
    def if_movie_page_opened(self, movie_title):
        try:
            return movie_title in self.driver.title
        except NoSuchElementException:
            return False


class MovieResultPage(BasePage):
    movie_loc = MovieResultPageLocators()

    # Открытие фильма из результатов поиска
    def movie_page(self, title):
        # Обработка на случай если фильм имеет уникальное название и
        # открыввается сразу при нажатии на кнопку поиск
        if self.is_movie_page_opened():
            print("Страница фильма уже открыта. Последующие действия отменены")
            return
        wait = WebDriverWait(self.driver, 10)
        try:
            first_result = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, title)))
            wait.until(EC.element_to_be_clickable(first_result))
            first_result.click()
        except Exception:
            raise

    # Для тестирования других элементов карточки поменяйте id в
    # elements_page_locators.py/movie_card
    @allure.step("Открыть страницу из карточки фильма")
    def card_info(self):
        self.element_is_clickable(self.movie_loc.movie_card).click()


class ExpandedSearch(BasePage):
    ex_locator = ExpandedSearchLocators

    #  Открытие страницы с расширенным поиском
    def open_ex_search(self):
        self.element_is_clickable(self.ex_locator.ex_search_button).click()

    # Ввод Названия фильма
    def enter_title(self, title):
        self.element_is_visible(
            self.ex_locator.ex_search_movie_field).send_keys(title)

    # Ввод даты релиза
    def enter_year(self, year_title):
        self.element_is_visible(
            self.ex_locator.ex_search_movie_year).send_keys(year_title)

    # Ввод Страны
    def enter_country(self, country):
        select_element = self.element_is_visible(
            self.ex_locator.ex_search_movie_country)
        select = Select(select_element)
        select.select_by_visible_text(country)

    #  Ввод жанра
    def enter_genre(self, genre):
        select_element = self.element_is_visible(
            self.ex_locator.ex_search_movie_genre)
        select = Select(select_element)
        select.select_by_visible_text(genre)

    #  Ввод Имени Актёра
    def enter_actor(self, actor):
        self.element_is_visible(
            self.ex_locator.ex_search_movie_actor).send_keys(actor)

    # Кнопка поиск
    def find_movie_button(self):
        self.element_is_clickable(
            self.ex_locator.ex_search_movie_button).click()
