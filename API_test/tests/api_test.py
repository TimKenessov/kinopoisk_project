import allure
import json
import pytest


@pytest.mark.api_positive_tests
@allure.feature("API Tests (Позитивные тесты)")
class TestApiElementsPositive:

    class TestAPI:

        @allure.story("Поиск фильмов и проверка наличия результатов")
        @allure.title(
            "Поиск фильма по названию возвращает корректный результат")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_search_movie(self, search_api):
            with allure.step(
                    "Отправить Get запрос на получение фильма по названию"):
                query = "Интерстеллар"
                response = search_api.search_movie(query)
                allure.attach(
                    name="API request",
                    body=json.dumps({"query": query},
                                    ensure_ascii=False,
                                    indent=4),
                    attachment_type=allure.attachment_type.JSON,
                )
                allure.attach(
                    name="API result",
                    body=response.text,
                    attachment_type=allure.attachment_type.JSON,
                )

            with allure.step("Проверить, что статус-код ответа равен 200"):
                assert search_api.code_status_is(200)
                allure.attach(
                    name="Statuse-code",
                    body=str(response.status_code),
                    attachment_type=allure.attachment_type.TEXT,
                )
                print(response.json())

        @allure.story("Поиск фильмов и проверка наличия результатов")
        @allure.title(
            "Получение списка фильмов по жанру возвращает корректный результат"
        )
        @allure.severity(allure.severity_level.CRITICAL)
        def test_get_movielist_by_genre(self, search_api):
            with allure.step(
                    "Отправить Get запрос на получение списка по жанру"):
                year = "2024"
                genre = "криминал"
                response = search_api.get_movielist_by_genre(year, genre)
                allure.attach(
                    name="API request",
                    body=json.dumps(
                        {
                            "year": year,
                            "genres.name": genre
                        },
                        ensure_ascii=False,
                        indent=4,
                    ),
                    attachment_type=allure.attachment_type.JSON,
                )
                allure.attach(
                    name="API result",
                    body=response.text,
                    attachment_type=allure.attachment_type.JSON,
                )

            with allure.step("Проверить, что статус-код ответа равен 200"):
                assert search_api.code_status_is(200)
                allure.attach(
                    name="Statuse-code",
                    body=str(response.status_code),
                    attachment_type=allure.attachment_type.TEXT,
                )
                print(response.json())

        @allure.story("Поиск фильмов и проверка наличия результатов")
        @allure.title("""Отправка запроса на получения списка по рейтингу
            возвращает корректный результат""")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_get_movielist_by_rating(self, search_api):
            with allure.step(
                    "Отправить Get запрос на получение списка по рейтингу"):
                rating = "rating.kp=10"
                response = search_api.get_movielist_by_rating(rating)
                allure.attach(
                    name="API request",
                    body=json.dumps({"field": rating},
                                    ensure_ascii=False,
                                    indent=4),
                    attachment_type=allure.attachment_type.JSON,
                )
                allure.attach(
                    name="API result",
                    body=response.text,
                    attachment_type=allure.attachment_type.JSON,
                )

            with allure.step("Проверить, что статус-код ответа равен 200"):
                assert search_api.code_status_is(200)
                allure.attach(
                    name="Statuse-code",
                    body=str(response.status_code),
                    attachment_type=allure.attachment_type.TEXT,
                )
                print(response.json())


@pytest.mark.api_negative_tests
@allure.feature("API Tests (Негативные тесты)")
class TestApiElementsNegative:

    class TestAPINegative:

        @allure.story("Поиск фильмов с некорректными данными")
        @allure.title(
            "Поиск фильма со спецсимволами возвращает пустой результат")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_search_movie(self, search_api):
            with allure.step(
                    "Отправить Get запрос состоящий лишь из спецсимволов"):
                query = "NN1,2,3,4,6 | IE3,4,5"
                response = search_api.search_movie(query)
                allure.attach(
                    name="API request",
                    body=json.dumps({"query": query},
                                    ensure_ascii=False,
                                    indent=4),
                    attachment_type=allure.attachment_type.JSON,
                )
                allure.attach(
                    name="API result",
                    body=response.text,
                    attachment_type=allure.attachment_type.JSON,
                )

            with allure.step("Проверить, что статус-код ответа равен 200"):
                assert search_api.code_status_is(200)
                allure.attach(
                    name="Statuse-code",
                    body=str(response.status_code),
                    attachment_type=allure.attachment_type.TEXT,
                )
                print(response.json())

        @allure.story("Поиск фильмов с некорректными данными")
        @allure.title("Запрос с датой будущего года возвращает пустой список")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_get_movielist_by_genre(self, search_api):
            with allure.step("Отправить Get запрос с датой далёкого будущего"):
                year = "2050"
                genre = "криминал"
                response = search_api.get_movielist_by_genre(year, genre)
                allure.attach(
                    name="API request",
                    body=json.dumps(
                        {
                            "year": year,
                            "genres.name": genre
                        },
                        ensure_ascii=False,
                        indent=4,
                    ),
                    attachment_type=allure.attachment_type.JSON,
                )
                allure.attach(
                    name="API result",
                    body=response.text,
                    attachment_type=allure.attachment_type.JSON,
                )

            with allure.step("Проверить, что статус-код ответа равен 200"):
                assert search_api.code_status_is(200)
                allure.attach(
                    name="Statuse-code",
                    body=str(response.status_code),
                    attachment_type=allure.attachment_type.TEXT,
                )
                print(response.json())

        @allure.story("Поиск фильмов с некорректными данными")
        @allure.title("Запрос с отправкой тегов возвращает пустой результат")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_get_movielist_by_rating(self, search_api):
            with allure.step("Отправить Get запрос состоящий из HTML тегов"):
                query = "<tt></tt>"
                response = search_api.search_movie(query)
                allure.attach(
                    name="API request",
                    body=json.dumps({"query": query},
                                    ensure_ascii=False,
                                    indent=4),
                    attachment_type=allure.attachment_type.JSON,
                )
                allure.attach(
                    name="API result",
                    body=response.text,
                    attachment_type=allure.attachment_type.JSON,
                )

            with allure.step("Проверить, что статус-код ответа равен 200"):
                assert search_api.code_status_is(200)
                allure.attach(
                    name="Statuse-code",
                    body=str(response.status_code),
                    attachment_type=allure.attachment_type.TEXT,
                )
                print(response.json())
