from utils import books, issued_books

def issue():
    book_id = input("Enter Book ID to issue: ")

    if book_id in books:    

        issued_books[book_id] = books.pop(book_id)   
        print("Book issued successfully")

    else:
        print("Book not available")