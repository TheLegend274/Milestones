class Book:
    def __init__(self, title, author, isbn, is_checked_out):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f'The book {self.title} by {self.author} has been checked out successfully')
            return True
        else:
            print(f'The book {self.title} by {self.author} is already checked out')
            return False  # Return False when the book is already checked out

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f'The book {self.title} by {self.author} has been returned')
        else:
            print(f'The book {self.title} by {self.author} has not been checked out')

    def get_info(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Checked out: {self.is_checked_out}'


class Library:
    def __init__(self, name):
        self.catalog = []
        self.name = name

    def add_book(self, book):
        # Check if the ISBN is already in the catalog
        for existing_book in self.catalog:
            if existing_book.isbn == book.isbn:
                print(f'The book {book.title} is already in the list')
                return

        self.catalog.append(book)
        print(f'The book {book.title} has been added')

    def remove_book(self, isbn):
        # Find the book with the given ISBN and remove it
        for book in self.catalog:
            if book.isbn == isbn:
                self.catalog.remove(book)
                print(f'Book with ISBN {isbn} has been removed')
            else:
                print("Book can not be found ")

        print(f'Book with ISBN {isbn} not found in the catalog')

    def find_book(self, isbn):
        for book in self.catalog:
            if book.isbn == isbn:
                return book


    def list_books(self):
        print(f'{self.name} Library Catalog')
        for book in self.catalog:
            print(book.get_info())
        print("\n")


    def check_out_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            book.check_out()
        else:
            print(f'The Book with ISBN {isbn} was not found in the library')

    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            book.return_book()
        else:
            print(f'Book with ISBN {isbn} has not been returned')


my_library = Library("My Local Library")

# Adding books
my_library.add_book(Book("1984", "George Orwell", "1234567890",False))
print()
my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "1234567891",False))
print()
# Listing books
my_library.list_books()
print()

# Checking out a book
my_library.check_out_book("1234567890")
print()
# Trying to check out the same book again (should handle this error)
my_library.check_out_book("1234567890")
print()
# Returning a book
my_library.return_book("1234567890")
print()
# Removing a book
my_library.remove_book("1234567891")
print()
# Listing books again to see changes
my_library.list_books()