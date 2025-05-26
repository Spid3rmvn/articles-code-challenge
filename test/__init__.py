"""
Test package for the articles code challenge.

This package contains all test modules for testing the functionality
of the articles database application.
"""

import sys
import os

# Add the parent directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test modules
from . import test_article
from . import test_author
from . import test_magazine

__all__ = ['test_article', 'test_author', 'test_magazine']

# Test configuration
TEST_DATABASE = 'test_articles.db'
