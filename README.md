# Проект тестирования API и UI для Kinopoisk

# Описание задачи

Проект представляет собой набор автоматизированных тестов для API и UI сайта [Kinopoisk](https://www.kinopoisk.ru/). Основная цель тестов — проверка корректности работы функционала сайта и его API. В проекте реализованы как позитивные, так и негативные тесты для различных API эндпоинтов и пользовательского интерфейса.


## Цель проекта

Основная цель проекта — обеспечить качество и стабильность работы Kinopoisk, автоматизировав процесс тестирования. Это помогает выявлять и устранять потенциальные ошибки на ранних стадиях разработки, что повышает надежность и удобство использования сервиса.

## Основные функции

- Автоматизация тестирования API эндпоинтов для поиска фильмов, получения информации о фильмах, фильтрации по жанру и рейтингу.
- Автоматизация тестирования пользовательского интерфейса для проверки корректности отображения элементов и функциональности основных страниц.
- Генерация подробных отчетов о результатах тестов с использованием Allure.


# Структура проекта

- `API_test / `
   - `pages / `
       - `base_page_api.py` - Базовый класс для работы с API.
        - `elements_page_api.py` - Класс для работы с API поиска фильмов и их получения.
    - `tests /`
       - `api_test.py` - Файлы тестов API.
- `UI_test /`
   - `pages/`
       - `base_page.py` - Базовый класс для работы с UI.
        - `elements_page_api.py` - Класс для работы с поиском фильмов.
    - `locators /`
       - `elements_page_locators.py` - Локаторы элелементов для работы с поиском
    - `tests /`
       - `ui_test.py` - Файлы тестов UI.
- `README.md` - Документация проекта.
- `requirements.txt` - Список зависимостей проекта.


# Запуск тестов

Для запуска тестов, выполните следующие шаги:

1. Установите зависимости:

    ```bash
    pip install - r requirements.txt

2. Запустите тесты:

    Для API тестов (позитивные):

        pytest -m api_positive_tests --alluredir=allure-api-positive
        
        allure serve allure allure-api-positive
    
    Для API тестов (негативные):

        pytest -m api_negative_tests --alluredir=allure-api-negative

        allure serve allure allure-api-negative

    Для UI тестов(позитивные):

        pytest -m ui_positive_tests --alluredir=allure-ui-positive

        allure serve allure llure-ui-positive
    
    Для UI тестов(негативные):

        pytest -m ui_negative_tests --alluredir=allure-ui-negative

        allure serve allure allure-ui-negative
    
    Для запуска всех тестов:

        pytest --alluredir=allure-results

        allure serve allure-results


## Финальный проект

[Ссылка на финальный проект](https://github.com/TimKenessov/qa_automation_course_work)