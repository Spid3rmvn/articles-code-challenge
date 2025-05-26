# Models package initialization

"""
Data models for the Articles application.
"""

# Import all model classes
from .article import Article
from .author import Author
from .magazine import Magazine

# Make models available at package level
__all__ = ["Article", "Author", "Magazine"]
