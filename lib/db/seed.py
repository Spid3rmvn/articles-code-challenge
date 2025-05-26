from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    """Populate the database with sample data"""
    # Clear existing data
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()
    
    # Create authors
    author1 = Author("John Doe")
    author1.save()
    
    author2 = Author("Jane Smith")
    author2.save()
    
    author3 = Author("Bob Johnson")
    author3.save()
    
    # Create magazines
    mag1 = Magazine("Tech Weekly", "Technology")
    mag1.save()
    
    mag2 = Magazine("Science Today", "Science")
    mag2.save()
    
    mag3 = Magazine("Art Review", "Arts")
    mag3.save()
    
    # Create articles
    article1 = Article("Python Tips", author1.id, mag1.id)
    article1.save()
    
    article2 = Article("Database Design", author1.id, mag1.id)
    article2.save()
    
    article3 = Article("Web Development", author2.id, mag1.id)
    article3.save()
    
    article4 = Article("Space Exploration", author2.id, mag2.id)
    article4.save()
    
    article5 = Article("Modern Art", author3.id, mag3.id)
    article5.save()
    
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
