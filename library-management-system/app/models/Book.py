from .Author import Author


class Book:
    """A model of the Book object"""

    books = []

    def save(self, isbn, title, author_id):
        """
        Creates a book with the provided arguments

        Args:
            isbn (str): A 13 digit string numbers
            title (str): title of the book
            author_id (int): author's id

        Returns:
            book (dict): A book dictionary
        """

        # First check if book exists
        if not self.find(title):
            self.isbn = isbn
            self.title = title
            self.author_id = author_id

            author = Author().get_author(self.author_id)
            if author:
                book = {
                    "isbn": self.isbn,
                    "title": self.title,
                    "author_id": self.author_id,
                }
                self.books.append(book)
                return {
                    "isbn": self.isbn,
                    "title": self.title,
                    "author": author,
                }
            else:
                return "Cannot create book, the author specified by the id {} was not Found!".format(
                    author_id
                )
        else:
            return "Book already exists"

    def find(self, title):
        """Finds a book by title"""
        for book in self.books:
            if book["title"].lower() == title.lower():
                author = Author().get_author(book["author_id"])
                return {
                    "isbn": book["isbn"],
                    "title": book["title"],
                    "author": author,
                }
            else:
                return None
