#!/usr/bin/env python


class Book:
    """This class represents a book model"""

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __str__(self):
        self.book = dict(isbn=self.isbn, title=self.title, author=self.author)
        return f"{self.book}"


class Library:
    """This is a model of the Library object"""

    def __init__(self):
        self.books = []


def run():
    """This function runs the application"""


if __name__ == "__main__":
    run()
