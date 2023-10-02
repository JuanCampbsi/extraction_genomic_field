from e_genomic.genomic_api_client_class import GenomicAPIClient
import pandas as pd
import re
from enum import Enum
from io import StringIO


class TypeFormat(Enum):
    json = 1,
    parquet = 2


class Pipeline:

    def __init__(self):
        self.__raw_path = "/Users/juancampos/Projects/ada_santander_coders/LMS1011_ada_santander_coders/extraction_genomic_field/e_genomic/raw"
        self.__enum = TypeFormat
        self.__key_woods = ['DNA', 'GENÉTICAS', 'TERAPIAS',
                            'SEQUENCIAMENTO', 'DOENÇAS']

    def filtrar_news(self, news: pd.DataFrame):
        print("Pipeline.__filtreds")

        regex = re.compile('|'.join(self.__key_woods), re.IGNORECASE)

        news = news.assign(title=news['title'].fillna(
            ''), description=news['description'].fillna(''), content=news['content'].fillna(''))

        news_filtreds = news[news.apply(lambda x: bool(regex.search(
            x['title'])) or bool(regex.search(x['description'])) or bool(regex.search(x['content'])), axis=1)]

        return news_filtreds

    def __load(self, df: pd.DataFrame, format: int, path: str):
        if format == self.__enum.json.value:
            df.to_json(path, orient="records", mode="w")
        elif format == self.__enum.parquet.value:
            df.to_parquet(path, index=False, compression="gzip")

    def __transform(self, df_news: pd.DataFrame, target_path: str, target_format: str):
        print("Pipeline.__transform")

        # 4.1 - Quantidade de notícias por ano, mês e dia de publicação
        df_news['publishedAt'] = pd.to_datetime(df_news['publishedAt'])
        df_news['year'] = df_news['publishedAt'].dt.year
        df_news['month'] = df_news['publishedAt'].dt.month
        df_news['day'] = df_news['publishedAt'].dt.day
        news_data = df_news.groupby(['year', 'month', 'day']).size()
        # print("news_data", news_data)

        # 4.2 - Quantidade de notícias por fonte e autor
        df_news['source_name'] = df_news['source'].apply(
            lambda x: x['name'] if isinstance(x, dict) and 'name' in x else 'NaN')
        news_by_source_author = df_news.groupby(
            ['source_name', 'author']).size()
        print("news_by_source_author", df_news['source'])

        # # 4.3 - Quantidade de aparições de 3 palavras chaves por ano, mês e dia de publicação
        # df_news['keywords'] = df_news['title'].apply(
        #     lambda x: any(word in x.upper() for word in self.__key_woods))
        # news_words_keys = df_news[df_news['keywords']].groupby(
        #     ['year', 'month', 'day']).size()

        # print("news_words_keys", news_words_keys)

        # df_result_transformed = df_news

        # self.__load(
        #     df=df_result_transformed,
        #     format=self.__enum[target_format].value,
        #     path=target_path
        # )

    def run(self):
        print("Pipeline.__run")
        client = GenomicAPIClient(url="https://newsapi.org/v2/everything")
        news_filtereds = self.filtrar_news(pd.DataFrame(
            client.news_searchs()['articles']))

        # Apply Data Transformations
        self.__transform(
            df_news=news_filtereds,
            target_path=f"{self.__raw_path}/news_transformation.parquet.gz",
            target_format="parquet"
        )
