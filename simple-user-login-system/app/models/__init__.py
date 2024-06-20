from app.db import Connection


class User:
    def __init__(self):
        self.db = Connection()

    users = []

    def create(self, username, password):

        self.username = username
        self.password = password

        # Insert user data into the database
        user = [self.username, self.password]
        self.db.cursor.execute(
            "INSERT INTO users (username, password) VALUES(%s, %s)", user
        )

        # Commit
        self.db.conn.commit()

    def user_login(self, username, password):
        """select a record from the database table based on its username"""
        self.db.cursor.execute("SELECT * FROM users WHERE username=%s", [username])
        # Get the record tuple
        record = self.db.cursor.fetchone()

        # Unpack the tuple
        record_id, record_username, record_password = record
        if record and record_password == password:
            return True
