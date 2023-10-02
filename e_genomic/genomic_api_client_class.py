import requests
import os
from dotenv import load_dotenv

load_dotenv()


class GenomicAPIClient:

    def __init__(self, url: str):
        self.url = url
        self.api_key = os.getenv("API_KEY")

    def __get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def __params(self):
        return {
            'q': 'DNA OR GENÉTICAS OR SEQUENCIAMENTO OR DOENÇAS OR TERAPIAS',
            'language': 'pt'
        }

    def news_searchs(self):
        response = requests.get(
            url=self.url,
            headers=self.__get_headers(),
            params=self.__params()
        )
        news = response.json()
        return news
