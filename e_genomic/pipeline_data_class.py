from e_genomic.api_client_class import GenomicAPIClient
import pandas as pd
import re
from enum import Enum


class TypeFormat(Enum):
    json = 1,
    parquet = 2


class Pipeline:

    def __init__(self):
        self.__raw_path = "/Users/juancampos/Projects/ada_santander_coders/LMS1011_ada_santander_coders/extraction_genomic_field/e_genomic/raw"
        self.__enum = TypeFormat
        self.__key_woods = ['DNA', 'GENÉTICAS', 'TERAPIAS',
                            'SEQUENCIAMENTO', 'DOENÇAS']

    @property
    def raw_path(self) -> str:
        return self.__raw_path

    @property
    def key_woods(self) -> list[str]:
        return self.__key_woods

    def __load(self, df: pd.DataFrame, format: int, path: str):
        if format == self.__enum.json.value:
            df.to_json(path, orient="records", mode="w")
        elif format == self.__enum.parquet.value:
            df.to_parquet(path, index=False, compression="gzip")

    def __transform(self, df_news: pd.DataFrame, target_format: str):
        print("Pipeline.__transform")

        # 4.1 - Quantidade de notícias por ano, mês e dia de publicação
        df_news['publishedAt'] = pd.to_datetime(df_news['publishedAt'])
        df_news['year'] = df_news['publishedAt'].dt.year
        df_news['month'] = df_news['publishedAt'].dt.month
        df_news['day'] = df_news['publishedAt'].dt.day
        count_news_date = df_news.groupby(
            ['year', 'month', 'day']).size().reset_index(name='count_news')

        # 4.2 - Quantidade de notícias por fonte e autor
        df_news['source_name'] = df_news['source'].apply(
            lambda x: x['name'] if isinstance(x, dict) and 'name' in x else 'NaN')
        count_by_source_author = df_news.groupby(
            ['source_name', 'author']).size().reset_index(name='count_source')

        # 4.3 - Quantidade de aparições de 3 palavras chaves por ano, mês e dia de publicação
        df_news['keywords'] = df_news['title'].apply(
            lambda x: any(word in x.upper() for word in self.__key_woods))
        counts_words_keys = df_news[df_news['keywords']].groupby(
            ['year', 'month', 'day']).size().reset_index(name='count_keywords')

        df_result_transformed = {
            'count_news_date': count_news_date,
            'count_by_source_author': count_by_source_author,
            'count_words_keys': counts_words_keys
        }

        for name, dataframe in df_result_transformed.items():
            display(dataframe)
            self.__load(
                df=dataframe,
                format=self.__enum[target_format].value,
                path=f"{self.__raw_path}/{name}.parquet.gz"
            )

    def run(self):
        try:
            print("Pipeline.__run")

            news_filtereds = pd.read_csv(
                f"{self.__raw_path}/load_batch_news_relevancy.csv")

            # Aplicando transformações de dados
            self.__transform(
                df_news=news_filtereds,
                target_format="parquet"
            )

            return {'status': 'success', 'message': 'Dados transformados e carregados!'}

        except Exception as e:
            return {'status': 'error', 'message': 'Falha na operação.'}
