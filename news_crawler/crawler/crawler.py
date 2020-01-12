import newspaper
from base64 import b64decode

from ..crawler.settings import URLS
from ..utils import flattened_list
from ..store import FileHandler


class Crawler:
    def __init__(self, file_handler: FileHandler):
        self._file_handler = file_handler
        self.urls = URLS

    @property
    def papers(self):
        return [newspaper.build(url) for url in self.urls]

    @property
    def articles(self):
        return self.filter_articles(flattened_list(self._get_articles()))

    def filter_articles(self, articles):
        article_urls = self._get_article_urls()
        return list(set(articles) - set(article_urls))

    def _get_article_urls(self):
        return [b64decode(file_path.stem) for file_path in self._file_handler.list_files()]

    def _get_articles(self):
        articles = []
        for paper in self.papers:
            paper.download_articles()
            articles.append(paper.articles)
        return articles
