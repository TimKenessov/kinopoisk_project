from API_test.pages.base_page_api import BaseAPI


class SearchAPI(BaseAPI):

    # Поиск фильма по названию
    def search_movie(self, query):
        params = {"query": query}
        return self.get("/movie/search", params=params)

    # Поиск фильмов по жанру

    def get_movielist_by_genre(self, year, genre):
        params = {"year": year, "genres.name": genre}
        return self.get("/movie", params=params)

    # Поиск фильмов по рейтингу Кинопоиск

    def get_movielist_by_rating(self, rating):
        params = {"field": rating}
        return self.get("/movie", params)
