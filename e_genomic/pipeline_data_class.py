from e_genomic.genomic_api_client_class import GenomicAPIClient


class Pipeline:

    def __init__(self, url):
        self.genomic_api_client = GenomicAPIClient(url)

    def filtrar_news(self, news):
        news_filtered = [item for item in news
                         if any(word in item['title'] or word in item['description']
                                for word in self.words_key)]
        return news_filtered
