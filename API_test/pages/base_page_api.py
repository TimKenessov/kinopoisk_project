import requests


class BaseAPI:
    base_url = "https://api.kinopoisk.dev/v1.4"
    api_key = "CKSK9H2-NEN4NE3-HDMTDYW-Z7FNH4A"
    response: requests.Response
    headers = {
        "x-api-key": api_key,
    }

    def get(self, endpoint, params):
        url = f"{self.base_url}{endpoint}"
        self.response = requests.get(url, headers=self.headers, params=params)
        return self.response

    def code_status_is(self, status):
        return self.response.status_code == status
