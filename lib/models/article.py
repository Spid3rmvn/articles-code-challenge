from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        """Save the article to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        
        if self.id:
            # Update existing article
            cursor.execute("""
                UPDATE articles SET title = ?, author_id = ?, magazine_id = ? 
                WHERE id = ?
            """, (self.title, self.author_id, self.magazine_id, self.id))
        else:
            # Insert new article
            cursor.execute("""
                INSERT INTO articles (title, author_id, magazine_id) 
                VALUES (?, ?, ?)
            """, (self.title, self.author_id, self.magazine_id))
            self.id = cursor.lastrowid
            
        conn.commit()
        conn.close()
        return self

    @classmethod
    def find_by_id(cls, id):
        """Find an article by its ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(row['title'], row['author_id'], row['magazine_id'], row['id'])
        return None

    @classmethod
    def find_by_title(cls, title):
        """Find articles by title"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        articles = []
        for row in cursor.fetchall():
            articles.append(cls(row['title'], row['author_id'], row['magazine_id'], row['id']))
        conn.close()
        return articles
    
    @classmethod
    def all(cls):
        """Get all articles from the database"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        articles = []
        for row in cursor.fetchall():
            articles.append(cls(row['title'], row['author_id'], row['magazine_id'], row['id']))
        conn.close()
        return articles

    def author(self):
        """Get the author of this article"""
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        """Get the magazine this article was published in"""
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)
