class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_available(self):
        if self._is_checked_out:
            return False
        return True

    def return_book(self):
        self._is_checked_out = False

    def check_out_book(self):
        self._is_checked_out = True

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title and book.is_available():
                book.check_out_book()

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title and not book.is_available():
                book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(book.title, "by", book.author)
