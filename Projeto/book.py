class Book:
    def __init__(self, db, book_id, title):
        self.db = db
        self.id = book_id
        self.title = title

    def create(self):
        query = "CREATE (b:Book {id: $book_id, title: $title})"
        self.db.execute_query(query, {'book_id': self.id, 'title': self.title})

    def update_title(self, new_title):
        query = "MATCH (b:Book {id: $book_id}) SET b.title = $new_title"
        self.db.execute_query(query, {'book_id': self.id, 'new_title': new_title})

    def delete(self):
        query = "MATCH (b:Book {id: $book_id}) DETACH DELETE b"
        self.db.execute_query(query, {'book_id': self.id})

    def add_author(self, author):
        query = """
        MATCH (a:Author {id: $author_id})
        MATCH (b:Book {id: $book_id})
        CREATE (a)-[:WROTE]->(b)
        """
        self.db.execute_query(query, {'author_id': author.id, 'book_id': self.id})

    @staticmethod
    def get_all(db):
        query = "MATCH (b:Book) RETURN b"
        return db.execute_query(query)