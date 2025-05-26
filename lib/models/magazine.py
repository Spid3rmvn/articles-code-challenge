class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return [
            author for author in self.contributors()
            if sum(1 for a in self._articles if a.author == author) > 2
        ]
