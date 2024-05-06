#!/usr/bin/env python
import json


class Book:
    """This is Book object model"""

    def save(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        # return book data as a tuple
        return (self.isbn, self.title, self.author)


class Library:
    """This is a model of the Library object"""

    def __init__(self):
        # read data from file
        with open("books.json", "r", encoding="utf-8") as file:
            self.books = json.load(file)
        file.close()

    def add_book(self, book):
        """method that adds a book to the library"""
        # unpack the book tuple object in order to create a dictionary
        isbn, title, author = book
        bk = dict(isbn=isbn, title=title, author=author)
        # add book to the books list
        self.books.append(bk)
        commit(self.books, "w")
        # return the added book as a dictionary
        return bk

    def display_all_books(self):
        """method that displays all books in the library"""
        print(self.books)

    def search_book_by_title(self, title):
        """method that searches a book in the library by title"""
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
            else:
                return "A book by that title is not available in our library"

    def book_checkout(self, title):
        """method that checks out a book from the library"""

        # First, search the book by title
        for book in self.books:
            if book["title"].lower() == title.lower():
                # Check if the book is availabe but has never been checkout out before
                if "checked_in" not in book:
                    # checkout the book
                    book.update({"checked_out": True, "checked_in": False})
                    commit(self.books, "w+")
                    print(f"You have successfully checked out the book {title}!")
                # Else check if the book is availabe, not checked out and is checked in
                elif not book["checked_out"] and book["checked_in"]:
                    # checkout the book
                    book.update({"checked_out": True, "checked_in": False})
                    commit(self.books, "w+")

                    print(f"You have successfully checked out the book {title}!")
                else:
                    print(f"The book {title} is not available at the moment!")

    def display_checked_out_books(self):
        """method that displays a list of checked out books in the library"""
        for books in self.books:
            if "checked_out" in books and books["checked_out"]:
                print(books)


def commit(object, flag):
    """Persist the transaction in the file"""
    with open("books.json", flag, encoding="utf-8") as file:
        json.dump(object, file, ensure_ascii=False, indent=2)
    file.close()


def run():
    """This function runs the application"""
    # inititialize the Library object
    library = Library()
    book = Book().save("0000000000005", "A Primer to Kubernetes", "Maxwel Barno")
    library.add_book(book)
    library.book_checkout("Morris Green")
    library.display_checked_out_books()


if __name__ == "__main__":
    run()
