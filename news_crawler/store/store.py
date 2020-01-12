from base64 import b64encode, b64decode
from typing import List
from pathlib import Path

from ..store.file_handler import FileHandler
from ..parser.settings import BasicArticle


class Store:
    def __init__(self, articles: List[BasicArticle], file_handler: FileHandler):
        self.articles = articles
        self.file_handler = file_handler

    def save_articles(self):
        for article in self.articles:
            self.file_handler.write_to_file(file_name=b64encode(article.url), text=article.text)

    def get_articles(self) -> List[BasicArticle]:
        basic_articles = []
        for file_path in self.file_handler.list_files():
            basic_articles.append(self._get_article(file_path))
        return basic_articles

    def _get_article(self, file_path: Path) -> BasicArticle:
        file_text = self.file_handler.read_from_file(file_path)
        return BasicArticle(url=b64decode(file_path.stem), text=file_text)
