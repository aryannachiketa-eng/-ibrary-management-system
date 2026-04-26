from utils import books

def add():
    book_id = input("Enter Book ID: ").upper()
    book_name = input("Enter Book Name: ").upper()

    books[book_id] = book_name   
    print(f"Book Added successfully: {book_name}")