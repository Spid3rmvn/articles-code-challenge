import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models.author import Author


class TestAuthor(unittest.TestCase):
    """Simple tests for Author class"""
    
    def test_author_creation(self):
        """Test creating an author"""
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertIsNone(author.id)
    
    def test_author_with_id(self):
        """Test creating an author with ID"""
        author = Author("Jane Smith", 3)
        self.assertEqual(author.name, "Jane Smith")
        self.assertEqual(author.id, 3)


if __name__ == '__main__':
    unittest.main()
