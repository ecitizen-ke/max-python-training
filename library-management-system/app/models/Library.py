from .Book import Book


class Library:
    """A model of the Library object"""

    library = []

    def __init__(self):
        self.books = Book().books

    def add_book(self, title):
        """Adds book to the library"""
        # First check if book already exists in library
        if not self.search(title):
            book = Book().find(title)
            if book:
                book.update({"checked_out": False, "checked_in": False})
                self.library.append(book)
                return book
            else:
                return "Such a book does not exist"
        else:
            return "Book already exists in the library"

    def search(self, title):
        """Searches for a book by title in the library"""
        for book in self.library:
            if book["title"].lower() == title.lower():
                return book
            else:
                return None

    def get_books(self):
        """Fetches all the books available in the library"""
        if self.library:
            return self.library
        else:
            return "We currently have no book in our library"

    def checkout(self, title):
        """Checks out a book from the library"""
        book = self.search(title)

        # First, check if the book exists and not already checked out from the library
        if book:
            # Confirm that the book is available for borrowing
            if not book["checked_out"]:
                book["checked_out"] = True
                book["checked_in"] = False
                return f"You have successfully checked out the book {title}!"
            else:
                return f"{title} has been checkout out. Please try again later!"

    def checkin(self, title):
        """Returns a book back to the library"""
        book = self.search(title)
        # First, check if the book exists in the library
        if book:
            # Confirm that the book has not been returned
            if not book["checked_in"]:
                book["checked_out"] = False
                book["checked_in"] = True
                return f"Thank you for returning {title} to the library!"
            else:
                return (
                    f"Sorry, we have {title} in our library. Could this be a mistake?"
                )
