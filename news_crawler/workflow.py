from news_crawler.crawler import Crawler
from news_crawler.parser import Parser
from news_crawler.store import Store
from news_crawler.settings import ARTICLES_DIR
from news_crawler.store import FileHandler
from news_crawler.search import Search

SOME_PHRASE = "bla"


class Workflow:
    def __init__(self):
        self._file_handler = FileHandler(folder_path=ARTICLES_DIR)
        self.crawler = Crawler(self._file_handler)
        self.parser = Parser(self.crawler.articles)
        self.articles = self.parser.articles
        self.store = Store(self.articles, self._file_handler)
        self.search = Search(self.store.get_articles())

    def run(self):
        print([article.url for article in self.search.get_articles_by_phrase(SOME_PHRASE)])
