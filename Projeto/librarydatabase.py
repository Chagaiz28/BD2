class LibraryDatabase:
    def __init__(self, db):
        self.db = db

    def create_author(self, author_id, name):
        query = "CREATE (a:Author {id: $author_id, name: $name})"
        self.db.execute_query(query, {'author_id': author_id, 'name': name})

    def create_book(self, book_id, title):
        query = "CREATE (b:Book {id: $book_id, title: $title})"
        self.db.execute_query(query, {'book_id': book_id, 'title': title})

    def add_author_to_book(self, author_id, book_id):
        query = """
        MATCH (a:Author {id: $author_id})
        MATCH (b:Book {id: $book_id})
        CREATE (a)-[:WROTE]->(b)
        """
        self.db.execute_query(query, {'author_id': author_id, 'book_id': book_id})

    def update_author_name(self, author_id, new_name):
        query = "MATCH (a:Author {id: $author_id}) SET a.name = $new_name"
        self.db.execute_query(query, {'author_id': author_id, 'new_name': new_name})

    def update_book_title(self, book_id, new_title):
        query = "MATCH (b:Book {id: $book_id}) SET b.title = $new_title"
        self.db.execute_query(query, {'book_id': book_id, 'new_title': new_title})

    def get_authors(self):
        query = "MATCH (a:Author) RETURN a"
        return self.db.execute_query(query)

    def get_books(self):
        query = "MATCH (b:Book) RETURN b"
        return self.db.execute_query(query)

    def get_author_books(self, author_id):
        query = """
        MATCH (a:Author {id: $author_id})-[:WROTE]->(b:Book)
        RETURN b
        """
        return self.db.execute_query(query, {'author_id': author_id})

    def delete_author(self, author_id):
        query = "MATCH (a:Author {id: $author_id}) DETACH DELETE a"
        self.db.execute_query(query, {'author_id': author_id})

    def delete_book(self, book_id):
        query = "MATCH (b:Book {id: $book_id}) DETACH DELETE b"
        self.db.execute_query(query, {'book_id': book_id})