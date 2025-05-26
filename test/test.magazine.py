import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models.magazine import Magazine


class TestMagazine(unittest.TestCase):
    """Simple tests for Magazine class"""
    
    def test_magazine_creation(self):
        """Test creating a magazine"""
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertIsNone(magazine.id)
    
    def test_magazine_with_id(self):
        """Test creating a magazine with ID"""
        magazine = Magazine("Science Today", "Science", 2)
        self.assertEqual(magazine.name, "Science Today")
        self.assertEqual(magazine.category, "Science")
        self.assertEqual(magazine.id, 2)


if __name__ == '__main__':
    unittest.main()
