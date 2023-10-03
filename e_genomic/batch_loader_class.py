import pandas as pd
from e_genomic.api_client_class import GenomicAPIClient
from e_genomic.pipeline_data_class import Pipeline
import re


class BatchLoader(Pipeline):
    def __init__(self):
        super().__init__()

    def __extract_and_load(self, new_data: pd.DataFrame, target_path: str):
        try:
            existing_data = pd.read_csv(target_path)
            is_in_existing = new_data['title'].isin(existing_data['title'])
            new_entries = new_data[~is_in_existing]
            has_new_entries = not new_entries.empty

            if has_new_entries:
                result = pd.concat([new_entries, new_data],
                                   axis=0).reset_index(drop=True)
                result.to_csv(target_path, index=False)
                return {'status': 'success', 'message': 'Novos Dados carregados!'}
            else:
                return {'status': 'success', 'message': 'Não existe dados novos para serem carregados!'}
        except FileNotFoundError:
            new_data.to_csv(target_path, index=False)
            return {'status': 'success', 'message': 'Dados carregados!'}

    def run(self):
        try:
            print("Batch.__run")
            client = GenomicAPIClient()
            news_filtereds = pd.DataFrame(
                client.news_searchs()['articles'])

            regex = re.compile('|'.join(super().key_woods), re.IGNORECASE)

            news_filtereds['title'] = news_filtereds['title'].replace(
                r'^\s*$|\[Removed\]', None, regex=True)
            news_filtereds['description'] = news_filtereds['description'].replace(
                r'^\s*$|\[Removed\]', None, regex=True)
            news_filtereds.dropna(
                subset=['title', 'description'], inplace=True)

            news_filtereds = news_filtereds[news_filtereds.apply(lambda x: bool(regex.search(x['title'])) or
                                                                 bool(regex.search(x['description'])) or
                                                                 bool(regex.search(x['content'])), axis=1)]

            result = self.__extract_and_load(
                new_data=news_filtereds,
                target_path=f"{super().raw_path}/load_batch_news_relevancy.csv"
            )

            return result

        except Exception:
            return {'status': 'error', 'message': 'Falha na operação.'}
