from app.db import Connection


class State:
    """This is a model of a state"""

    states = []

    def __init__(self):
        self.db = Connection()

    def get_states(self):
        """Get all states"""

        query = "SELECT * FROM states"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],
                    "population": row[3],
                    "year_admitted": row[4],
                }
                self.states.append(state)
            return self.states

    def filter(self):
        """Filter states by first letter"""

        query = "SELECT * FROM states WHERE name LIKE 'A%'"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],
                    "population": row[3],
                    "year_admitted": row[4],
                }
                self.states.append(state)
            return self.states

    def create(self, name, abbreviation, population, year_admitted):
        """Create state method"""

        self.name = name
        self.abbreviation = abbreviation
        self.population = population
        self.year_admitted = year_admitted

        state = (self.name, self.abbreviation, self.population, self.year_admitted)

        query = "INSERT INTO states(name, abbreviation, population, year_admitted) VALUES(%s,%s,%s,%s)"

        self.db.cursor.execute(query, state)

        # If query execution is successful
        if self.db.cursor.rowcount:
            # Commit data to the database
            self.db.conn.commit()
            return {
                "name": self.name,
                "abbreviation": self.abbreviation,
                "population": self.population,
                "year_admitted": year_admitted,
            }
