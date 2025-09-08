class Library:
    def __init__(self, books, initial_books):
        self.books = books
        self.initial_books = initial_books
        
    def add_book(self, book):
        self.books.append(book)
        self.initial_books.append(book)

    def remove_book(self, book):
        if book in self.initial_books:
            self.initial_books.remove(book)
            if book in self.books:
                self.books.remove(book)
            return True
        else:
            return False

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        else:
            return False

    def return_books(self, book):
        if book in self.initial_books and book not in self.books:
            self.books.append(book)
            return True
        else:
            return False

    def missing_books(self):
        missing = [book for book in self.initial_books if book not in self.books]
        return missing

class lib1(Library):
    def __init__(self, books):
        initial_books = ["The Great Gatsby", "1984", "To Kill a Mockingbird"]
        super().__init__(books, initial_books)
    
