# Articles Database Project

A simple project to manage Authors, Articles, and Magazines using Python and SQLite.

## Quick Start Guide

### Step 1: Set Up Your Environment

First, make sure you have Python installed. Then:

```bash
# Install pipenv if you don't have it
pip install pipenv

# Install project dependencies
pipenv install

# Activate the virtual environment
pipenv shell
```

### Step 2: Create the Database

Run this command to create your database:

```bash
python scripts/setup_db.py
```

This creates an `articles.db` file with three tables:
- **authors** - Stores author information
- **magazines** - Stores magazine information  
- **articles** - Connects authors and magazines

### Step 3: Add Sample Data

Run this to add some test data:

```bash
python lib/db/seed.py
```

### Step 4: Try It Out!

Run the example queries:

```bash
python scripts/run_queries.py
```

Or play with the debug console:

```bash
python lib/debug.py
```

## Project Structure

```
articles-code-challenge/
├── lib/                    # Main code folder
│   ├── models/            # Database models (Author, Article, Magazine)
│   ├── db/                # Database files
│   │   ├── connection.py  # Database connection
│   │   ├── schema.sql     # Table definitions
│   │   └── seed.py        # Sample data
│   └── debug.py           # Interactive testing
├── scripts/               # Helper scripts
│   ├── setup_db.py        # Creates the database
│   └── run_queries.py     # Example queries
└── test/                  # Test files (for later)
```

## How to Use

### Creating Records

```python
# Create an author
author = Author("Your Name")
author.save()

# Create a magazine
magazine = Magazine("Tech Today", "Technology")
magazine.save()

# Create an article
article = Article("My First Article", author.id, magazine.id)
article.save()
```

### Finding Records

```python
# Find by ID
author = Author.find_by_id(1)

# Find by name
magazine = Magazine.find_by_name("Tech Today")
```

### Getting Related Data

```python
# Get all articles by an author
articles = author.articles()

# Get all magazines an author wrote for
magazines = author.magazines()

# Get all articles in a magazine
articles = magazine.articles()
```

## Tips for Beginners

1. **Start Small**: Try creating one author, one magazine, and one article first
2. **Use the Debug Console**: Run `python lib/debug.py` to experiment
3. **Check Your Database**: The `articles.db` file contains all your data
4. **Read the Error Messages**: They often tell you exactly what's wrong

## Common Issues

- **"No such table" error**: Run `python scripts/setup_db.py` first
- **"No data found"**: Run `python lib/db/seed.py` to add sample data
- **Import errors**: Make sure you're in the project folder and activated pipenv

Happy coding! 🚀
