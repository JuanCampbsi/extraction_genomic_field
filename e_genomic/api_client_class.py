import requests
import os
from dotenv import load_dotenv

load_dotenv()


class GenomicAPIClient:

    def __init__(self):
        self.__url = "https://newsapi.org/v2/everything"
        self.__api_key = os.getenv("API_KEY")

    def __get_headers(self):
        return {
            "Authorization": f"Bearer {self.__api_key}",
            "Content-Type": "application/json"
        }

    def __params(self):
        return {
            'q': 'DNA OR GENÉTICAS OR SEQUENCIAMENTO OR DOENÇAS OR TERAPIAS',
            'language': 'pt',
            'sortBy': 'relevancy'
        }

    def news_searchs(self):
        response = requests.get(
            url=self.__url,
            headers=self.__get_headers(),
            params=self.__params()
        )
        return response.json()
