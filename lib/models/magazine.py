from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        """Save the magazine to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        
        if self.id:
            # Update existing magazine
            cursor.execute("""
                UPDATE magazines SET name = ?, category = ? 
                WHERE id = ?
            """, (self.name, self.category, self.id))
        else:
            # Insert new magazine
            cursor.execute("""
                INSERT INTO magazines (name, category) 
                VALUES (?, ?)
            """, (self.name, self.category))
            self.id = cursor.lastrowid
            
        conn.commit()
        conn.close()
        return self

    @classmethod
    def create(cls, name, category):
        """Create and save a new magazine"""
        magazine = cls(name, category)
        return magazine.save()

    @classmethod
    def find_by_id(cls, id):
        """Find a magazine by its ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(row['name'], row['category'], row['id'])
        return None

    @classmethod
    def find_by_name(cls, name):
        """Find a magazine by its name"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(row['name'], row['category'], row['id'])
        return None

    @classmethod
    def all(cls):
        """Get all magazines"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        magazines = []
        for row in cursor.fetchall():
            magazines.append(cls(row['name'], row['category'], row['id']))
        conn.close()
        return magazines

    def delete(self):
        """Delete the magazine from the database"""
        if not self.id:
            return False
            
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
        self.id = None
        return True

    def articles(self):
        """Get all articles published in this magazine"""
        from lib.models.article import Article
        
        if not self.id:
            return []
            
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM articles 
            WHERE magazine_id = ?
        """, (self.id,))
        
        articles = []
        for row in cursor.fetchall():
            article = Article.find_by_id(row['id'])
            if article:
                articles.append(article)
                
        conn.close()
        return articles

    def contributors(self):
        """Get all authors who have written for this magazine"""
        from lib.models.author import Author
        
        if not self.id:
            return []
            
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT author_id FROM articles
            WHERE magazine_id = ?
        """, (self.id,))
        
        authors = []
        for row in cursor.fetchall():
            author = Author.find_by_id(row['author_id'])
            if author:
                authors.append(author)
                
        conn.close()
        return authors

    def article_titles(self):
        """Get titles of all articles in this magazine"""
        if not self.id:
            return []
            
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title FROM articles 
            WHERE magazine_id = ?
        """, (self.id,))
        
        titles = [row['title'] for row in cursor.fetchall()]
        conn.close()
        return titles

    def contributing_authors(self):
        """Get authors with more than 2 articles in this magazine"""
        from lib.models.author import Author
        
        if not self.id:
            return []
            
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT author_id FROM articles
            WHERE magazine_id = ?
            GROUP BY author_id
            HAVING COUNT(id) > 2
        """, (self.id,))
        
        authors = []
        for row in cursor.fetchall():
            author = Author.find_by_id(row['author_id'])
            if author:
                authors.append(author)
                
        conn.close()
        return authors
