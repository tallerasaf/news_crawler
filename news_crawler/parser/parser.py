import newspaper
from typing import List

from ..parser.settings import BasicArticle


class Parser:
    def __init__(self, articles : List[newspaper.Article]):
        self._articles = articles

    @property
    def articles(self):
        return [BasicArticle(text=newspaper.fulltext(article), url=article.url) for article in self._articles]
