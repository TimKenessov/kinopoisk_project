import pytest
from API_test.pages.elements_page_api import SearchAPI


@pytest.fixture(scope="session")
def search_api():
    return SearchAPI()
