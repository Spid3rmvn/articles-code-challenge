from lib.models.article import Article


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def write_article(self, magazine, title):
        article = Article(title, self, magazine)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})
