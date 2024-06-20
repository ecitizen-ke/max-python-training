from app.db import Connection


class User:
    def __init__(self):
        self.db = Connection()

    def create(self, username, password):

        self.username = username
        self.password = password

        # User data
        user = (self.username, self.password)

        query = "INSERT INTO users (username, password) VALUES(%s, %s)"

        # Execute query that inserts user data into the database
        self.db.cursor.execute(query, user)

        # Commit data to the database
        self.db.conn.commit()
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def user_login(self, username, password):
        """select a record from the database table based on its username"""
        query = "SELECT * FROM users WHERE username=%s"
        self.db.cursor.execute(query, [username])

        # Retrieve the user record in the database: returns a tuple
        record = self.db.cursor.fetchone()

        # Compare database password with given password
        if record and record[2] == password:
            return True

        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
