# Database package initialization

"""
Database utilities for the Articles application.
"""

# Import database connection function
from .connection import get_connection

# Make get_connection available at package level
__all__ = ["get_connection"]
