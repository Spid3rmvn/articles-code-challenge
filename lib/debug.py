#!/usr/bin/env python3
"""
Simple debug file to test your models and database
Run with: python lib/debug.py
"""

import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def show_examples():
    """Display example commands for the user"""
    print("\n=== Example Commands ===")
    print("\n# Create a new author:")
    print("author = Author('Your Name')")
    print("author.save()")
    
    print("\n# Find an author:")
    print("author = Author.find_by_name('John Doe')")
    
    print("\n# Create a magazine:")
    print("mag = Magazine('My Magazine', 'Technology')")
    print("mag.save()")
    
    print("\n# Add an article:")
    print("author = Author('Jane Doe')")
    print("author.save()")
    print("mag = Magazine('Tech Today', 'Technology')")
    print("mag.save()")
    print("article = author.add_article(mag.id, 'The Future of AI')")
    
    print("\n# Get all articles by an author:")
    print("author = Author.find_by_name('Jane Doe')")
    print("articles = author.articles()")
    print("for article in articles:")
    print("    print(f'{article.title} in {article.magazine.name}')")
    
    print("\n# Get all magazines an author contributed to:")
    print("author = Author.find_by_name('Jane Doe')")
    print("magazines = author.magazines()")
    print("for mag in magazines:")
    print("    print(mag.name)")
    
    print("\n# Type 'help()' to see these examples again")
    print("# Type 'exit()' to quit")

def help():
    """Show help information"""
    show_examples()

def main():
    print("=== Article Database Debug Console ===")
    print("\nThis is an interactive tool to test your database and models.")
    print("\nFirst, make sure you've created the database.")
    
    show_examples()
    
    print("\nStarting interactive mode...")
    print("Type 'help()' for examples or 'exit()' to quit\n")
    
    # Import everything so user can test
    import code
    variables = locals()
    variables['help'] = help
    code.interact(local=variables)

if __name__ == "__main__":
    main()
