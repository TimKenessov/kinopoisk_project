from UI_test.pages.elements_page import SearchField
from UI_test.pages.elements_page import MovieResultPage
from UI_test.pages.elements_page import ExpandedSearch
import allure
import pytest


@pytest.mark.ui_positive_tests
@allure.feature("UI Tests (Позитивные тесты)")
class TestElementsPositive:

    class TestSearchField:

        @allure.story("Поиск фильмов и проверка наличия результатов")
        @allure.title(
            "Поиск фильма по названию возвращает корректный результат")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_search_movie(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                call = SearchField(driver, "https://www.kinopoisk.ru/")
                call.open()

            # Отладка на случай возникновения CAPTCHA
            call.captcha_check()

            with allure.step("Шаг 2. Выполнить поиск фильма по названию"):
                movie_tittle = "Интерстеллар"
                call.search_movie(movie_tittle)

            if call.if_movie_page_opened(movie_tittle):
                assert True
            else:
                with allure.step(
                        "Шаг 3. Проверить наличие результатов поиска"):
                    results = call.get_search_results()
                    results_text = "\n".join(
                        [result.text for result in results])
                    allure.attach(
                        results_text,
                        name="Search Results",
                        attachment_type=allure.attachment_type.JSON,
                    )
                    assert len(results) > 0

    class TestMoviePage:

        @allure.story(
            "Открытие страницы с информацией о фильме из результата поиска")
        @allure.title("Страница с фильмом открывавется из результатов поиска")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_open_movie_page(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                call = SearchField(driver, "https://www.kinopoisk.ru/")
                open = MovieResultPage(driver, "https://www.kinopoisk.ru/")
                call.open()

            # Отладка на случай возникновения CAPTCHA
            call.captcha_check()

            with allure.step("Шаг 2. Выполнить поиск фильма по названию"):
                movie_title = "Головой о стену"
                call.search_movie(movie_title)

            with allure.step("Шаг 3. Открыть страницу с фильмом"):
                open.movie_page(movie_title)

        @allure.story("Открытие информации из карточки фильма")
        @allure.title("Страницы с информацией открываются из карточки фильма")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_open_actors_page(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                call = SearchField(driver, "https://www.kinopoisk.ru/")
                open = MovieResultPage(driver, "https://www.kinopoisk.ru/")
                call.open()

            # Отладка на случай возникновения CAPTCHA
            call.captcha_check()

            with allure.step("Шаг 2. Выполнить поиска фильма по названию"):
                movie_tittle = "Новый Человек-паук"
                call.search_movie(movie_tittle)

            with allure.step(
                    "Шаг 3. Открыть страницу с актёрами из карточки фильма"):
                open.card_info()

            with allure.step("Шаг 4. Проверить заголовок страницы"):
                assert "Новый Человек-паук" in driver.title
                allure.attach(
                    driver.title,
                    name="Page Title",
                    attachment_type=allure.attachment_type.JSON,
                )

    class TestExpandedSearch:

        @allure.story("Поиск фильмов в расширенном поиске")
        @allure.title("Поиск фильмов в расширенном поиске осуществляется")
        @allure.severity(allure.severity_level.NORMAL)
        def test_expanded_search(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                expanded = ExpandedSearch(driver, "https://www.kinopoisk.ru/")
                expanded.open()

            with allure.step("Шаг 2. Перейти в расширенный поиск"):
                expanded.open_ex_search()

            with allure.step("Шаг 3. Ввести название фильма в строку поиск"):
                movie_title = "Мальчик в полосатой пижаме"
                expanded.enter_title(movie_title)

            with allure.step("Шаг 4. Выбрать год"):
                year_title = "2008"
                expanded.enter_year(year_title)

            with allure.step("Шаг 5. Выбрать страну"):
                country = "США"
                expanded.enter_country(country)

            with allure.step("Шаг 6. Ввести жанр"):
                genre = "драма"
                expanded.enter_genre(genre)

            with allure.step("Шаг 7. Ввести имя актёра"):
                actor_name = "Эйса Баттерфилд"
                expanded.enter_actor(actor_name)

            with allure.step('Шаг 8. Нажать кнопку "Поиск"'):
                expanded.find_movie_button()

            with allure.step("Шаг 9. Проверить заголовок страницы"):
                assert "Мальчик в полосатой пижаме" in driver.title
                allure.attach(
                    driver.title,
                    name="Page Title",
                    attachment_type=allure.attachment_type.JSON,
                )

            with allure.step(
                    "Шаг 10. Проверить URL страницы результатов поиска"):
                current_url = driver.current_url
                assert "film" in current_url
                allure.attach(
                    current_url,
                    name="Current URL",
                    attachment_type=allure.attachment_type.TEXT,
                )


@pytest.mark.ui_negative_tests
@allure.feature("UI Tests (Негативные тесты)")
class TestElementsNegative:

    class TestSearchFieldNegative:

        @allure.story("Поиск фильмов с некорректными данными")
        @allure.title("""
            При вводе запроса содержащий лишь пробелы возвращается
            пустой список
            """)
        @allure.severity(allure.severity_level.CRITICAL)
        def test_search_movie(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                call = SearchField(driver, "https://www.kinopoisk.ru/")
                call.open()

            # Отладка на случай возникновения CAPTCHA
            call.captcha_check()

            with allure.step(
                    "Шаг 2. Ввести запрос, содержащий только пробелы"):
                movie_tittle = "      "
                call.search_movie(movie_tittle)

            if call.if_movie_page_opened(movie_tittle):
                assert True
            else:
                with allure.step("Шаг 3. Проверить наличие текста об ошибке"):
                    results = call.no_results_message_is_present()
                    assert (
                        "К сожалению, по вашему запросу ничего не найдено..."
                        in results)
                    allure.attach(
                        results,
                        name="No results message",
                        attachment_type=allure.attachment_type.TEXT,
                    )

    class TestMoviePageNegative:

        @allure.story("Поиск фильмов с некорректными данными")
        @allure.title(
            "При вводе в поле поиска спецсимволов возвращается пустой список")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_open_movie_page(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                call = SearchField(driver, "https://www.kinopoisk.ru/")
                call.open()

            # Отладка на случай возникновения CAPTCHA
            call.captcha_check()

            with allure.step(
                    """
                    Шаг 2. Ввести запрос, содержащий только специальные символы
                    """
            ):
                movie_title = "&gt; NN1,2,3,4,6 | IE3,4,5"
                call.search_movie(movie_title)

            with allure.step("Шаг 3. Проверить наличие текста об ошибке"):
                results = call.no_results_message_is_present()
                assert (
                    "К сожалению, по вашему запросу ничего не найдено..."
                    in results)
                allure.attach(
                    results,
                    name="No results message",
                    attachment_type=allure.attachment_type.TEXT,
                )

        @allure.story("Поиск фильмов с некорректными данными")
        @allure.title(
            "При вводе в поле поиска HTML-теги возвращается пустой список")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_open_actors_page(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                call = SearchField(driver, "https://www.kinopoisk.ru/")
                call.open()

            # Отладка на случай возникновения CAPTCHA
            call.captcha_check()

            with allure.step(
                    """
                    Шаг 2. Ввести запрос, содержащий небезопасные
                    символы или HTML-теги
                    """
            ):
                movie_tittle = "<tt></tt>"
                call.search_movie(movie_tittle)

            with allure.step("Шаг 3. Проверить наличие текста об ошибке"):
                results = call.no_results_message_is_present()
                assert (
                    "К сожалению, по вашему запросу ничего не найдено..."
                    in results)
                allure.attach(
                    results,
                    name="No results message",
                    attachment_type=allure.attachment_type.TEXT,
                )

    class TestExpandedSearchNegative:

        @allure.story(
            "Поиск фильмов в расширенном поиске с некорректными данными")
        @allure.title(
            "Ввод некорректных данных в поле поиска возвращает пустой список")
        @allure.severity(allure.severity_level.NORMAL)
        def test_expanded_search(self, driver):
            with allure.step("Шаг 1. Открыть главную страницу"):
                expanded = ExpandedSearch(driver, "https://www.kinopoisk.ru/")
                call = SearchField(driver, "https://www.kinopoisk.ru/")
                expanded.open()

            with allure.step("Шаг 2. Перейти в расширенный поиск"):
                expanded.open_ex_search()

            with allure.step("Шаг 3. Ввести в строку поиск спецсимволы"):
                movie_title = "| IE3,4,5"
                expanded.enter_title(movie_title)

            with allure.step("Шаг 4. Ввести год буквами"):
                year_title = "две тысяча восьмой"
                expanded.enter_year(year_title)

            with allure.step("Шаг 5. Выбрать страну"):
                country = "США"
                expanded.enter_country(country)

            with allure.step("Шаг 6. Выбрать жанр"):
                genre = "драма"
                expanded.enter_genre(genre)

            with allure.step(
                    '''
                    Шаг 7. Ввести в поле "актер" запрос содержащий
                    только пробелы
                    '''
            ):
                actor_name = "    "
                expanded.enter_actor(actor_name)

            with allure.step('Шаг 8. Нажать кнопку "Поиск"'):
                expanded.find_movie_button()

            with allure.step("Шаг 9. Проверить наличие текста об ошибке"):
                results = call.no_results_message_is_present()
                assert (
                    "К сожалению, по вашему запросу ничего не найдено..."
                    in results)
                allure.attach(
                    results,
                    name="No results message",
                    attachment_type=allure.attachment_type.TEXT,
                )
