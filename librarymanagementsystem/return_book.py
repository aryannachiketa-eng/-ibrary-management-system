from utils import books, issued_books

def return_book():
    book_id = input("enter book id: ")

    if book_id in issued_books:  

        books[book_id] = issued_books.pop(book_id) 
        print("thank you for using")

    else:
        print(f"Book was not issued")