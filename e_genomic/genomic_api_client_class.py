import requests


class GenomicAPIClient:

    def __init__(self, url):
        self.url = url
        self.api_key = "aa603652ad8d4f0d8da9a9d3b52a0efb"

    def __get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def __params(self):
        return {
            'q': 'genômica OR medicina personalizada'
        }

    def news_searchs(self):
        response = requests.get(
            url=self.url,
            headers=self.__get_headers(),
            params=self.__params()
        )
        news = response.json()
        return news
