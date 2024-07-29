from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: str
    pages: int


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)

    def find_by_title(self, title):
        retval = []
        for book in self._books:
            if book.title == title:
                retval.append(book)

        return retval


# book = Book('aaa', 'bbb', 'ccc', 123)
#
# print(book.title)
