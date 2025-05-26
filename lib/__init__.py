# This file makes the lib directory a Python package

"""
Main library package for the Articles Code Challenge.
"""

# Import key components for easy access
from . import models
from . import db

# Package metadata
__version__ = "1.0.0"
__all__ = ["models", "db"]
