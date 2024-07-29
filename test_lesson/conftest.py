import pytest

from libr import Book, Library


@pytest.fixture()
def library():
    books = [
        Book("a", "aa", "aaa", 111),
        Book("b", "bb", "bbb", 222),
        Book("c", "cc", "ccc", 333),
    ]
    library = Library()
    for book in books:
        library.add_book(book)

    yield library

    del library
