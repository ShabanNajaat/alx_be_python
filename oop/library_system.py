class Book:
    """Base class representing a book"""
    def _init_(self, title, author):
        """Initialize book with title and author"""
        self.title = title
        self.author = author
    
    def _str_(self):
        """String representation of the book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book"""
    def _init_(self, title, author, file_size):
        """Initialize ebook with additional file_size attribute"""
        super()._init_(title, author)
        self.file_size = file_size
    
    def _str_(self):
        """String representation of the ebook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical book"""
    def _init_(self, title, author, page_count):
        """Initialize print book with additional page_count attribute"""
        super()._init_(title, author)
        self.page_count = page_count
    
    def _str_(self):
        """String representation of the print book"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books"""
    def _init_(self):
        """Initialize library with empty books list"""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library collection"""
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library"""
        for book in self.books:
            print(book)
