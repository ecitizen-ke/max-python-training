class Author:
    """A model of the Author object"""

    authors = []

    def create(self, id, first_name, last_name):
        """Creates an author with the arguments provided"""
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

        author = {}
        author["id"] = self.id
        author["first_name"] = self.first_name
        author["last_name"] = self.last_name

        if author:
            self.authors.append(author)
            return author

    def get_author(self, id):
        """Finds an author by the id provided"""
        for author in self.authors:
            if author["id"] == id:
                return author
            else:
                return None

    def get_authors(self):
        """Fetches all authors"""
        return self.authors

    def update(self, id, data):
        """Updates the details of an author"""
        author = self.get_author(id)
        if author:
            author.update({"first_name": data.get("first_name")})
            author.update({"last_name": data.get("last_name")})
            return author
        else:
            return None
