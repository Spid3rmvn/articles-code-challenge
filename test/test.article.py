import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models.article import Article


class TestArticle(unittest.TestCase):
    """Simple tests for Article class"""
    
    def test_article_creation(self):
        """Test creating an article"""
        article = Article("Test Article", 1, 1)
        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)
        self.assertIsNone(article.id)
    
    def test_article_with_id(self):
        """Test creating an article with ID"""
        article = Article("Test Article", 1, 1, 5)
        self.assertEqual(article.id, 5)
    
    def test_article_title(self):
        """Test article title getter and setter"""
        article = Article("Original Title", 1, 1)
        article.title = "Updated Title"
        self.assertEqual(article.title, "Updated Title")
    
    def test_article_author_id(self):
        """Test article author_id getter and setter"""
        article = Article("Test Article", 1, 1)
        article.author_id = 2
        self.assertEqual(article.author_id, 2)
    
    def test_article_magazine_id(self):
        """Test article magazine_id getter and setter"""
        article = Article("Test Article", 1, 1)
        article.magazine_id = 3
        self.assertEqual(article.magazine_id, 3)


if __name__ == '__main__':
    unittest.main()
