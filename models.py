class Book:
    def __init__(self, author: str, title: str, publisher: str,
                 year: int, pages: int, copies: int):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.copies = copies

    def __str__(self):
        return f"{self.author:20} | {self.title:25} | {self.publisher:15} | " \
               f"{self.year:4} | {self.pages:4} стр. | {self.copies:3} экз."

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.author == other.author and
                self.title == other.title and
                self.publisher == other.publisher and
                self.year == other.year)


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """Добавить книгу в библиотеку"""
        self.books.append(book)
    
    def remove_book(self, author, title, publisher, year):
        """Удалить книгу из библиотеки"""
        for i, book in enumerate(self.books):
            if (book.author == author and
                    book.title == title and
                    book.publisher == publisher and
                    book.year == year):
                self.books.pop(i)
                return True
        return False
