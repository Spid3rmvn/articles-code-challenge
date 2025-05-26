# Articles Database Project

A simple project to manage Authors, Articles, and Magazines using Python and SQLite.

## Project Overview

This project implements a database system for tracking articles, authors, and magazines. It uses SQLite for data storage and provides Python models for interacting with the database.

## Project Structure

```
articles-code-challenge/
├── lib/                    # Main code folder
│   ├── models/            # Database models
│   │   ├── __init__.py    # Package initialization
│   │   ├── article.py     # Article model
│   │   ├── author.py      # Author model
│   │   └── magazine.py    # Magazine model
│   ├── db/                # Database files
│   │   ├── connection.py  # Database connection
│   │   ├── schema.sql     # Table definitions
│   │   └── seed.py        # Sample data
│   └── debug.py           # Interactive testing
├── scripts/               # Helper scripts
│   ├── setup_db.py        # Creates the database
│   └── run_queries.py     # Example queries
└── test/                  # Test files
    ├── __init__.py        # Test package initialization
    ├── test_article.py    # Article tests
    ├── test_author.py     # Author tests
    └── test_magazine.py   # Magazine tests
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install required packages:
```bash
pip install pytest
```

3. Set up the database:
```bash
python scripts/setup_db.py
```

4. Add sample data (optional):
```bash
python lib/db/seed.py
```

## Running Tests

Run tests using pytest:
```bash
python -m pytest test/
```

## Using the Application

You can use the interactive debug console to experiment with the models:
```bash
python lib/debug.py
```

Example operations:
```python
# Create a new author
author = Author("John Doe")
author.save()

# Create a magazine
magazine = Magazine("Tech Weekly", "Technology")
magazine.save()

# Create an article
article = Article("Python Tips", author.id, magazine.id)
article.save()
```

## Current Status

- Basic models implemented (Author, Article, Magazine)
- Database schema created
- Test files set up
- Interactive debugging console available

## Next Steps

- Implement additional query methods
- Add more comprehensive tests
- Create a user interface
