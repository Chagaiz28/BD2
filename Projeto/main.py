from database import Database
from librarydatabase import LibraryDatabase

def main_menu(library_db):
    while True:
        print("1. Create Author")
        print("2. Create Book")
        print("3. Add Author to Book")
        print("4. Update Author Name")
        print("5. Update Book Title")
        print("6. List Authors")
        print("7. List Books")
        print("8. List Author Books")
        print("9. Delete Author")
        print("10. Delete Book")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            author_id = input("Enter author ID: ")
            name = input("Enter author name: ")
            library_db.create_author(author_id, name)
        elif choice == '2':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            library_db.create_book(book_id, title)
        elif choice == '3':
            author_id = input("Enter author ID: ")
            book_id = input("Enter book ID: ")
            library_db.add_author_to_book(author_id, book_id)
        elif choice == '4':
            author_id = input("Enter author ID: ")
            new_name = input("Enter new author name: ")
            library_db.update_author_name(author_id, new_name)
        elif choice == '5':
            book_id = input("Enter book ID: ")
            new_title = input("Enter new book title: ")
            library_db.update_book_title(book_id, new_title)
        elif choice == '6':
            authors = library_db.get_authors()
            for author in authors:
                print(f"ID: {author['id']}, Name: {author['name']}")
        elif choice == '7':
            books = library_db.get_books()
            for book in books:
                print(f"ID: {book['id']}, Title: {book['title']}")
        elif choice == '8':
            author_id = input("Enter author ID: ")
            books = library_db.get_author_books(author_id)
            for book in books:
                print(f"ID: {book['id']}, Title: {book['title']}")
        elif choice == '9':
            author_id = input("Enter author ID to delete: ")
            library_db.delete_author(author_id)
        elif choice == '10':
            book_id = input("Enter book ID to delete: ")
            library_db.delete_book(book_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    db = Database("neo4j+s://efaa3965.databases.neo4j.io", "neo4j", "Mb0EOi68tISoaWvBPRIhW-peX7fdr30OiOyU51hly5o")
    db.drop_all()
    library_db = LibraryDatabase(db)
    main_menu(library_db)
    db.close()
