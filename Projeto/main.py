from database import Database
from author import Author
from book import Book

def main_menu(db):
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
            author = Author(db, author_id, name)
            author.create()
        elif choice == '2':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            book = Book(db, book_id, title)
            book.create()
        elif choice == '3':
            author_id = input("Enter author ID: ")
            book_id = input("Enter book ID: ")
            author = Author(db, author_id, '')
            book = Book(db, book_id, '')
            book.add_author(author)
        elif choice == '4':
            author_id = input("Enter author ID: ")
            new_name = input("Enter new author name: ")
            author = Author(db, author_id, new_name)
            author.update_name(new_name)
        elif choice == '5':
            book_id = input("Enter book ID: ")
            new_title = input("Enter new book title: ")
            book = Book(db, book_id, new_title)
            book.update_title(new_title)
        elif choice == '6':
            authors = Author.get_all(db)
            for author in authors:
                print(f"ID: {author['id']}, Name: {author['name']}")
        elif choice == '7':
            books = Book.get_all(db)
            for book in books:
                print(f"ID: {book['id']}, Title: {book['title']}")
        elif choice == '8':
            author_id = input("Enter author ID: ")
            author = Author(db, author_id, '')
            books = author.get_books()
            for book in books:
                print(f"ID: {book['id']}, Title: {book['title']}")
        elif choice == '9':
            author_id = input("Enter author ID to delete: ")
            author = Author(db, author_id, '')
            author.delete()
        elif choice == '10':
            book_id = input("Enter book ID to delete: ")
            book = Book(db, book_id, '')
            book.delete()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    db = Database("neo4j+s://efaa3965.databases.neo4j.io", "neo4j", "Mb0EOi68tISoaWvBPRIhW-peX7fdr30OiOyU51hly5o")
    main_menu(db)
    db.close()