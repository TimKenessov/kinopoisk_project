from selenium.webdriver.common.by import By


class SearchFieldLocators:
    search_field = (By.NAME, "kp_query")
    search_button = (By.CLASS_NAME, "styles_root__CUh_v")
    search_results = (By.CSS_SELECTOR, ".search_results .element.most_wanted")
    search_results_message = (By.CSS_SELECTOR, "h2.textorangebig")


class ExpandedSearchLocators:
    ex_search_button = (By.XPATH, '//a[@aria-label="Расширенный поиск"]')
    ex_search_movie_field = (By.CLASS_NAME, "el_1")
    ex_search_movie_year = (By.CLASS_NAME, "el_2")
    ex_search_movie_country = (By.CLASS_NAME, "el_5")
    ex_search_movie_genre = (By.CLASS_NAME, "el_6")
    ex_search_movie_actor = (By.CLASS_NAME, "el_9")
    ex_search_movie_button = (By.CLASS_NAME, "el_18")


class MovieResultPageLocators:
    movie_card = (By.XPATH,
                  '(//div[contains(@class, "search_results")]//a)[3]')

    #  [2] - актёры
    #  [3] - трейлеры
    #  [4] - кадры
    #  [5] - постеры
    #  [6] - сайты
