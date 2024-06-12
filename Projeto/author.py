class Author:
    def __init__(self, db, author_id, name):
        self.db = db
        self.id = author_id
        self.name = name

    def create(self):
        query = "CREATE (a:Author {id: $author_id, name: $name})"
        self.db.execute_query(query, {'author_id': self.id, 'name': self.name})

    def update_name(self, new_name):
        query = "MATCH (a:Author {id: $author_id}) SET a.name = $new_name"
        self.db.execute_query(query, {'author_id': self.id, 'new_name': new_name})

    def delete(self):
        query = "MATCH (a:Author {id: $author_id}) DETACH DELETE a"
        self.db.execute_query(query, {'author_id': self.id})

    def get_books(self):
        query = """
        MATCH (a:Author {id: $author_id})-[:WROTE]->(b:Book)
        RETURN b
        """
        return self.db.execute_query(query, {'author_id': self.id})

    @staticmethod
    def get_all(db):
        query = "MATCH (a:Author) RETURN a"
        return db.execute_query(query)