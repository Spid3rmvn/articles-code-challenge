#!/usr/bin/env python3
"""
Simple debug file to test your models and database
Run with: python lib/debug.py
"""

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
    print("mag = Magazine('Tech Today', 'Technology')")
    print("article = author.add_article(mag.id, 'The Future of AI')")
    
    print("\n# Get all articles by an author:")
    print("author = Author('Jane Doe')")
    print("articles = author.articles()")
    print("for article in articles:")
    print("    print(f'{article.title} in {article.magazine.name}')")
    
    print("\n# Get all magazines an author contributed to:")
    print("author = Author('Jane Doe')")
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
    
    # Create some sample data for demonstration
    print("\n=== Creating Sample Data ===")
    author1 = Author("Alice")
    author2 = Author("Bob")
    print(f"Created authors: {author1.name}, {author2.name}")
    
    mag1 = Magazine("Tech Monthly", "Technology")
    mag2 = Magazine("Health Today", "Health")
    print(f"Created magazines: {mag1.name}, {mag2.name}")
    
    article1 = author1.add_article(mag1.id, "AI in 2025")
    article2 = author1.add_article(mag2.id, "Healthy Living Tips")
    article3 = author2.add_article(mag1.id, "Cybersecurity Essentials")
    print(f"Created articles: '{article1.title}', '{article2.title}', '{article3.title}'")
    
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
