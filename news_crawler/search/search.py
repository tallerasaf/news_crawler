from typing import List

from ..parser.settings import BasicArticle


class Search:
    def __init__(self, articles: List[BasicArticle]):
        self.articles = articles

    def get_articles_by_phrase(self, phrase: str):
        return [article for article in self.articles if phrase in article.text]
