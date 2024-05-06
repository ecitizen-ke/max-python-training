#!/usr/bin/env python


class Library:
    """This is a model of the Library object"""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """method that adds a book to the library"""
        # unpack the book tuple object in order to create a dictionary
        isbn, title, author = book
        bk = dict(isbn=isbn, title=title, author=author)

        # add book to the books list
        self.books.append(bk)
        # return the added book as a dictionary
        return bk

    def __str__(self):
        return f"{self.books}"


def run():
    """This function runs the application"""
    # inititialize the Library object
    library = Library()

    # inititialize two Book objects: book1 and book2
    book = ("0000000000001", "Introduction to Python", "Mr Mesfin Githinji")

    # Add both books to the library
    library.add_book(book)

    print(str(library.books))


if __name__ == "__main__":
    run()
