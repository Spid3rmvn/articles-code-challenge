from lib.db.connection import get_connection
from lib.models.article import Article

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        """Save the author to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        
        if self.id:
            # Update existing author
            cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
        else:
            # Insert new author
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            self.id = cursor.lastrowid
            
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an author by their ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(row['name'], row['id'])
        return None

    @classmethod
    def find_by_name(cls, name):
        """Find an author by their name"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(row['name'], row['id'])
        return None

    def articles(self):
        """Get all articles written by this author"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM articles 
            WHERE author_id = ?
        """, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        """Get all magazines this author has written for"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines

    def add_article(self, magazine_id, title):
        """Create a new article for this author"""
        # Import Article here to avoid circular import
        from lib.models.article import Article
        
        # Create the article object
        article = Article(title, self.id, magazine_id)
        article.save()
        
        # Return the created article
        return article

    def topic_areas(self):
        """Get unique categories of magazines the author has written for"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        categories = [row['category'] for row in cursor.fetchall()]
        conn.close()
        return categories
