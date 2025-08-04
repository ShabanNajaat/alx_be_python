class Book:
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance with title and author.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
            str: A string in the format "Book: title by author".
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance with title, author, and file size.

        Args:
            title (str): The title of the eBook.
            author (str): The author of the eBook.
 file_size (int): The file size of the eBook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the eBook.

        Returns:
            str: A string in the format "EBook: title by author, File Size: file_sizeKB".
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance with title, author, and page count.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The page count of the print book.
        """
        super().__init__(title, author)
        self.page_count = page_count

 def __str__(self):
        """
        Returns a string representation of the print book.

        Returns:
            str: A string in the format "PrintBook: title by author, Page Count: page_count".
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        for book in self.books:
            print(book)

